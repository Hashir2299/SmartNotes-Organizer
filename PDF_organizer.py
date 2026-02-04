import os
from workflow import app

PDF_DIR = "C:/StudyTest/Unorganized"

for pdf in os.listdir(PDF_DIR):
    if pdf.lower().endswith(".pdf"):
        app.invoke({
            "pdf_path": os.path.join(PDF_DIR, pdf),
            "text": "",
            "subject": "",
            "topic": ""
        })
    print(f"File Organized Successfully: {pdf}")

print("✅ All PDFs organized successfully")