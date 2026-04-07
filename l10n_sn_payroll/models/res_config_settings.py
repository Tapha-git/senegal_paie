from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    sn_ipres_employee_rate = fields.Float(
        related="company_id.sn_ipres_employee_rate",
        readonly=False,
    )
    sn_ipres_employer_rate = fields.Float(
        related="company_id.sn_ipres_employer_rate",
        readonly=False,
    )
    sn_ipres_ceiling = fields.Float(
        related="company_id.sn_ipres_ceiling",
        readonly=False,
    )
    sn_css_employee_rate = fields.Float(
        related="company_id.sn_css_employee_rate",
        readonly=False,
    )
    sn_css_employer_rate = fields.Float(
        related="company_id.sn_css_employer_rate",
        readonly=False,
    )
    sn_css_ceiling = fields.Float(
        related="company_id.sn_css_ceiling",
        readonly=False,
    )
    sn_professional_expense_rate = fields.Float(
        related="company_id.sn_professional_expense_rate",
        readonly=False,
    )
    sn_professional_expense_min = fields.Float(
        related="company_id.sn_professional_expense_min",
        readonly=False,
    )
    sn_professional_expense_max = fields.Float(
        related="company_id.sn_professional_expense_max",
        readonly=False,
    )
