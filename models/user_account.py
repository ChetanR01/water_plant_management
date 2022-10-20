from odoo import api, fields, models

import base64
import qrcode
from io import BytesIO

# Model
class WaterPlantManagementUsers(models.Model):
    _name = "water_plant_management.users"

    name = fields.Char(string="Customer Name")
    mobile_no = fields.Char("Mobile No.")
    cust_id = fields.Char("Customer Unique Id")
    address = fields.Text("Address")
    email = fields.Char("Email")



    # @api.multi
    # def generate_qr(self, txt=''):
    #     qr_code = qrcode.QRCode(version=4, box_size=4, border=1)
    #     qr_code.add_data(txt)
    #     qr_code.make(fit=True)
    #     qr_img = qr_code.make_image()
    #     im = qr_img._img.convert("RGB")
    #     buffered = BytesIO()
    #     im.save(buffered, format="JPEG")
    #     img_str = base64.b64encode(buffered.getvalue()).decode('ascii')
    #     return img_str


    # base_url = self.env['ir.config_parameter'].get_param('web.base.url')
    # if not 'localhost' in base_url:
    #     if 'http://' in base_url:
    #         base_url = base_url.replace('http://', 'https://')
    # base_url = base_url + '/web#id=' + str(self.id) + '&model=your.model.goes.here&view_type=form&cids='