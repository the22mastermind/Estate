# -*- coding: utf-8 -*-
{
    'name': "estate",

    'summary': """
        A real estate business module""",

    'description': """
        A module to manage a small real estate business, allowing the management
        of properties, offers, and users.
    """,

    'author': "SIC Ltd",
    'website': "https://www.sicrwanda.com/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/estate_property_actions.xml',
        'data/estate_property_type_actions.xml',
        'data/estate_property_tag_actions.xml',
        'data/estate_property_offer_actions.xml',
        'views/estate_property_types_views.xml',
        'views/estate_property_tags_views.xml',
        'views/estate_property_offers_views.xml',
        'views/estate_property_views.xml',
        'views/res_users_views.xml',
        'views/templates.xml',
        'views/estate_menus.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
}
