import os
import requests

HF_TOKEN = os.getenv("HF_TOKEN")

API_URL = "https://router.huggingface.co/hf-inference/models/mistralai/Mistral-7B-Instruct-v0.2"

HEADERS = {
    "Authorization": f"Bearer {HF_TOKEN}",
    "Content-Type": "application/json"
}

def generate_answer(question, level, domain, length):
    length_map = {
        "Short (3-4 sentences)": "3-4 sentences",
        "Medium (5-6 sentences)": "5-6 sentences",
        "Long (7-8 sentences)": "7-8 sentences"
    }

    prompt = f"""
You are an AI interview coach.

Rules:
- Answer in first person ("I")
- Professional and interview-safe
- No company names, job titles, or exaggeration
- Limit answer to {length_map[length]}

Candidate level: {level}
Interview type: {domain}

Interview Question:
{question}

Answer:
"""

    payload = {
        "inputs": prompt,
        "parameters": {
            "max_new_tokens": 300,
            "temperature": 0.6,
            "return_full_text": False
        }
    }

    response = requests.post(API_URL, headers=HEADERS, json=payload, timeout=60)

    if response.status_code != 200:
        return f"Error from model: {response.text}"

    result = response.json()
    return result[0]["generated_text"].strip()