from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str) -> str:
    """
    Hashes a password using Argon2.
    """
    return ph.hash(password)


def verify_password(password_hash: str, password: str) -> bool:
    """
    Verifies a password against a hash.
    """
    try:
        ph.verify(password_hash, password)
        return True
    except VerifyMismatchError:
        return False
