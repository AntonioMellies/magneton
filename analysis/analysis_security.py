from analysis.analysis_base import AnalysisBase
from validators.site.validator_https import ValidatorHttps
from validators.site.validator_ssl import ValidatorSSL


class AnalysisSecurity(AnalysisBase):

    def __init__(self) -> None:
        extractorsHtml = []
        validatorsSite = [
            ValidatorSSL(),
            ValidatorHttps()
        ]
        super().__init__(extractorsHtml, validatorsSite)
