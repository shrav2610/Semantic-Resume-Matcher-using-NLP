# Semantic Resume Matcher (NLP)

Live Demo: https://semantic-resume-matcher-using-nlp-8fksnsakva3kiwv65tn8x9.streamlit.app/

---

## Overview

This project analyzes how well a resume matches a job description using Natural Language Processing (NLP).

It combines **semantic similarity (Sentence-BERT)** with **skill-based matching** to provide an interpretable match score and actionable feedback.

---

## Features

* Resume parsing from PDF
* Semantic similarity using transformer embeddings (SBERT)
* Skill extraction using spaCy
* Skill gap analysis (matched, missing, extra skills)
* Improvement suggestions
* Interactive Streamlit web app
* Evaluation with dataset, accuracy, and confusion matrix

---

## Tech Stack

* Python
* Sentence Transformers (SBERT)
* spaCy
* Scikit-learn
* Streamlit

---

## Methodology

1. Extract text from resume (PDF)
2. Generate embeddings using Sentence-BERT
3. Compute cosine similarity between resume and job description
4. Extract skills using spaCy
5. Compare skills to identify:

   * Matched skills
   * Missing skills
   * Extra skills
6. Generate improvement suggestions

---

## App Demo

### Input

![Input]("Results\Input.png")

### Results

![Score](Results\score.png)

### Skill Analysis

![Skills](Results\skills.png)

### Suggestions

![Suggestions](Results\suggestions.png)

---

## Evaluation

A labeled dataset was created to evaluate model performance.

* Accuracy: XX%
* Confusion Matrix included in notebook

See: `notebooks/evaluation.ipynb`

---

## Example Output

* Match Score: 68%
* Missing Skills: Deep Learning, NLP
* Suggestions provided for improvement

---

## Project Structure

```
├── app.py
├── main.py
├── matcher.py
├── parser.py
├── skills.py
├── requirements.txt
├── notebooks/
│   └── evaluation.ipynb
├── results/
└── README.md
```

---

## CLI Usage

You can also run the project from command line:

```
python main.py
```

---

## Future Improvements

* Improve skill extraction using NER models
* Expand evaluation dataset
* Improve scoring calibration
* Add support for multiple resumes

---

## Author

Shravani
