import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# PDF Path (Modify this as needed)
PDF_PATH = os.getenv("PDF_PATH", "budget_speech.pdf")

# FAISS Similarity Metric
SIMILARITY_METRIC = os.getenv("SIMILARITY_METRIC", "cosine")
