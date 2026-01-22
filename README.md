# 📄 Smart Resume Analyzer

A web-based application that evaluates how well a resume matches a given job description by simulating an Applicant Tracking System (ATS) keyword screening process.

🔗 **Live Demo:** https://YOUR-RENDER-LINK.onrender.com

---

## 🚀 Features

- Upload resumes in PDF format
- Paste any job description
- Calculates ATS-style compatibility score
- Identifies matched and missing keywords
- Clean and responsive UI
- Deployed as a live web application

---

## 🧠 How It Works

1. Extracts text from uploaded PDF resumes
2. Tokenizes and filters keywords from both resume and job description
3. Compares keyword overlap to simulate ATS screening
4. Computes a match percentage score
5. Highlights missing keywords to help optimize resumes

This mirrors how many automated resume screening systems work in practice.

---

## 🛠 Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **PDF Parsing:** PyPDF2
- **NLP Techniques:** Keyword extraction & matching
- **Deployment:** Render
- **Server:** Gunicorn

---

## 📦 Run Locally
bash
git clone https://github.com/jiya18patel/smart-resume-analyzer.git
cd smart-resume-analyzer
pip install -r requirements.txt
python app.py
