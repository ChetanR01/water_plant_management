from email.policy import default
from odoo import api, fields, models
from datetime import datetime

class WaterPlantManagementDistribution(models.Model):
    _name = "water_plant_management.distribution"

    name = fields.Many2one(string="Customer Name", comodel_name="water_plant_management.users")
    payment_state = fields.Selection([("account", "Account"),("cash","Cash"),("online","Online")] ,string="Payment Mode", default="account")
    order_time = fields.Datetime("Order Time", default=datetime.now())
    delivered_time = fields.Datetime("Delivered Time")
    delivery_state = fields.Selection([("ordered", "Ordered"),("cancelled","Cancelled"),("delivered","Delivered")] ,string="Delivery Status", default="ordered")
    delivered_by = fields.Many2one(string="Delivered by", comodel_name="water_plant_management.employee")
