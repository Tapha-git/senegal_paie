{
    "name": "Senegal Payroll Accounting for Odoo 19",
    "version": "19.0.1.0.0",
    "summary": "Accounting bridge for Senegal payroll rules",
    "description": """
Companion module for Senegal Payroll for Odoo 19.

This addon adds accounting fields and starter mappings for Senegal payroll
rules when a payroll accounting addon is available in the Odoo stack.
""",
    "author": "Tapha",
    "website": "https://github.com/Tapha-git",
    "support": "taphaaaly.ml@gmail.com",
    "category": "Hidden",
    "license": "OPL-1",
    "depends": [
        "l10n_sn_payroll",
        "hr_payroll_account_community",
    ],
    "data": [
        "views/hr_salary_rule_views.xml",
    ],
    "installable": True,
    "application": False,
}
