### **README.md**  

```md
# AI-Powered PDF Search API  

## **Overview**  
This project allows users to upload a PDF file and perform semantic searches to find similar content within the document. It uses **FAISS (Facebook AI Similarity Search)** for efficient similarity matching and **Hugging Face's sentence-transformers** for text embeddings.

## **Approach**  
1. **Extract Text from PDF** → Using `pdfminer`, the text is extracted from the uploaded PDF.  
2. **Chunking the Text** → The text is divided into smaller, meaningful chunks for better search accuracy.  
3. **Create Embeddings** → The chunks are converted into numerical vectors using **Hugging Face transformers**.  
4. **Build FAISS Index** → The embeddings are indexed using FAISS for efficient similarity search.  
5. **Query Search** → When a user searches for a query, its embedding is computed and compared against the FAISS index to retrieve the most relevant chunks.  

---

## **How to Run the Project Locally**  

### **1. Clone the Repository**  
```sh
git clone https://github.com/your-repo/pdf-search-api.git
cd pdf-search-api
```

### **2. Set Up a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
venv\Scripts\activate      # For Windows
```

### **3. Install Dependencies**  
```sh
pip install -r requirements.txt
```

### **4. Run the FastAPI Server**  
```sh
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```

The API will now be accessible at **http://127.0.0.1:8000**  

---

## **API Endpoints & Examples**  

### **1. Upload PDF File**
#### **Endpoint:**  
```http
POST /api/upload_pdf
```
#### **Request Example (Form-Data)**
```sh
curl -X POST "http://127.0.0.1:8000/api/upload_pdf" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@budget_speech.pdf"
```

#### **Response Example**
```json
{
  "message": "PDF uploaded and indexed successfully.",
  "num_chunks": 150
}
```

---

### **2. Search for Similar Content**
#### **Endpoint:**  
```http
GET /api/search?query="budget deficit" &top_k=5
```
#### **Response Example**
```json
{
  "query": "budget deficit",
  "results": [
    {
      "chunk": "The government plans to reduce the budget deficit through increased taxation...",
      "score": 0.85
    },
    {
      "chunk": "A significant reduction in fiscal deficit is projected over the next 5 years...",
      "score": 0.78
    }
  ]
}
```

---

## **Tech Stack**
- **FastAPI** - Backend API Framework  
- **FAISS** - Efficient Similarity Search  
- **Hugging Face Transformers** - Text Embeddings  
- **pdfminer.six** - Extract text from PDFs  
- **Uvicorn** - ASGI Server  

---

---

---
⭐ **If you find this project useful, give it a star!** 🚀  
```

---

