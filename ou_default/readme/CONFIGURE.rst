Configuración de la migración

Proyecto a migrar = SRC

Se crea el proyecto SRC y se restaura la bd a migrar
Se crea el proyecto ou12 con los mismos repos que el SRC

En los tres yml el pg-migrate debe apuntar a la bd a migrar.

migrate.yml
-----------

Ejecuta la migración in situ en la base original haciendo un
update all, se hace con la imagen jobiols/odoo-jeo:xx.0.ou

update-migrated.yml
-------------------

Hace un update all con la imagen normal

test_odoo_target.yml
--------------------

Arranca odoo para verlo por http en 8069
