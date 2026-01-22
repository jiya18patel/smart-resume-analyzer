from flask import Flask, render_template, request
from PyPDF2 import PdfReader
import re
from collections import Counter

app = Flask(__name__)

def extract_text_from_pdf(file):
    reader = PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]{3,}\b', text.lower())
    return Counter(words)

@app.route("/", methods=["GET", "POST"])
def index():
    score = None
    missing_keywords = []
    matched_keywords = []

    if request.method == "POST":
        resume_file = request.files["resume"]
        job_description = request.form["job_description"].lower()

        resume_text = extract_text_from_pdf(resume_file)
        resume_keywords = extract_keywords(resume_text)
        job_keywords = extract_keywords(job_description)

        matches = set(resume_keywords) & set(job_keywords)
        missing = set(job_keywords) - set(resume_keywords)

        score = round((len(matches) / len(job_keywords)) * 100, 2) if job_keywords else 0
        matched_keywords = sorted(matches)
        missing_keywords = sorted(list(missing)[:15])

    return render_template(
        "index.html",
        score=score,
        matched_keywords=matched_keywords,
        missing_keywords=missing_keywords
    )

if __name__ == "__main__":
    app.run(debug=True)
