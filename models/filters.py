from pydantic import BaseModel


class Filters(BaseModel):
    cnpj: str = ""
    email: str = ""
    phone: str = ""
