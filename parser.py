<<<<<<< HEAD
from pdfminer.high_level import extract_text

def load_resume(path):
    return extract_text(path)

def load_job_description(path):
    with open(path, "r", encoding="utf-8") as f:
=======
from pdfminer.high_level import extract_text

def load_resume(path):
    return extract_text(path)

def load_job_description(path):
    with open(path, "r", encoding="utf-8") as f:
>>>>>>> 02572dc4207c60c45eac41d52f36227373f10187
        return f.read()