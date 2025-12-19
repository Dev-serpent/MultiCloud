from dataclasses import dataclass, field
from typing import List


@dataclass
class CloudAccount:
    name: str
    provider: str
    credentials: dict


@dataclass
class User:
    username: str
    password_hash: str
    cloud_accounts: List[CloudAccount] = field(default_factory=list)
