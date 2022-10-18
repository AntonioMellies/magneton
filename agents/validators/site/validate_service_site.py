from typing import List

from models.base.response import Response
from utils.url_utils import valid_and_return_url
from agents.validators.site.base.validator_site import ValidatorSite
from agents.validators.validate_service import ValidateService


class ValidateServiceSite(ValidateService):

    def __init__(self, url: str, validators: List[ValidatorSite]) -> None:
        super().__init__()
        self.url = valid_and_return_url(url)
        self.validators = validators

    def validate(self, response: Response = Response()) -> Response:
        if len(self.validators) == 0:
            return response

        for validator in self.validators:
            validator.set_url(self.url)

        for x in range(1, len(self.validators)):
            self.validators[x - 1].set_next(self.validators[x])

        return self.validators[0].handle(response)
