#This file is part company_subdivision_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.model import ModelView, ModelSQL, fields
from trytond.pool import PoolMeta

__all__ = ['ActionReport', 'ActionReportCompanySubdivision']


class ActionReport:
    __metaclass__ = PoolMeta
    __name__ = 'ir.action.report'
    subdivisions = fields.One2Many('action.report.company.subdivision', 'report',
        'Subdivisions')


class ActionReportCompanySubdivision(ModelSQL, ModelView):
    'Action report Company Subdivision'
    __name__ = "action.report.company.subdivision"
    report = fields.Many2One('ir.action.report', 'Report', ondelete='CASCADE',
        select=True, required=True)
    subdivision = fields.Many2One('company.subdivision', 'Subdivision',
        ondelete='CASCADE', select=True, required=True)
    directory = fields.Char('Directory', required=True,
        help='Directory name (without "/")')
    active = fields.Boolean('Active')

    @staticmethod
    def default_active():
        return True
