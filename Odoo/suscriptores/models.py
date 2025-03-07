# -*- coding: utf-8 -*-

from odoo import models, fields, api


class suscriptores(models.Model):
    _name = 'suscriptores.suscriptores'
    _description = 'suscriptores.suscriptores'

    name = fields.Char()
    apellidos = fields.Char()
    fecha_nacimiento = fields.Date()
    suscripcion = fields.Selection([('1','Normal'),('2','Gold'),('3','Premium')])