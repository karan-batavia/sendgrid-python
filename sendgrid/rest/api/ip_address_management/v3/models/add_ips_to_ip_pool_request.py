from typing import Optional, Dict, List
from sendgrid.converters.serialize import to_serializable, from_serializable


class AddIpsToIpPoolRequest:
    def __init__(self, ips: Optional[List[str]] = None):
        self.ips = ips

    def to_dict(self):
        return {
            key: to_serializable(value)
            for key, value in {"ips": self.ips}.items()
            if value is not None
        }

    @classmethod
    def from_dict(cls, data):
        return from_serializable(data, cls)

    @staticmethod
    def generate_model(payload: Dict[str, object]):
        return AddIpsToIpPoolRequest(ips=payload.get("ips"))
