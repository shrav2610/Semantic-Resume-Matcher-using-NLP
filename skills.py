import spacy
from spacy.matcher import PhraseMatcher

# Safe loading for Streamlit Cloud
try:
    nlp = spacy.load("en_core_web_sm")
except:
    from spacy.cli import download
    download("en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

SKILL_LIST = [
    "Python", "SQL", "Machine Learning", "Deep Learning",
    "Pandas", "NumPy", "NLP", "TensorFlow", "PyTorch",
    "Data Analysis", "Data Visualization"
]

matcher = PhraseMatcher(nlp.vocab, attr="LOWER")
patterns = [nlp.make_doc(skill.lower()) for skill in SKILL_LIST]
matcher.add("SKILLS", patterns)

def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)

    skills = set()
    for _, start, end in matches:
        skills.add(doc[start:end].text.title())

    return skills

def compare_skills(resume_skills, jd_skills):
    matched = resume_skills & jd_skills
    missing = jd_skills - resume_skills
    return matched, missing