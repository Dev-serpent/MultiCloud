import tempfile
from pathlib import Path

from core.packer import pack_folder
from core.crypto import encrypt
from core.splitter import split_file
from core.verifier import sha256


def backup_folder(folder: str, password: str = "changeme"):
    with tempfile.TemporaryDirectory() as tmp:
        archive = Path(tmp) / "data.tar.gz"
        encrypted = Path(tmp) / "data.enc"

        pack_folder(folder, archive)
        encrypted.write_bytes(encrypt(archive.read_bytes(), password))

        chunks = split_file(encrypted)

        print("Backup complete")
        print("Chunks:")
        for c in chunks:
            print(" ", c)

        print("SHA256:", sha256(encrypted))
