import os
import re
import shutil
from config import OUTPUT_DIR

_INVALID_WIN_CHARS = r'<>:"/\\|?*'

def _sanitize_name(name: str, fallback: str) -> str:
    if not name:
        return fallback
    cleaned = re.sub(rf"[{re.escape(_INVALID_WIN_CHARS)}]", "", name)
    cleaned = cleaned.replace("**", "").strip()
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or fallback

def save_pdf(pdf_path: str, subject: str, topic: str):
    if not os.path.exists(pdf_path):
        return
    safe_subject = _sanitize_name(subject, "Unsorted")
    safe_topic = _sanitize_name(topic, "Manual Review")

    os.makedirs(os.path.join(OUTPUT_DIR, safe_subject), exist_ok=True)

    filename = os.path.basename(pdf_path)
    safe_topic = safe_topic.replace(" ", "_")

    new_name = f"{safe_topic}_{filename}"

    shutil.move(
        pdf_path,
        os.path.join(OUTPUT_DIR, safe_subject, new_name)
    )
