import streamlit as st
import subprocess

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI-Powered Interview Assistant",
    page_icon="🤖",
    layout="centered"
)

st.title("🤖 AI-Powered Interview Assistant")
st.caption("Practice interview questions with **context-aware, professional answers** tailored to your experience level")
st.divider()

# ---------------- EXAMPLE QUESTIONS ----------------
example_qs = [
    "Tell me about yourself",
    "What are your strengths and weaknesses?",
    "Why do you want this job?",
    "Why should we hire you?",
    "Where do you see yourself in 5 years?"
]

selected_example = st.selectbox("Select an example question (optional)", [""] + example_qs)

# ---------------- INPUTS ----------------
question = st.text_input(
    "Interview Question",
    value=selected_example,
    placeholder="Type your question here"
)

col1, col2, col3 = st.columns([1,1,1])

with col1:
    level = st.selectbox(
        "Experience Level",
        ["Fresher", "Intermediate", "Expert"]
    )

with col2:
    domain = st.selectbox(
        "Interview Type",
        ["General", "HR", "Behavioral"]
    )

with col3:
    length = st.radio(
        "Answer Length",
        ["Short (3-4 sentences)", "Medium (5-6 sentences)", "Long (7-8 sentences)"]
    )

generate = st.button("✨ Generate Answer")

# ---------------- LLM FUNCTION ----------------
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
- No job titles, company names, or exaggeration
- Use {length_map[length]}

Candidate level: {level}
Interview type: {domain}

Interview Question:
{question}

Answer:
"""
    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    return result.stdout.strip()

# ---------------- OUTPUT ----------------
if generate:
    if question.strip() == "":
        st.warning("Please enter an interview question.")
    else:
        st.divider()
        with st.spinner("Generating interview-ready answer..."):
            answer = generate_answer(question, level, domain, length)

        st.markdown("### 📝 Interview-Ready Answer")
        st.write(answer)

    


    