from fastapi import APIRouter, HTTPException
from fastapi.concurrency import run_in_threadpool

from app.services.embedding_service import process_embedding
from app.schemas.embedding_schema import EmbeddingRequest

router = APIRouter(tags=["Embedding"])

@router.post("/embed")
async def embed_file(request: EmbeddingRequest):

    try:
        result = await run_in_threadpool(
            process_embedding,
            request.file_name
        )

        return {
            "status": "success",
            "data": result
        }

    except FileNotFoundError as e:
        raise HTTPException(status_code=404, detail=str(e))

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
