# Compliance Notes

This module has been prepared to be safer for commercialization, but it still
requires legal validation before production use.

Current implementation choices:

- Main Senegal payroll rates and ceilings are configurable at company level.
- IR keeps a family quotient approach through contract tax parts.
- A companion accounting addon is provided for payroll posting enrichment.

Validation sources to review before sale:

- Odoo payroll structure documentation for version 19
- DGID publications and tax procedures
- Official Senegal social institution publications for IPRES and CSS

Recommended next legal checks:

- current IPRES ceilings and split between employer and employee
- CSS basis and employer rates by risk class if applicable
- annual IR brackets and quotient limits
- TRIMF applicability and current schedule
- employer declarations and year-end reporting formats
