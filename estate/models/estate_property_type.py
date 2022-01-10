from odoo import models, fields, api

class EstatePropertyType(models.Model):
  _name = 'estate.property.type'
  _description = 'Estate Property Types'
  _order = 'sequence, name'

  name = fields.Char(required=True)
  property_ids = fields.One2many('estate.property', 'property_type_id', string='Properties')
  sequence = fields.Integer('Sequence', default=1, help='Used to order property types')
  offer_ids = fields.One2many('estate.property.offer', 'property_type_id', string='Offers')
  offer_count = fields.Integer(compute='_compute_offers')

  _sql_constraints = [
    ('name_unique', 'unique(name)', 'The property type must be unique')
  ]

  @api.depends('offer_ids')
  def _compute_offers(self):
    for record in self:
      record.offer_count = len(record.offer_ids)
