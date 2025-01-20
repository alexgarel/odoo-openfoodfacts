# odoo-openfoodfacts

Some odoo related stuff that we use at openfoodfacts.

It would be great to transform that into a real module.

## Copying a change

Right now to copy changes from the platform,
I use the "export" action and then use `yq` to transform the csv into yaml.

`yq -p "csv" -oy exported.csv > exported.yaml`
