{
    "name": "Senegal Payroll for Odoo 19",
    "version": "19.0.1.0.0",
    "summary": "Senegal payroll localization with payroll rules, structures, and contract configuration",
    "description": """
Senegal Payroll Localization for Odoo 19
========================================

This module provides a payroll foundation for Senegal:

* Senegal-specific payroll structure
* Salary rules for gross salary, IPRES, CSS, TRIMF, IR and net salary
* Contract-level Senegal payroll configuration
* Odoo Apps-ready technical packaging

Important:
This module is a technical payroll base and must be validated against the
latest legal, tax, social and accounting requirements before production use.
""",
    "author": "Tapha",
    "website": "https://github.com/Tapha-git",
    "category": "Human Resources/Payroll",
    "license": "OPL-1",
    "depends": [
        "hr_contract",
        "payroll",
    ],
    "data": [
        "data/hr_payroll_data.xml",
        "views/hr_contract_views.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
    "application": False,
}
