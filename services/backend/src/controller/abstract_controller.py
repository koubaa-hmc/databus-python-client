from abc import ABC
from http import HTTPStatus
from fastapi import HTTPException
from typing import Any


class AbstractController(ABC):
    @staticmethod
    def response_ok(response: Any = None) -> Any:
        if isinstance(response, str) or response is None:
            return {"message": response}

        return response

    @staticmethod
    def response_failed(http_status_code: int, reason: str = None) -> Any:
        http_status = HTTPStatus(http_status_code)
        return HTTPException(status_code=http_status.value, detail=reason or http_status.phrase, )
