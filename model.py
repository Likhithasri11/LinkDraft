# model.py
from sentence_transformers import SentenceTransformer, util

# Load BERT model
model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight and fast

def calculate_similarity(resume_text, job_desc):
    embeddings = model.encode([resume_text, job_desc], convert_to_tensor=True)
    similarity_score = util.cos_sim(embeddings[0], embeddings[1]).item()
    return round(similarity_score * 100, 2)  # return as percentage

