from odoo import models

class EstateProperty(models.Model):
  _inherit = 'estate.property'

  def action_set_status_sold(self):
    """Set a property as sold, create invoice"""

    journal = self.env['account.move'].with_context(default_move_type='out_invoice')._get_default_journal()
    for record in self:
      invoice_vals = {
        'partner_id': record.salesperson,
        'move_type': 'out_invoice',
        'journal_id': journal.id,
        'invoice_line_ids': [{
            'name': f'6% of the selling price',
            'quantity': 1,
            'price_unit': record.selling_price*(6/100),
          },
          {
            'name': 'Additional 100.00 administrative fees',
            'quantity': 1,
            'price_unit': record.selling_price+100.00,
          },
        ],
      }
      self.env['account.move'].sudo().with_context(default_move_type='out_invoice').create(invoice_vals)
    
    return super(EstateProperty, self).action_set_status_sold()
