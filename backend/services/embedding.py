import faiss
import numpy as np
from langchain.text_splitter import RecursiveCharacterTextSplitter
from sentence_transformers import SentenceTransformer
from config import SIMILARITY_METRIC

# Load SentenceTransformer Model
hf_model = SentenceTransformer("all-MiniLM-L6-v2")

def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    """Splits text into chunks for efficient embedding."""
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    return text_splitter.create_documents(docs)

def create_faiss_index(doc_chunks):
    """Creates FAISS index with specified similarity metric."""
    global index
    vector_embeddings = hf_model.encode([doc.page_content for doc in doc_chunks], convert_to_numpy=True)
    dimension = vector_embeddings.shape[1]

    if SIMILARITY_METRIC == "cosine":
        faiss.normalize_L2(vector_embeddings)
        index = faiss.IndexFlatIP(dimension)
    elif SIMILARITY_METRIC == "dotproduct":
        index = faiss.IndexFlatIP(dimension)
    elif SIMILARITY_METRIC == "euclidean":
        index = faiss.IndexFlatL2(dimension)
    else:
        raise ValueError("Invalid similarity metric. Choose 'cosine', 'dotproduct', or 'euclidean'.")

    index.add(vector_embeddings)
    return index, doc_chunks
