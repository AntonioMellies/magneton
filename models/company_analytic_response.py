from models.base.response import Response
from models.enums.analytic_result_type_enum import AnalyticResultType


class CompanyAnalyticResponse(Response):
    cnpjPublic: AnalyticResultType = AnalyticResultType.NOT_PERFORMED
    emailPublic: AnalyticResultType = AnalyticResultType.NOT_PERFORMED
    phonePublic: AnalyticResultType = AnalyticResultType.NOT_PERFORMED
    ssl: AnalyticResultType = AnalyticResultType.NOT_PERFORMED
    https: AnalyticResultType = AnalyticResultType.NOT_PERFORMED
