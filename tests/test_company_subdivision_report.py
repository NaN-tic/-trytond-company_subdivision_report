#!/usr/bin/env python
# This file is part company_subdivision_report module for Tryton.
# The COPYRIGHT file at the top level of this repository contains
# the full copyright notices and license terms.
import unittest
import trytond.tests.test_tryton
from trytond.tests.test_tryton import test_view, test_depends


class CompanySubdivisionReportTestCase(unittest.TestCase):
    'Test Company Subdivision Report module'

    def setUp(self):
        trytond.tests.test_tryton.install_module('company_subdivision_report')

    def test0005views(self):
        'Test views'
        test_view('company_subdivision_report')

    def test0006depends(self):
        'Test depends'
        test_depends()


def suite():
    suite = trytond.tests.test_tryton.suite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(
            CompanySubdivisionReportTestCase))
    return suite
