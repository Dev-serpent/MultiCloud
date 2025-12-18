import hashlib


def verify_password(password: str, check: str) -> bool:
    return hashlib.sha256(password.encode()).hexdigest() == check


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()
