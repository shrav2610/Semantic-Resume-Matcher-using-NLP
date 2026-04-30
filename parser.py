from pdfminer.high_level import extract_text

def load_resume(path):
    return extract_text(path)

def load_job_description(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()