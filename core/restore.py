import tempfile
from pathlib import Path

from core.crypto import decrypt
from core.splitter import reassemble
from core.packer import unpack_folder


def restore_backup(chunks: list, password: str, output_dir: str):
    with tempfile.TemporaryDirectory() as tmp:
        enc_file = Path(tmp) / "data.enc"
        tar_file = Path(tmp) / "data.tar.gz"

        reassemble(chunks, enc_file)
        tar_file.write_bytes(decrypt(enc_file.read_bytes(), password))
        unpack_folder(tar_file, output_dir)

        print("Restore complete")
