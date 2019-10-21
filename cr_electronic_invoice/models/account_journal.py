# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
import logging

_logger = logging.getLogger(__name__)


class AccountJournalInherit(models.Model):
    _name = 'account.journal'
    _inherit = 'account.journal'

    sucursal = fields.Integer(string="Sucursal", required=False, default="1")
    terminal = fields.Integer(string="Terminal", required=False, default="1")

    FE_sequence_id = fields.Many2one(comodel_name="ir.sequence",
                                     string="Secuencia de Facturas Electrónicas",
                                     required=False)
    TE_sequence_id = fields.Many2one(comodel_name="ir.sequence",
                                     string="Secuencia de Tiquetes Electrónicos",
                                     required=False)
    FEE_sequence_id = fields.Many2one(comodel_name="ir.sequence",
                                      string="Secuencia de Facturas Electrónicas de Exportación",
                                      required=False)
    NC_sequence_id = fields.Many2one(comodel_name="ir.sequence",
                                     string="Secuencia de Notas de Crédito Electrónicas",
                                     required=False)
    ND_sequence_id = fields.Many2one(comodel_name="ir.sequence",
                                     string="Secuencia de Notas de Débito Electrónicas",
                                     required=False)

    @api.model
    def set_sequences(self):
        for record in self.search([]):
            record.FE_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequece.FE')], limit=1)[0]
            record.TE_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequece.TE')], limit=1)[0]
            record.FEE_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequece.FEE')], limit=1)[0]
            record.NC_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequece.NC')], limit=1)[0]
            record.ND_sequence_id = self.env['ir.sequence'].search([('code', '=', 'sequece.ND')], limit=1)[0]
