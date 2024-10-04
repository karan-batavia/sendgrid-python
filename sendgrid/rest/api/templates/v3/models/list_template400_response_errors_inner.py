from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ListTemplate400ResponseErrorsInner:
    def __init__(self, message: Optional[str] = None, error_id: Optional[str] = None):
        self.message = message
        self.error_id = error_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {
                "message": self.message,
                "error_id": self.error_id,
            }.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ListTemplate400ResponseErrorsInner(
            message=payload.get("message"), error_id=payload.get("error_id")
        )
