import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    
    PDF_STORAGE_PATH = os.path.join(BASE_DIR, "storage", "pdf")
    
    MAX_FILE_SIZE_MB = 10
    
    ALLOWED_EXTENSIONS = [".pdf"]
    
settings = Settings()