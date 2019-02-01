# -*- coding: utf-8 -*-
from odoo import http

# class ModuloOdoo11(http.Controller):
#     @http.route('/modulo_odoo11/modulo_odoo11/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo_odoo11/modulo_odoo11/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo_odoo11.listing', {
#             'root': '/modulo_odoo11/modulo_odoo11',
#             'objects': http.request.env['modulo_odoo11.modulo_odoo11'].search([]),
#         })

#     @http.route('/modulo_odoo11/modulo_odoo11/objects/<model("modulo_odoo11.modulo_odoo11"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo_odoo11.object', {
#             'object': obj
#         })