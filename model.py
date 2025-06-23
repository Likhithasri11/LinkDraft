# model.py - Lightweight version
import re
from collections import Counter
import math

def preprocess_text(text):
    """Clean and normalize text"""
    # Convert to lowercase and remove special characters
    text = re.sub(r'[^a-zA-Z0-9\s]', '', text.lower())
    # Split into words
    words = text.split()
    # Remove common stop words
    stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with', 'by', 'is', 'are', 'was', 'were', 'be', 'been', 'have', 'has', 'had', 'do', 'does', 'did', 'will', 'would', 'could', 'should'}
    words = [word for word in words if word not in stop_words and len(word) > 2]
    return words

def calculate_cosine_similarity(text1, text2):
    """Calculate cosine similarity between two texts"""
    words1 = preprocess_text(text1)
    words2 = preprocess_text(text2)
    
    # Create word frequency vectors
    all_words = set(words1 + words2)
    
    vec1 = [words1.count(word) for word in all_words]
    vec2 = [words2.count(word) for word in all_words]
    
    # Cosine similarity formula
    dot_product = sum(a * b for a, b in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(a * a for a in vec1))
    magnitude2 = math.sqrt(sum(a * a for a in vec2))
    
    if magnitude1 == 0 or magnitude2 == 0:
        return 0
    
    return dot_product / (magnitude1 * magnitude2)

def calculate_similarity(resume_text, job_desc):
    """Main function to calculate resume-job similarity"""
    # Basic cosine similarity
    base_score = calculate_cosine_similarity(resume_text, job_desc)
    
    # Bonus scoring for key matches
    resume_lower = resume_text.lower()
    job_lower = job_desc.lower()
    
    # Extract key terms from job description
    tech_keywords = ['python', 'java', 'javascript', 'react', 'nodejs', 'sql', 'aws', 'docker', 'git', 'machine learning', 'data science', 'flask', 'django']
    skill_matches = sum(1 for keyword in tech_keywords if keyword in resume_lower and keyword in job_lower)
    
    # Calculate final score (0-100%)
    final_score = (base_score * 70) + (skill_matches * 5)  # Weight base similarity 70%, skill matches 30%
    final_score = min(final_score * 100, 100)  # Convert to percentage, cap at 100%
    
    return round(final_score, 2)

