from pathlib import Path


def split_file(path: str, chunk_size: int = 5 * 1024 * 1024):
    path = Path(path)
    chunks = []

    with path.open("rb") as f:
        index = 0
        while True:
            data = f.read(chunk_size)
            if not data:
                break
            chunk_path = path.with_suffix(f".part{index}")
            chunk_path.write_bytes(data)
            chunks.append(str(chunk_path))
            index += 1

    return chunks


def reassemble(chunks: list, output: str):
    with open(output, "wb") as out:
        for chunk in chunks:
            with open(chunk, "rb") as f:
                out.write(f.read())
