import streamlit as st
from parser import load_resume
from matcher import compute_similarity
from skills import extract_skills, compare_skills, get_suggestions

# ── Page Config ─────────────────────────────────────────────
st.set_page_config(page_title="Semantic Resume Matcher", layout="centered")

# ── Header ─────────────────────────────────────────────────
st.title("Semantic Resume Matcher")
st.write("Compare your resume with a job description using NLP")

# ── Inputs ─────────────────────────────────────────────────
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_desc = st.text_area("Paste Job Description")

# ── Analyze Button ─────────────────────────────────────────
if st.button("Analyze"):

    if resume_file is None or job_desc.strip() == "":
        st.warning("Please upload resume and enter job description")
    else:
        # Save file
        with open("temp.pdf", "wb") as f:
            f.write(resume_file.read())

        # Spinner (feels professional, unlike your debugging phase)
        with st.spinner("Analyzing resume..."):

            # Load + compute
            resume_text = load_resume("temp.pdf")
            score = compute_similarity(resume_text, job_desc)

            resume_skills = extract_skills(resume_text)
            jd_skills = extract_skills(job_desc)

            result = compare_skills(resume_skills, jd_skills)

            matched = result["matched"]
            missing = result["missing"]
            extra = result["extra"]

            suggestions = get_suggestions(missing)

        # ── Results ─────────────────────────────────────────
        st.subheader("Results")

        # Clean score display
        score_percent = score * 100
        st.metric("Match Score", f"{score_percent:.2f}%")

        # Interpretation
        if score > 0.7:
            st.success("Strong Match")
        elif score > 0.4:
            st.warning("Moderate Match")
        else:
            st.error("Weak Match")

        st.divider()

        # ── Skills Section ─────────────────────────────────
        col1, col2, col3 = st.columns(3)

        # Matched
        with col1:
            st.markdown("### Matched Skills")
            if matched:
                for s in sorted(matched):
                    st.write(f"- {s.title()}")
            else:
                st.caption("None")

        # Missing
        with col2:
            st.markdown("### Missing Skills")
            if missing:
                for s in sorted(missing):
                    st.write(f"- {s.title()}")
            else:
                st.caption("None")

        # Extra
        with col3:
            st.markdown("### Extra Skills")
            if extra:
                for s in sorted(extra):
                    st.write(f"- {s.title()}")
            else:
                st.caption("None")

        st.divider()

        # ── Suggestions ─────────────────────────────────────
        st.subheader("Improvement Suggestions")

        if suggestions:
            for s in suggestions:
                st.write(f"- {s}")
        else:
            st.success("Your resume aligns well with the job description.")