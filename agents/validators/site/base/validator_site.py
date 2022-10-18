from abc import ABC

from agents.validators.validator import Validator


class ValidatorSite(Validator, ABC):
    url: str = None

    def set_url(self, url):
        self.url = url
