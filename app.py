<<<<<<< HEAD
import streamlit as st
from parser import load_resume
from matcher import compute_similarity
from skills import extract_skills, compare_skills

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("Resume Analyzer")
st.write("Compare your resume with a job description using NLP")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if resume_file is None or job_desc.strip() == "":
        st.warning("Please upload resume and enter job description")
    else:
        with open("temp.pdf", "wb") as f:
            f.write(resume_file.read())

        resume_text = load_resume("temp.pdf")

        score = compute_similarity(resume_text, job_desc)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_desc)

        matched, missing = compare_skills(resume_skills, jd_skills)

        st.subheader("Results")

        st.write(f"Match Score: {round(score*100,2)}%")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Matched Skills")
            for s in matched:
                st.write("-", s)

        with col2:
            st.write("Missing Skills")
            for s in missing:
                st.write("-", s)
=======
import streamlit as st
from parser import load_resume
from matcher import compute_similarity
from skills import extract_skills, compare_skills

st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("Resume Analyzer")
st.write("Compare your resume with a job description using NLP")

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

if st.button("Analyze"):

    if resume_file is None or job_desc.strip() == "":
        st.warning("Please upload resume and enter job description")
    else:
        with open("temp.pdf", "wb") as f:
            f.write(resume_file.read())

        resume_text = load_resume("temp.pdf")

        score = compute_similarity(resume_text, job_desc)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_desc)

        matched, missing = compare_skills(resume_skills, jd_skills)

        st.subheader("Results")

        st.write(f"Match Score: {round(score*100,2)}%")

        col1, col2 = st.columns(2)

        with col1:
            st.write("Matched Skills")
            for s in matched:
                st.write("-", s)

        with col2:
            st.write("Missing Skills")
            for s in missing:
                st.write("-", s)
>>>>>>> 02572dc4207c60c45eac41d52f36227373f10187
