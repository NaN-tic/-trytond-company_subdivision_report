#This file is part company_subdivision module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool, PoolMeta
from trytond.transaction import Transaction
from trytond.config import config
import os

__all__ = ['CompanySubdivision']
__metaclass__ = PoolMeta


class CompanySubdivision:
    __name__ = "company.subdivision"

    @classmethod
    def __register__(cls, module_name):
        super(CompanySubdivision, cls).__register__(module_name)
        # create directory
        database_name = Transaction().database.name
        directory = os.path.join(config.get('database', 'path'),
            database_name, "reports")
        if not os.path.isdir(directory):
            os.makedirs(directory)
 
    @staticmethod
    def report_directory(data):
        '''Return report directory (full path) from user subdivision'''
        pool = Pool()
        ReportSubdivision  = pool.get('action.report.company.subdivision')
        User = pool.get('res.user')

        report_directory = None

        user = User(Transaction().user)
        if user.subdivision:
            subdivision_reports = ReportSubdivision.search([
                ('report', '=', data.get('action_id')),
                ('subdivision', '=', user.subdivision),
                ], limit=1)
            if not subdivision_reports:
                return report_directory
            subdivision_report, = subdivision_reports

            if subdivision_report.directory:
                directory = subdivision_report.directory
                # create directory
                cursor = Transaction().connection.cursor()
                report_directory = os.path.join(config.get('database', 'path'),
                    cursor.database_name, "reports", directory)
                if not os.path.isdir(report_directory):
                    os.makedirs(report_directory)

        return report_directory
