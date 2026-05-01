from parser import load_resume, load_job_description
from matcher import compute_similarity
from skills import extract_skills, compare_skills

resume = load_resume("data/resume.pdf")
jd = load_job_description("data/job.txt")

score = compute_similarity(resume, jd)

resume_skills = extract_skills(resume)
jd_skills = extract_skills(jd)

matched, missing = compare_skills(resume_skills, jd_skills)

print("\n===== RESULT =====")
print("Match Score:", round(score * 100, 2), "%")

print("\nMatched Skills:")
for s in matched:
    print("-", s)

print("\nMissing Skills:")
for s in missing:
    print("-", s)