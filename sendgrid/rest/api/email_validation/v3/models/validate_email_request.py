from typing import Optional, Dict
from sendgrid.converters.serialize import to_serializable, from_serializable


class ValidateEmailRequest:
    def __init__(self, email: Optional[str] = None, source: Optional[str] = None):
        self.email = email
        self.source = source

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"email": self.email, "source": self.source}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return ValidateEmailRequest(
            email=payload.get("email"), source=payload.get("source")
        )
