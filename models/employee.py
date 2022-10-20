from odoo import api, fields, models

class WaterPlantManagementEmployee(models.Model):
    _name = "water_plant_management.employee"

    name = fields.Char(string="Employee Name")
    mobile_no = fields.Char(string="Mobile No.")
    email = fields.Char(string="Email")
    employee_id = fields.Char("Employee Id")
    address = fields.Text(string="Address")
    join_date = fields.Date("Joining Date")
    salary = fields.Integer("Salary")
    