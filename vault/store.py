import json
from pathlib import Path

from core.crypto import encrypt, decrypt
from core.config import config

VAULT_FILE = Path(config.get("vault", "path", fallback="vault.sec"))


def save_vault(data: dict, password: str):
    raw = json.dumps(data).encode()
    encrypted = encrypt(raw, password)
    VAULT_FILE.write_bytes(encrypted)


def load_vault(password: str) -> dict:
    if not VAULT_FILE.exists():
        return {}

    raw = decrypt(VAULT_FILE.read_bytes(), password)
    return json.loads(raw.decode())
