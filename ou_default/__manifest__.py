# -----------------------------------------------------------------------------
#
#    Copyright (C) 2020  jeo Software  (http://www.jeosoft.com.ar)
#    All Rights Reserved.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# -----------------------------------------------------------------------------
{
    'name': 'ou12',
    'version': '12.0.0.0.0',
    'license': 'AGPL',
    'category': 'Tools',
    'summary': 'Migration 11.0 > 12.0',
    'author': 'jeo Software',
    'depends': [],

    'data': [],
    'test': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': [],

    # Here begins odoo-env manifest configuration
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    # manifest version, if omitted it is backward compatible
    'env-ver': '2',

    # if Enterprise it installs in a different directory than community
    'odoo-license': 'CE',

    # port where odoo starts serving pages
    'port': '8069',

    # list of url repos to install in the form 'repo-url directory'
    'git-repos': [
        'https://github.com/jobiols/cl-ou.git -b 12.0',
    ],

    # list of images to use in the form 'name image-url'
    'docker-images': [
        'odoo jobiols/odoo-jeo:12.0.ou',
        'postgres postgres:10.1-alpine',
    ]}