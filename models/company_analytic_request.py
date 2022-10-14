from typing import Union

from pydantic import BaseModel

from models.enums.analysis_type_enum import AnalysisType
from models.filters import Filters


class CompanyAnalyticRequest(BaseModel):
    url: str
    depth: Union[int, None] = None
    type: AnalysisType = AnalysisType.BASIC
    filters: Filters
