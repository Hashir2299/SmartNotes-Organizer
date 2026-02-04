# SmartNotes Organizer

Organize study PDFs by extracting text/OCR, classifying with an LLM, and moving files into subject folders.

## Features
- PDF text extraction with `pypdf`
- OCR fallback for scanned/handwritten PDFs
- LLM-based subject/topic classification (Ollama)
- Safe file naming and organized output structure

## Important Tips for Using Tool
- Just Change the name of the subjects from the config file
- Simply enter there what you want to organize and the SmartNotes-Organzier will do it for you
- You can organize Subjects, Projects, Documents, etc through these tools

## Setup
```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
```

## OCR (Windows)
Install Tesseract OCR and ensure `tesseract` is on PATH.

## Run
```powershell
$env:OLLAMA_MODEL='llama3.1:latest'
.\venv\Scripts\python .\PDF_organizer.py
```

## Notes
- Input folder: `C:/StudyTest/Unorganized`
- Output folder: `C:/StudyTest/Organized`
