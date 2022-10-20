from odoo import http
from odoo.http import request
from .. import models
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager

class PortalAccount(CustomerPortal):
    # For home page
    @http.route(['/my', '/my/home'], type='http', auth="user", website=True)
    def home(self, **kw):
        return request.render("read_emp_mail.portal_my_home_daily_mails", {})

    def _prepare_home_portal_values(self, counters):
        values = super()._prepare_home_portal_values(counters)
        current  = request.env['res.users'].browse(request.uid)
        daily_mails_count = request.env['emp_mail'].sudo().search_count([('name','=',current.name)])
        values['daily_mails_count'] = daily_mails_count
        return values


class DailyMails(http.Controller):
    @http.route('/my/daily_mails/',website=True, auth='user')
    def daily_mails_con(self,**kw):
        current  = request.env['res.users'].browse(request.uid)
        mails = request.env['emp_mail'].sudo().search([('name.name','=',current.name)])
        
        return request.render('read_emp_mail.daily_mails_web_view', {'mails':mails})

        
    @http.route('/my/daily_mails/',website=True, auth='user')
    def daily_mails_con(self,**kw):
        current  = request.env['res.users'].browse(request.uid)
        mails = request.env['emp_mail'].sudo().search([('name.name','=',current.name)])
        
        return request.render('read_emp_mail.daily_mails_web_view', {'mails':mails})
        # return f"<h1>Hello There</h1><br>{mails}"

    @http.route(['/my/view_mail/'], type='http', website=True, auth='user')
    def view_mail_con(self, mail_id):
        print("#####   Mail id : ",mail_id)
        read_mail = request.env['emp_mail'].sudo().search([('id','=',mail_id)])

        # return f"<h1>Hello There</h1><br>{read_mail}"
        
        return request.render('read_emp_mail.view_mail_web_view', {'read_mail':read_mail})




    
