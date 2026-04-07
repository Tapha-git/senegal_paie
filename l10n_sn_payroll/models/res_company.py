from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    sn_ipres_employee_rate = fields.Float(
        string="IPRES Employee Rate",
        default=5.6,
        help="Employee IPRES rate in percent.",
    )
    sn_ipres_employer_rate = fields.Float(
        string="IPRES Employer Rate",
        default=8.4,
        help="Employer IPRES rate in percent.",
    )
    sn_ipres_ceiling = fields.Float(
        string="IPRES Ceiling",
        default=1700000.0,
        help="Monthly ceiling used to compute IPRES.",
    )
    sn_css_employee_rate = fields.Float(
        string="CSS Employee Rate",
        default=3.0,
        help="Employee CSS rate in percent.",
    )
    sn_css_employer_rate = fields.Float(
        string="CSS Employer Rate",
        default=7.0,
        help="Employer CSS rate in percent.",
    )
    sn_css_ceiling = fields.Float(
        string="CSS Ceiling",
        default=63000.0,
        help="Monthly ceiling used to compute CSS.",
    )
    sn_professional_expense_rate = fields.Float(
        string="Professional Expense Deduction Rate",
        default=20.0,
        help="Annual professional expense deduction rate in percent for IR.",
    )
    sn_professional_expense_min = fields.Float(
        string="Professional Expense Minimum",
        default=336000.0,
        help="Minimum annual professional expense deduction for IR.",
    )
    sn_professional_expense_max = fields.Float(
        string="Professional Expense Maximum",
        default=672000.0,
        help="Maximum annual professional expense deduction for IR.",
    )
