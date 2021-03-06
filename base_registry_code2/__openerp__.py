# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
    'name': 'Company Registry Code',
    'version': '1.1',
    'summary': 'Company Registry for partner and lead',
    'depends': ['base_vat', 'crm'],
    'author': 'OERP',
    'description': """
Address Book
==========================================

Adds new field - Company Registry Code in partners and also in leads. 
When contact is created from lead, also fills Company Registry if it was filled in lead. 

    """,
    'website': 'http://www.oerp.eu',
    'category': 'base',
    'demo': [],
    'test': [],
    'data': ['res_partner_view.xml',
             'crm_lead_view.xml',
    ],
    'auto_install': False,
    'installable': True,
}
