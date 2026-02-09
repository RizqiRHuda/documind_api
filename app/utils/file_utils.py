import os
from fastapi import UploadFile

from app.core.config import settings

def validate_pdf_file(file: UploadFile):
    
    ext = os.path.splitext(file.filename)[1].lower()
    
    if ext not in settings.ALLOWED_EXTENSIONS:
        raise ValueError("Only PDF files are allowed")
    
    if file.content_type and "pdf" not in file.content_type:
        raise ValueError("Invalid PDF content type")
