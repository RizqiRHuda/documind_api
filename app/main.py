from fastapi import FastAPI
from app.api.upload_routes import router as upload_router

app = FastAPI(title="DocuMind API")

app.include_router(upload_router, prefix="/api")

@app.get("/")
def root():
    return {"message": "DocuMind API running"}
