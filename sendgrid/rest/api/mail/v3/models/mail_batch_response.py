from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class MailBatchResponse:
    def __init__(self, batch_id: Optional[str] = None):
        self.batch_id = batch_id

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"batch_id": self.batch_id}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return MailBatchResponse(batch_id=payload.get("batch_id"))
