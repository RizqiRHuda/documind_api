from pydantic import BaseModel

class EmbeddingRequest(BaseModel):
    file_name: str
