try:
  # TEST !!! to test with url
  if record is None:
      # raise RuntimeError("Skill pool form: no record provided")  
      record = env["formio.form"].browse([247])[0]
      log("Producers support mail for form %s via web: %r" % (record.id, json.loads(record.submission_data)))

  form_data = json.loads(record.submission_data)
  
  # see https://www.odoo.com/fr_FR/forum/aide-1/send-email-with-python-96924
  mail_pool = env['mail.mail']
  body_html = [
      "<p>Hi, a producer needs help 😊</p>",
      "<p>Company name: %s</p>" % (form_data.get('nomDeVotreEntrepriseOuMarque', "-"),),
      "<p>Full name: %s</p>" % (form_data.get('votreAdresseEMailProfessionnelle', "-"),),
      "<p>Mail: %s - Tél: %s</p>" % (form_data.get('votreAdresseEMailProfessionnelle', "-"), form_data.get('numeroDeTelephoneFacultatifPourUnContactRapide', "-")),
      "<p>%s  Products − Structured data: %s  − %s</p>" % (
        form_data.get('combienDeProduitsSouhaitezVousAjouterALaBaseDeDonnees', "") or '?',
        form_data.get('disposezVousDejaDeDonneesStructureesPourVosProduits', ""),
        form_data.get('quelEstLeFormatActuelDeVosDonnees', "")
      ),
      "<p>Message:<br>%s</p>" % (form_data.get('enQuoiPouvonsNousVousAider', ""),),
  ]
  values={
    "subject": "Support request from Pro",
    "email_to": "producers@openfoodfacts.org",
    "body_html": "\n".join(body_html),
  }
  
  # try to attach to contact
  contact_email = form_data.get('votreAdresseEMailProfessionnelle')
  if contact_email:
    candidates = env["res.partner"].search([("email", "ilike", contact_email)], limit=1)
    if candidates:
      values["model"] = "res.partner"
      values["res_id"] = candidates[0].id

  msg_id = mail_pool.create(values)
  if msg_id:
    mail_pool.send([msg_id])

except Exception as e:
  log("Producers support email: Got exception %s (%r) while processing form %s" % (e, e, record.id), level='error')



