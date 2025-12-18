from dataclasses import dataclass


@dataclass
class CloudAccount:
    name: str
    provider: str
    access_key: str
    secret_key: str
