from pathlib import Path

TEXT_DIR = Path("storage/text").resolve()
TEXT_DIR.mkdir(parents=True, exist_ok=True)


def save_text(file_name: str, text: str) -> str:
    text_path = TEXT_DIR / f"{file_name}.txt"

    with open(text_path, "w", encoding="utf-8") as f:
        f.write(text)

    return str(text_path)
