from pathlib import Path
import json

CHUNK_DIR = Path("storage/chunks").resolve()
CHUNK_DIR.mkdir(parents=True, exist_ok=True)

def save_chunks(file_stem: str, chunks: list[str]) -> str:
    file_path = CHUNK_DIR / f"{file_stem}_chunks.json"

    data = []

    for i, chunk in enumerate(chunks):
        data.append({
            "chunk_id": i,
            "text": chunk
        })

    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return str(file_path)