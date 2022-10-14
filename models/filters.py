from pydantic import BaseModel


class Filters(BaseModel):
    cnpj: str = ""
    email: str = ""
    ssl: bool = False
    https: bool = False
