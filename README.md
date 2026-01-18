# 🤖 AI-Powered Interview Assistant

Practice interview questions with **context-aware, professional answers** instantly. This app is powered by an AI language model (Mistral) and provides role-tailored interview answers for various experience levels.



# 📝 Features

- Generate **interview-ready answers** in first person.
- Control **answer length**: Short (3-4 sentences), Medium (5-6 sentences), Long (7-8 sentences).
- Select **experience level**: Fresher, Intermediate, Expert.
- Choose **interview type/domain**: General, HR, Behavioral.
- Select from **example questions** or type your own.



# ⚡ How It Works

1. User enters an interview question (or selects an example question).  
2. Chooses experience level, domain, and answer length.  
3. Clicks **Generate Answer**.  
4. The app calls the **Ollama Mistral** LLM model locally to generate an AI-powered answer.  



# 💻 Local Setup

# Prerequisites
- Python 3.10+
- [Streamlit](https://streamlit.io/)
- [Ollama](https://ollama.com/) installed and Mistral model downloaded locally.

# Installation

1. Clone this repository:
   ```bash
   git clone <your-repo-link>
   cd <your-project-folder>

2. Create a virtual environment:
   python  -m venv venv
   venv\scripts\activate  # windows
   source venv/bin/activate  # Mac/Linux

3. Install dependencies:
   pip install -r requirements.txt

4. Make sure Ollama Mistral is installed locally:
   Ollama pull mistral      

5. Run Streamlit app:

   streamlit run app.py   
