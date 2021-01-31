#!#/bin/bash

sudo docker run --rm -it \
    -p 8069:8069 -p 8072:8072 \
    -v /odoo_ar/odoo-12.0/ou12/config:/opt/odoo/etc/ \
    -v /odoo_ar/odoo-12.0/ou12/data_dir:/opt/odoo/data \
    -v /odoo_ar/odoo-12.0/ou12/log:/var/log/odoo \
    -v /odoo_ar/odoo-12.0/ou12/sources:/opt/odoo/custom-addons \
    -v /odoo_ar/odoo-12.0/ou12/backup_dir:/var/odoo/backups/ \
    --link pg-ou12:db \
    --name ou12 \
    -e ODOO_CONF=/dev/null \
    jobiols/odoo-jeo:12.0.ou --logfile=/dev/stdout


#    --link wdb \
#    -e WDB_SOCKET_SERVER=wdb \
#    -v /odoo_ar/odoo-12.0/extra-addons:/opt/odoo/extra-addons \
#    -v /odoo_ar/odoo-12.0/dist-packages:/usr/lib/python3/dist-packages \
#    -v /odoo_ar/odoo-12.0/dist-local-packages:/usr/local/lib/python3.5/dist-local-packages \
