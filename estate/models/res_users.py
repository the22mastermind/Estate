# -*- coding: utf-8 -*-

from odoo import models, fields


class ResUsers(models.Model):
  _inherit = 'res.users'

  property_ids = fields.One2many('estate.property', 'salesperson', string='Properties', domain='[("state", "=", "new"), ("state", "=", "offer_received")]')
