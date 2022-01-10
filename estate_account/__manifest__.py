# -*- coding: utf-8 -*-
{
    'name': "estate_account",

    'summary': """
        Estate and Account link module""",

    'description': """
        A module to link estate and invoicing modules.
    """,

    'author': "SIC Ltd",
    'website': "https://www.sicrwanda.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
      'estate',
      'account',
    ],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        # 'demo/demo.xml',
    ],
    'application': True,
}
