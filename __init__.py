#This file is part company_subdivision_report module for Tryton.
#The COPYRIGHT file at the top level of this repository contains 
#the full copyright notices and license terms.
from trytond.pool import Pool
from .report import *
from .company import *

def register():
    Pool.register(
        ActionReport,
        ActionReportCompanySubdivision,
        CompanySubdivision,
        module='company_subdivision_report', type_='model')
