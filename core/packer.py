import tarfile
from pathlib import Path


def pack_folder(folder: str, out_file: str):
    folder = Path(folder)
    with tarfile.open(out_file, "w:gz") as tar:
        tar.add(folder, arcname=folder.name)


def unpack_folder(archive: str, out_dir: str):
    with tarfile.open(archive, "r:gz") as tar:
        tar.extractall(out_dir)
