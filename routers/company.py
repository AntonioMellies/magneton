from fastapi import APIRouter

from models.company_analytic_request import CompanyAnalyticRequest
from services.company_analysis_business import CompanyAnalysisBusiness

router = APIRouter(prefix="/company")

companyService = CompanyAnalysisBusiness()


@router.post("/analyze")
async def full(request: CompanyAnalyticRequest):
    return companyService.analyze(request)

