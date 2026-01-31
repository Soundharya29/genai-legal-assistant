import pdfplumber
import docx

def extract_text(file_path):
    if file_path.endswith(".pdf"):
        return extract_pdf_text(file_path)
    elif file_path.endswith(".docx"):
        return extract_docx_text(file_path)
    elif file_path.endswith(".txt"):
        return extract_txt_text(file_path)
    else:
        return ""

def extract_pdf_text(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_docx_text(path):
    doc = docx.Document(path)
    return "\n".join(p.text for p in doc.paragraphs)

def extract_txt_text(path):
    with open(path, "r", encoding="utf-8", errors="ignore") as f:
        return f.read()
