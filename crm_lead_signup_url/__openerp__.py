# -*- encoding: utf-8 -*-
##############################################################################
#    
#    Odoo, Open Source Management Solution
#
#    Author: Andrius Laukavičius. Copyright: JSC Boolit
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
    'name': 'Lead/Opportunity access link method',
    'version': '0.1',
    'category': 'Tools',
    'summary': 'url, custom, method, crm',
    'description': """
	Implements custom method to access crm.lead records as links
	""",
    'author': 'OERP',
    'website': 'www.oerp.eu',
    'depends': [  
        'crm', 'auth_signup',    
    ],
    'data': [
        #'security/ir.model.access.csv',
        #'views/',
        #'data/',        

    ],
    'demo': [
    ],
    'test': [

    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'images': [],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
