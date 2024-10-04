from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable
from sendgrid.rest.api.email_activity.v3.models.status2 import Status2


class RequestCsv202Response:
    def __init__(self, status: Optional[Status2] = None, message: Optional[str] = None):
        self.status = status
        self.message = message

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"status": self.status, "message": self.message}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return RequestCsv202Response(
            status=payload.get("status"), message=payload.get("message")
        )
