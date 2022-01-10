from odoo import models, fields, api
from datetime import date, datetime
from dateutil.relativedelta import relativedelta


class EstatePropertyOffer(models.Model):
  _name = 'estate.property.offer'
  _description = 'Estate Property Offer'
  _order = 'price desc'

  price = fields.Float()
  status = fields.Selection(
    selection=[('accepted', 'Accepted'), ('refused', 'Refused')],
    copy=False
  )
  partner_id = fields.Many2one('res.partner', required=True)
  property_id = fields.Many2one('estate.property', required=True)
  validity = fields.Integer(default=7)
  date_deadline = fields.Date(compute='_compute_deadline', inverse='_inverse_deadline')
  property_type_id = fields.Many2one(related='property_id.property_type_id', store=True)

  _sql_constraints = [
    ('check_price', 'CHECK(price > 0)', 'The offer price must be strictly positive')
  ]

  @api.model
  def create(self, vals):
    """At offer creation, set property state to 'Offer Received'"""
    self.env['estate.property.offer'].browse(vals['property_id'])
    record = self.env['estate.property'].search([('id', '=', vals['property_id'])], limit=1)
    record.state = 'offer_received'
    return super().create(vals)

  @api.depends('create_date', 'validity')
  def _compute_deadline(self):
    for record in self:
      if record.create_date:
        record.date_deadline = record.create_date + relativedelta(days=record.validity)
      else:
        record.date_deadline = date.today() + relativedelta(days=record.validity)

  def _inverse_deadline(self):
    for record in self:
      new_deadline = datetime.strptime(record.date_deadline.strftime('%Y-%m-%d'), '%Y-%m-%d')
      new_create_date = datetime.strptime(record.create_date.strftime('%Y-%m-%d'), '%Y-%m-%d')
      record.validity = abs((new_deadline - new_create_date).days)

  def action_accept_offer(self):
    for record in self:
      record.status = 'accepted'
      record.property_id.buyer = record.partner_id
      record.property_id.selling_price = record.price
      record.property_id.state = 'offer_accepted'
      for offer in record.property_id.offer_ids:
        if not offer.id == record.id:
          offer.status = 'refused'
      return True

  def action_refuse_offer(self):
    for record in self:
      record.status = 'refused'
      record.property_id.buyer = None
      record.property_id.selling_price = 0
      for offer in record.property_id.offer_ids:
        if not offer.id == record.id:
          offer.status = 'accepted'
      return True
