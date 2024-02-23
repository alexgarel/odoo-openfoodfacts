TRANSLATE_ATTR = {"tooltip", "legend", "html", "label"}

if record:
  records = [record]
elif records:
  records = list(records)
  
def batch(l, n):
  results = []
  result = []
  for e in l:
    result.append(e)
    if len(result) >= n:
      results.append(result)
      result = []
  if result:
    results.append(result)
  return results
  
VALID_KEY_CHARS = set("0123456789abcdefghijklmnopqrstuvwxyz")

def value_to_key(value, default):
  # we can't use codecs module :'(
  last = None
  chars = ["off_"]
  for c in value.lower():
    if c in VALID_KEY_CHARS:
      chars.append(c)
      last = c
    elif last != "_":
      chars.append("_")
      last = "_"
  return "".join(chars[:100]).strip("_")

def get_translations(elt, prefix=""):
    translations = []
    sub_elt = []
    if isinstance(elt, list):
        sub_elt = list(enumerate(elt))
    elif isinstance(elt, dict):
        for attr in TRANSLATE_ATTR:
            value = elt.get(attr)
            if value:
                translations.append((value_to_key(value, ("%s_%s" % (prefix, attr)).lstrip("_")), value))
        sub_elt = list(elt.items())
    for name, e in sub_elt:
        translations.extend(get_translations(e, prefix="%s_%s" % (prefix, name)))
    return translations

for record in records:
  jsform = json.loads(record["schema"])
  all_translations = list(get_translations(jsform))
  for translations in batch(all_translations, 100):
    translations = dict(translations)
    # update existing
    existing = env["formio.translation.source"].search([("property", "in", list(translations.keys()))])
    for e in existing:
      value = translations[e.property]
      if e.source != value:
        e.write({"source": value})
    # update
    existing.flush()
    # create missing
    missing = set(translations.keys()) - set(e.property for e in existing)
    env["formio.translation.source"].create([{"property": prop, "source": translations[prop]} for prop in missing])
    # ensure french translations exists
    # FIXME TODO
