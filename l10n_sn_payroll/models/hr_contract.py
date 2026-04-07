from odoo import fields, models


class HrContract(models.Model):
    _inherit = "hr.contract"

    sn_tax_parts = fields.Float(
        string="Senegal Tax Parts",
        default=1.0,
        help="Number of tax parts used for family quotient tax computation.",
    )
    sn_seniority_bonus = fields.Monetary(
        string="Seniority Bonus",
        currency_field="currency_id",
        help="Taxable seniority bonus included in payroll computation.",
    )
    sn_transport_allowance = fields.Monetary(
        string="Transport Allowance",
        currency_field="currency_id",
        help="Taxable transport allowance included in payroll computation.",
    )
    sn_representation_allowance = fields.Monetary(
        string="Representation Allowance",
        currency_field="currency_id",
        help="Taxable representation allowance included in payroll computation.",
    )
    sn_other_taxable_allowance = fields.Monetary(
        string="Other Taxable Allowance",
        currency_field="currency_id",
        help="Any other taxable allowance to include in payroll computation.",
    )
    sn_other_nontaxable_allowance = fields.Monetary(
        string="Other Non-taxable Allowance",
        currency_field="currency_id",
        help="Allowance added to net pay but excluded from taxable income.",
    )
