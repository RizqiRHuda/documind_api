import os
from datetime import datetime
from fastapi import UploadFile

from app.core.config import settings
from app.utils.file_utils import validate_pdf_file

async def save_pdf_file(file: UploadFile):
    
    validate_pdf_file(file)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{timestamp}_{file.filename}"
    
    save_path = os.path.join(settings.PDF_STORAGE_PATH, filename)
    
    with open(save_path, "wb") as buffer:
        content = await file.read()
        buffer.write(content)
    
    return {
        "filename" : filename,
        "path" : save_path,
        "size" : len(content)
    }