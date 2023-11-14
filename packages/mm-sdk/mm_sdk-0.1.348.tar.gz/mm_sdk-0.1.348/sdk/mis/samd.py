from urllib.parse import urljoin

from pydantic import BaseModel, HttpUrl

from ..client import Empty, SDKClient, SDKResponse


class CallBackRequest(BaseModel):
    task_id: str
    data: str
    has_error: bool


class MisSamdService:
    def __init__(self, client: SDKClient, url: HttpUrl):
        self._client = client
        self._url = url

    def send_callback(self, query: CallBackRequest, timeout=3) -> SDKResponse[Empty]:
        return self._client.post(
            urljoin(str(self._url), "samd/tasks/callback/"),
            Empty,
            json=query.dict(exclude_none=True),
            timeout=timeout,
        )
