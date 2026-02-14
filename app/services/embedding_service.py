import json
from pathlib import Path

from app.utils.embedding_model import get_embedding

CHUNK_DIR = Path("storage/chunks").resolve()
EMBED_DIR = Path("storage/embeddings").resolve()

def process_embedding(file_name: str):

    chunk_file = CHUNK_DIR / f"{file_name}_chunks.json"

    if not chunk_file.exists():
        raise FileNotFoundError("Chunk file not found")

    with open(chunk_file, "r", encoding="utf-8") as f:
        chunks = json.load(f)

    embedded_data = []

    for chunk in chunks:
        vector = get_embedding(chunk["text"])

        embedded_data.append({
            "chunk_id": chunk["chunk_id"],
            "text": chunk["text"],
            "embedding": vector
        })

    EMBED_DIR.mkdir(parents=True, exist_ok=True)

    embed_file = EMBED_DIR / f"{file_name}_embeddings.json"

    with open(embed_file, "w", encoding="utf-8") as f:
        json.dump(embedded_data, f, ensure_ascii=False, indent=2)

    return {
        "file_name": file_name,
        "total_chunks": len(embedded_data),
        "embedding_file": str(embed_file),
        "embedding_dimension": len(embedded_data[0]["embedding"])
    }
