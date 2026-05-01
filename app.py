import streamlit as st
from parser import load_resume
from matcher import compute_similarity
from skills import extract_skills, compare_skills

# Page config
st.set_page_config(page_title="Resume Analyzer", layout="centered")

st.title("Semantic Resume Matcher")
st.write("Compare your resume with a job description using NLP")

# Inputs
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

# Button
if st.button("Analyze"):

    if resume_file is None or job_desc.strip() == "":
        st.warning("Please upload resume and enter job description")
    else:
        # Save uploaded file temporarily
        with open("temp.pdf", "wb") as f:
            f.write(resume_file.read())

        # Process
        resume_text = load_resume("temp.pdf")

        score = compute_similarity(resume_text, job_desc)

        resume_skills = extract_skills(resume_text)
        jd_skills = extract_skills(job_desc)

        # FIXED PART (dictionary handling)
        result = compare_skills(resume_skills, jd_skills)

        matched = result["matched"]
        missing = result["missing"]
        extra = result["extra"]

        # Output
        st.subheader("Results")

        st.write(f"Match Score: {round(score * 100, 2)}%")

        col1, col2, col3 = st.columns(3)

        # Matched
        with col1:
            st.write("Matched Skills")
            if matched:
                for s in sorted(matched):
                    st.write(f"- {s}")
            else:
                st.write("None")

        # Missing
        with col2:
            st.write("Missing Skills")
            if missing:
                for s in sorted(missing):
                    st.write(f"- {s}")
            else:
                st.write("None")

        # Extra
        with col3:
            st.write("Extra Skills")
            if extra:
                for s in sorted(extra):
                    st.write(f"- {s}")
            else:
                st.write("None")