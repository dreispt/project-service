# -*- coding: utf-8 -*-
##############################################################################
#
#    Daniel Reis
#    2012
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
##############################################################################


{
    'name': 'Project Issue with Department',
    'version': '6.1.1',
    "category": "Project Management",
    'description': """\
Add Department field to Project Issues.
""",
    'author': 'Daniel Reis',
    'website': 'daniel.reis@securitas.pt',
    'depends': [
        'project_issue',
        #'project_department', #from lp:c2c-addons/6.1
    ],
    'init_xml': [
    ],
    'update_xml': [
        'project_issue_view.xml',
    ],
    'demo_xml': [],
    'test': [],
    'installable': True,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
