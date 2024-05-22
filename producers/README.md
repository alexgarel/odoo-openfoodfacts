# Producers

- Fields :

  - x_off_org_id
  - x_main_contact
  - x_last_import_date
  - x_last_export_date

- Inherited view:

  - res.partner :
    - button to open org in pro platform (when partner is 'company')
    - new custom off fields in res.partner

- Automated action:

  - new org welcome (sends an email to the main contact)

- Server Action:
  - Open in pro plateform as org (res.partner)

[Dasel](https://github.com/TomWright/dasel) was used to transform Odoo csv exports into yaml :

```sh
cat data.csv | dasel -r csv -w yaml
```
