{
    'name': 'Biodata',
    'version': '1.0',
    'summary': 'Module for managing biodata',
    'author': 'Syahrul',
    'category': 'Tools',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/biodata.views.xml',
        'views/menuitems.views.xml',
    ],
    'installable': True,
    'application': True,
}