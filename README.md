# 🎨 Post Architect: Influencer-Style LinkedIn Content Generator

**Post Architect** is a specialized AI tool engineered to mimic the high-engagement posting styles of top LinkedIn influencers, such as **Muskan Handa**. Unlike generic AI writers, this application uses a curated knowledge base and **Few-Shot Prompting** to generate posts that actually resonate with the LinkedIn algorithm and professional audiences.



## 🚀 Live Demo
**Frontend & API:** [https://post-generator-8dbf.onrender.com](https://post-generator-8dbf.onrender.com)

---

## ✨ Key Features
- **Persona Mimicry:** Specifically tuned to replicate the "hook-value-action" structure of professional LinkedIn creators.
- **Bilingual Generation:** Supports high-quality output in both **English (Global)** and **Hinglish** (the preferred style for Indian professional audiences).
- **Glassmorphism UI:** A sleek, modern light-theme interface with a soft-focus aesthetic and a "Copy to Clipboard" utility.
- **Context-Aware Lengths:** Ability to toggle between "Quick Tips" and "Deep Dives" while maintaining the influencer's tone.

---

## 🛠️ Tech Stack
- **AI Orchestration:** LangChain with **Mistral AI** (`mistral-small-latest`).
- **Backend:** FastAPI (Python) for high-performance asynchronous API handling.
- **Frontend:** HTML5, CSS3 (Glassmorphism), and Vanilla JavaScript.
- **Data Logic:** Custom **Few-Shot Learning** implementation using a `JSON` storage of influencer data.
- **DevOps:** Render (Cloud Hosting) with absolute path resolution for production stability.

---

## 📂 Project Structure
```text
Post_Generator/
├── app/
│   ├── app.py              # FastAPI core & CORS configuration
│   └── templates/
│       └── app.html        # Glassmorphism UI & JS Logic
├── Post_generation/
│   ├── __init__.py         # Package initialization
│   ├── generate_post.py    # Mistral AI prompt orchestration
│   ├── few_short.py        # Logic to load persona-based examples
│   └── Data/               # Knowledge base: processed_post_data.json
├── render-build.sh         # Bash script for Render build environment
├── requirements.txt        # Production-grade dependencies
└── setup.py                # Editable install configuration

```
---
##Engineering Highlights
1. Hinglish & Cultural Context
The engine is prompted to understand the nuance of Hinglish, making it ideal for the Indian tech ecosystem. It correctly balances professional English vocabulary with conversational Hindi terms to maximize relatability and engagement.

2. Few-Shot Data Loading
To solve the FileNotFoundError common in cloud deployments, this project implements Robust Path Resolution using the pathlib library. This ensures the model can always access its "Few-Shot" training data, regardless of the server environment.

3. Persona-Based Prompting
The model is instructed via system roles to adopt the specific persona of a growth-focused influencer. This ensures the output includes:

    Strong Hooks: Captivating first lines to stop the scroll.

    White Space: Clean formatting for better readability.

    Strategic Emojis: Used for emphasis, not just decoration.


## ⚙️ Installation

### Clone Repository
```bash
git clone https://github.com/akshadj24/Post_Generator.git
cd Post_Generator

```
```
Install Dependencies
pip install -r requirements.txt
pip install -e .
Setup Environment Variables
Create .env file:

MISTRAL_API_KEY=your_api_key_here
```

```
Run Application
uvicorn app.app:app --reload

```
 ---
## 👤 Author
Akshad Joshi AI & Data Science Engineering Student www.LinkedIn.com/akshadj21 | https://github.com/akshadj24


   
