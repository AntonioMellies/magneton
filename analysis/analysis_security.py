from analysis.analysis_base import AnalysisBase
from validators.site.validator_https import ValidatorHttps
from validators.site.validator_ssl import ValidatorSSL
from validators.site.validator_whois import ValidatorWhoIs


class AnalysisSecurity(AnalysisBase):

    def __init__(self) -> None:
        extractorsHtml = []
        validatorsSite = [
            ValidatorSSL(),
            ValidatorWhoIs(),
            ValidatorHttps()
        ]
        super().__init__(extractorsHtml, validatorsSite)
