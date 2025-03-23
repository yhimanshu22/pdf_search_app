import uvicorn
import os
import shutil
import numpy as np
from fastapi import FastAPI, Query, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from services.pdf_extractor import extract_text_from_pdf
from services.embedding import chunk_data, create_faiss_index, hf_model
from models.search_model import SearchResponse, SearchResult

UPLOAD_DIR = "uploaded_pdfs"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

documents = []
document_chunks = []
index = None
processed_documents = []

@app.post("/api/upload_pdf")
async def upload_pdf(file: UploadFile = File(...)):
    file_path = os.path.join(UPLOAD_DIR, file.filename)
    
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    global documents, document_chunks, index, processed_documents
    documents = extract_text_from_pdf(file_path)
    document_chunks = chunk_data(documents)
    index, processed_documents = create_faiss_index(document_chunks)

    return {"message": "PDF uploaded and indexed successfully", "chunks": len(document_chunks)}

@app.get("/api/search", response_model=SearchResponse)
def search(query: str = Query(..., title="Search Query"), top_k: int = 5):
    if not processed_documents:
        return {"error": "No PDF uploaded yet"}
    
    query_embedding = hf_model.encode([query], convert_to_numpy=True).astype(np.float32)
    distances, indices = index.search(query_embedding, top_k)

    results = [
        SearchResult(chunk=processed_documents[i].page_content, score=float(distances[0][j]))
        for j, i in enumerate(indices[0])
    ]

    return SearchResponse(query=query, results=results)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
