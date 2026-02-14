from fastapi import FastAPI
from app.api.upload_routes import router as upload_router
from app.api.document_routes import router as extract_router
from app.api.embedding_routes import router as embedding_router

app = FastAPI(title="DocuMind API")

app.include_router(upload_router, prefix="/api")
app.include_router(extract_router, prefix="/api")
app.include_router(embedding_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "DocuMind API running"}
