import os
from fastapi import FastAPI
import llama_cpp
from pydantic import BaseModel
from contextlib import asynccontextmanager

model_name = os.environ.get('REPO_ID', 'nomic-ai/nomic-embed-text-v1.5-GGUF')
file_name = os.environ.get('FILE_NAME', 'nomic-embed-text-v1.5.Q4_K_M.gguf')

@asynccontextmanager
async def lifespan(app: FastAPI):

    app.state.model = llama_cpp.Llama.from_pretrained(repo_id=model_name, filename='nomic-embed-text-v1.5.Q4_K_M.gguf', n_gpu_layers=0, embedding=True)
    yield

app = FastAPI(lifespan=lifespan)

class EmbeddingsBody(BaseModel):
    text: list[str]

@app.post('/embeddings')
async def embeddings(body: EmbeddingsBody):
    embeddings = app.state.model.create_embedding(body.text)
    return { "embeddings": [e["embedding"] for e in embeddings["data"]] }

@app.get('/health')
async def health_check():
    embedding = app.state.model.create_embedding("Ping")
    return { "embedding": embedding["data"][0]["embedding"] }
