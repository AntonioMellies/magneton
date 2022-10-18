from typing import List

from agents.informations.inform_service import InformService
from agents.informations.site.base.informer_site import InformerSite
from agents.validators.site.base.validator_site import ValidatorSite
from models.base.response import Response
from utils.url_utils import valid_and_return_url


class InformServiceSite(InformService):

    def __init__(self, url: str, informants: List[InformerSite]) -> None:
        super().__init__()
        self.url = valid_and_return_url(url)
        self.informants = informants

    def inform(self, response: Response = Response()) -> Response:
        if len(self.informants) == 0:
            return response

        for informer in self.informants:
            informer.set_url(self.url)

        for x in range(1, len(self.informants)):
            self.informants[x - 1].set_next(self.informants[x])

        return self.informants[0].handle(response)
