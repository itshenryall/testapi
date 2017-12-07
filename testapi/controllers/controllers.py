# -*- coding: utf-8 -*-
from openerp import http

# class Testapi(http.Controller):
#     @http.route('/testapi/testapi/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/testapi/testapi/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('testapi.listing', {
#             'root': '/testapi/testapi',
#             'objects': http.request.env['testapi.testapi'].search([]),
#         })

#     @http.route('/testapi/testapi/objects/<model("testapi.testapi"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('testapi.object', {
#             'object': obj
#         })