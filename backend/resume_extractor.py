import PyPDF2
import re

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        text = " ".join([page.extract_text() for page in reader.pages if page.extract_text()])
    return text

def extract_info(text):
    name_match = re.search(r"([A-Z][a-z]+ [A-Z][a-z]+)", text)
    email_match = re.search(r"[\w\.-]+@[\w\.-]+", text)
    phone_match = re.search(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}", text)

    return {
        "name": name_match.group(0) if name_match else "Unknown",
        "email": email_match.group(0) if email_match else "Not Found",
        "phone": phone_match.group(0) if phone_match else "Not Found",
    }
