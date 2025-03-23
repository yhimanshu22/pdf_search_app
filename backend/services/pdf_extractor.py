
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    documents = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                documents.append(text)
    return documents
