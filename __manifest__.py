# __manifest__.py
{
    'name': 'Ticket Reservation',
    'version': '17.0.1.0.0',
    'summary': 'Module for managing ticket reservations',
    'description': 'A simple module to manage ticket reservations.',
    'author': 'Your Name',
    'website': 'https://www.yourwebsite.com',
    'category': 'Uncategorized',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'security/ticket_reservation_security.xml',
        'views/ticket_reservation_views.xml',
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}