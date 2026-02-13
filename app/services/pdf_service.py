from pathlib import Path
from app.utils.pdf_utils import extract_text_from_pdf
from app.services.text_service import save_text
from app.services.chunk_service import chunk_text
from app.services.chunk_storage_service import save_chunks

BASE_DIR = Path("storage/pdf").resolve()


def process_pdf(file_path: str) -> dict:
    pdf_path = (BASE_DIR / Path(file_path)).resolve()

    if not str(pdf_path).startswith(str(BASE_DIR)):
        raise PermissionError("Invalid file path")

    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF not found: {pdf_path.name}")

    # Extract text
    text = extract_text_from_pdf(pdf_path)

    # Save text
    text_file = save_text(pdf_path.stem, text)
    
    chunks = chunk_text(text)
    chunk_file = save_chunks(pdf_path.stem, chunks)


    return {
        "file_name": pdf_path.name,
        "text_file": text_file,
        "total_characters": len(text),
        "total_chunks" : len(chunks),
        "chunk_file" : chunk_file,
        "preview": text[:500]
    }
