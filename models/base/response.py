from pydantic import BaseModel


class Response(BaseModel):
    def __init__(self) -> None:
        super().__init__()
