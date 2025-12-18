import os
import hashlib
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from argon2.low_level import hash_secret_raw, Type

KEY_LEN = 32
SALT_LEN = 16
NONCE_LEN = 12


def derive_key(password: str, salt: bytes) -> bytes:
    return hash_secret_raw(
        secret=password.encode(),
        salt=salt,
        time_cost=3,
        memory_cost=65536,
        parallelism=2,
        hash_len=KEY_LEN,
        type=Type.ID,
    )


def encrypt(data: bytes, password: str) -> bytes:
    salt = os.urandom(SALT_LEN)
    nonce = os.urandom(NONCE_LEN)
    key = derive_key(password, salt)

    aes = AESGCM(key)
    ciphertext = aes.encrypt(nonce, data, None)

    return salt + nonce + ciphertext


def decrypt(blob: bytes, password: str) -> bytes:
    salt = blob[:SALT_LEN]
    nonce = blob[SALT_LEN:SALT_LEN + NONCE_LEN]
    ciphertext = blob[SALT_LEN + NONCE_LEN:]

    key = derive_key(password, salt)
    aes = AESGCM(key)

    return aes.decrypt(nonce, ciphertext, None)
