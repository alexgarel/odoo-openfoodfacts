# Producers

- Fields :

  - x_off_org_id
  - x_off_main_contact
  - x_off_last_import_date
  - x_off_last_export_date
  - x_off_last_logged_org_contact
  - x_off_last_template_download_date
  - x_off_last_import_type
  - x_off_user_login_date
  - x_off_public_products
  - x_off_pro_products

- Inherited view:

  - res.partner.form > res.partner.form_off_pro:
    - button to open org in pro platform (when partner is 'company')
    - new custom off fields, see ir_model_fields.yml

- Automated action:

  - [email] new org welcome (sends an email to the org main contact)

- Email templates:

  - New org - welcome

- Server Action:

  - Open in pro plateform as org (res.partner)

- Tags (crm.tag): onboarding

- Category (res.partner.category): Producer, AGENA3000, EQUADIS, CSV, Manual import, BAYARD, SFTP

[Dasel](https://github.com/TomWright/dasel) was used to transform Odoo csv exports into yaml :

```sh
cat data.csv | dasel -r csv -w yaml
```
