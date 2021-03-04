from odoo import models, fields, api
from datetime import date, datetime

class Product(models.Model):
    _name = 'product'

    image = fields.Binary('Product image')
    name = fields.Char('Name', required=True)
    description = fields.Text('Description')
    price = fields.Float('Price')
    stock = fields.Integer('Stock', default=1)

    @api.constrains('stock')
    def _check_stock(self):
        for product in self:
            if product.stock < 0:
                raise models.ValidationError('Stock must be a positive number')

    @api.constrains('price')
    def _check_price(self):
        for product in self:
            if product.price < 0:
                raise models.ValidationError('Price must be a positive number')

class Consumer(models.Model):
    _name = 'consumer'
    _inherits = {'res.partner': 'partner_id'}

    @api.multi
    def set_phone_number(self):
        for consumer in self:
            consumer.phone = consumer.partner_id.phone

    partner_id = fields.Many2one('res.partner', ondelete='cascade', string='Name')
    phone = fields.Char('Phone', compute=set_phone_number)
    country = fields.Many2one('res.country', 'Country')
    date_of_birth = fields.Date('Date of birth')

class Sale(models.Model):
    _name = 'sale'
    _rec_name = 'consumer'

    consumer = fields.Many2one('consumer', required=True)
    product = fields.Many2one('product', required=True)
    date_of_sale = fields.Date('Date of Sale', default=lambda *a:datetime.now().strftime('%Y-%m-%d'))
    quantity = fields.Integer('Quantity', default=1)
    discount = fields.Integer('Discount (%)')

    @api.multi
    def get_price(self):
        for sale in self:
            product = sale.product
            discounted_product = product.price - (product.price * (sale.discount / 100))
            sale.total_price = discounted_product * sale.quantity

    total_price = fields.Float('Total price', compute=get_price)

    @api.constrains('quantity')
    def _check_quantity(self):
        for sale in self:
            if sale.quantity > sale.product.stock:
                raise models.ValidationError('There is not enough stock')
            else:
                sale.product.stock = sale.product.stock - sale.quantity

            if sale.quantity < 0:
                raise models.ValidationError('Quantity must be a positive number')

    @api.constrains('discount')
    def _check_discount(self):
        for sale in self:
            if sale.discount < 0:
                raise models.ValidationError('Discount must be a positive number')