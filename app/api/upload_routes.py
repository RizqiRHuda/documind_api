from fastapi import APIRouter, UploadFile, File, HTTPException
from app.services.file_service import save_pdf_file

router = APIRouter(tags=["Upload"])

@router.post("/upload/pdf")
async def upload_pdf(file: UploadFile = File(...)):
    try:
        result = await save_pdf_file(file)
        return {
            "status" : "success",
            "data" : result
        }
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception:
        raise HTTPException(status_code=500, detail="Upload failde")