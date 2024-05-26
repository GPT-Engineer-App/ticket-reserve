# models/ticket_reservation.py
from odoo import models, fields, api

class TicketReservation(models.Model):
    _name = 'ticket.reservation'
    _description = 'Ticket Reservation'

    name = fields.Char(string='Reservation Name', required=True)
    event_date = fields.Date(string='Event Date', required=True)
    customer_name = fields.Char(string='Customer Name', required=True)
    number_of_tickets = fields.Integer(string='Number of Tickets', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled')
    ], string='Status', default='draft')

    def action_confirm(self):
        self.state = 'confirmed'

    def action_cancel(self):
        self.state = 'cancelled'