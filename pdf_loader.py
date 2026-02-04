import os
from pypdf import PdfReader

def _ocr_page_texts(pdf_path: str):
    try:
        from pdf2image import convert_from_path
        import pytesseract
    except Exception:
        return []

    try:
        images = convert_from_path(pdf_path, dpi=200)
    except Exception:
        return []

    ocr_texts = []
    for img in images:
        try:
            ocr_texts.append(pytesseract.image_to_string(img).strip().lower())
        except Exception:
            continue
    return ocr_texts

def _ocr_pdf(pdf_path: str) -> str:
    ocr_texts = _ocr_page_texts(pdf_path)
    return "\n".join(t for t in ocr_texts if t).strip()

def extract_text(pdf_path: str) -> str:
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            if page_text:
                text += page_text.lower()

    if not text.strip():
        text = _ocr_pdf(pdf_path)

    return text

def extract_snippets(pdf_path: str) -> str:
    page_texts = []
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        for page in reader.pages:
            page_text = page.extract_text() or ""
            page_texts.append(page_text.strip().lower())

    non_empty = [t for t in page_texts if t]
    if not non_empty:
        non_empty = [t for t in _ocr_page_texts(pdf_path) if t]
        if not non_empty:
            return ""

    first = non_empty[0]
    middle = non_empty[len(non_empty) // 2]
    last = non_empty[-1]

    snippets = [
        "START:\n" + first[:1200],
        "MIDDLE:\n" + middle[:1200],
        "END:\n" + last[:1200],
    ]
    result = "\n\n".join(snippets)

    if os.getenv("DEBUG_SNIPPETS") == "1":
        print("----- SNIPPETS PREVIEW -----")
        print(result[:1200])
        print("----- SNIPPETS PREVIEW END -----")

    return result
