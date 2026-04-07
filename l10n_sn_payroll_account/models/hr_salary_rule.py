from odoo import fields, models


class HrSalaryRule(models.Model):
    _inherit = "hr.salary.rule"

    sn_reporting_code = fields.Char(
        string="Senegal Reporting Code",
        help="Internal code used for Senegal declarations and reporting.",
    )
    sn_is_employer_charge = fields.Boolean(
        string="Employer Charge",
        help="Identify contributions that must be posted as employer charges.",
    )
