import spacy
from spacy.matcher import PhraseMatcher

# Load spaCy model (already installed via requirements.txt)
nlp = spacy.load("en_core_web_sm")

# Define skill list
SKILL_LIST = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "nlp",
    "pandas",
    "numpy",
    "tensorflow",
    "pytorch",
    "data analysis",
    "data visualization",
    "excel",
    "power bi",
    "tableau"
]

# Create matcher
matcher = PhraseMatcher(nlp.vocab, attr="LOWER")

patterns = [nlp.make_doc(skill) for skill in SKILL_LIST]
matcher.add("SKILLS", patterns)


# 🔹 Extract skills from text
def extract_skills(text):
    doc = nlp(text)
    matches = matcher(doc)

    skills = set()
    for _, start, end in matches:
        skills.add(doc[start:end].text.lower())

    return skills


# 🔹 Compare resume vs job skills
def compare_skills(resume_skills, jd_skills):
    matched = resume_skills.intersection(jd_skills)
    missing = jd_skills.difference(resume_skills)
    extra = resume_skills.difference(jd_skills)

    return {
        "matched": matched,
        "missing": missing,
        "extra": extra
    }



def get_suggestions(missing_skills):
    suggestions = []

    for skill in missing_skills:
        suggestions.append(f"Consider learning or adding **{skill}** to your resume.")

    return suggestions