from agents.informations.site.informer_whois import InformerWhoIs
from agents.validators.site.validator_https import ValidatorHttps
from agents.validators.site.validator_ssl import ValidatorSSL
from analysis.analysis_base import AnalysisBase


class AnalysisSecurity(AnalysisBase):

    def __init__(self) -> None:
        extractorsHtml = []
        validatorsSite = [
            ValidatorSSL(),
            ValidatorHttps()
        ]
        informersSite = [
            InformerWhoIs()
        ]
        super().__init__(extractorsHtml, validatorsSite, informersSite)
