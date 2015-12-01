# This file is part of the company_subdivision_report module for Tryton.
# The COPYRIGHT file at the top level of this repository contains the full
# copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import ModuleTestCase


class CompanySubdivisionReportTestCase(ModuleTestCase):
    'Test Company Subdivision Report module'
    module = 'company_subdivision_report'


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
        CompanySubdivisionReportTestCase))
    return suite