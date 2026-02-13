from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool
from pydantic import BaseModel
from app.services.pdf_service import process_pdf

router = APIRouter()


class ExtractRequest(BaseModel):
    file_path: str


@router.post("/extract-pdf")
async def extract_pdf(request: ExtractRequest):
    try:
        result = await run_in_threadpool(process_pdf, request.file_path)
        return {"status": "success", "data": result}

    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except PermissionError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
