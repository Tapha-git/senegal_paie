===========================
Senegal Payroll for Odoo 19
===========================

Overview
========

This module provides a commercial-ready payroll localization base for Senegal
on Odoo 19.

It includes:

* Senegal payroll contract settings
* Salary rule categories
* Salary rules for:
  * base salary
  * taxable and non-taxable allowances
  * IPRES employee and employer
  * CSS employee and employer
  * TRIMF
  * IR with family quotient support
  * net salary
* A dedicated Senegal payroll structure
* Company-level payroll settings for rates and ceilings

Main Contract Fields
====================

* Tax parts
* Seniority bonus
* Transport allowance
* Representation allowance
* Other taxable allowance
* Other non-taxable allowance

Functional Notes
================

This addon is designed as a strong starting point for a paid Odoo Apps module.
Before production deployment or publication as a legally compliant payroll
solution, validate all payroll logic, rates, ceilings, tax brackets, accounting
impacts and declarations with a Senegal payroll specialist or chartered
accountant.

Technical Notes
===============

* Target version: Odoo 19
* Dependency: ``hr_payroll_community``
* License: ``OPL-1``

Accounting
==========

For payroll accounting, use the companion module
``l10n_sn_payroll_account`` with the payroll accounting addon available in your
Odoo stack.
