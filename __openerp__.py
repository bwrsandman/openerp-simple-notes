{
    'name': 'Very Simple Note Addon',
    'version': '1.0',
    'description': """\
This module is a very simple "notes" addon for OpenERP.""",
    "category": "Generic Modules/Others",
    'author': 'Sandy Carter @ SavoirFaireLinux',
    'website': 'http://www.savoirfairelinux.com',
    'depends': ['base'],
    'data': ['simple_note_view.xml'],
    'js': ['static/src/js/simple_widget.js'],
    'qweb': ['static/src/xml/simple_widget.xml'],
    'demo': ['simple_note_demo.xml'],
    'test': [],
    'installable': True,
}
