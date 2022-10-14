from analysis.analysis_base import AnalysisBase
from analysis.analysis_basic import AnalysisBasic
from analysis.analysis_contact import AnalysisContact
from analysis.analysis_full import AnalysisFull
from analysis.analysis_security import AnalysisSecurity
from models.enums.analysis_type_enum import AnalysisType
from models.filters import Filters


class AnalysisFactory:

    def __init__(self, analysis_type: AnalysisType) -> None:
        super().__init__()
        self.analysis_type = analysis_type

    def get_analyse(self, filters: Filters) -> AnalysisBase:
        if self.analysis_type == AnalysisType.BASIC:
            return AnalysisBasic(filters)
        elif self.analysis_type == AnalysisType.FULL:
            return AnalysisFull(filters)
        elif self.analysis_type == AnalysisType.CONTACT:
            return AnalysisContact(filters)
        elif self.analysis_type == AnalysisType.SECURITY:
            return AnalysisSecurity()
        else:
            return None
