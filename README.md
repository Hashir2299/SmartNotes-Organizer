# SmartNotes Organizer

Organize study PDFs by extracting text/OCR, classifying with an LLM, and moving files into subject folders.

## Features
- PDF text extraction with `pypdf`
- OCR fallback for scanned/handwritten PDFs
- LLM-based subject/topic classification (Ollama)
- Used Langgraph for better results
- Safe file naming and organized output structure

## Important Tips for Using Tool
- Just Change the name of the subjects from the config file
- Simply enter there what you want to organize, do other minimal changes in LLM's prompt and the **SmartNotes-Organzier** will do the rest
- You can organize Subjects, Projects, Documents, etc through these tools
- I have used Ollama in this project which is an open-source model. Use ChatOpenai model if you want more precision and speed

## Setup
```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
```

## OCR (Windows)
Install Tesseract OCR and ensure `tesseract` is on PATH.
If you didn't do this then the LLM will not be able to extract hand written pdf

## Run
```powershell
$env:OLLAMA_MODEL='llama3.1:latest'
.\venv\Scripts\python .\PDF_organizer.py
```

## Notes
- Input folder path: `C:/StudyTest/Unorganized`
- Output folder path: `C:/StudyTest/Organized`
