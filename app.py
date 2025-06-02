# app.py
from flask import Flask, render_template, request
from model import calculate_similarity

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/match', methods=['POST'])
def match():
    resume_text = request.form['resume']
    job_desc = request.form['job']
    
    if not resume_text or not job_desc:
        return "Please provide both resume and job description."

    match_percentage = calculate_similarity(resume_text, job_desc)
    return render_template('result.html', match_score=match_percentage)

if __name__ == '__main__':
    app.run(debug=True)
