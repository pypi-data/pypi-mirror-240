from typing import Any
from pydantic import BaseModel


class ErrorData(BaseModel):
    error_code: int
    error_text: str


class Response(BaseModel):
    error: bool = False
    response: Any | ErrorData
