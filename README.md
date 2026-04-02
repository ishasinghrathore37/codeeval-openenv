<<<<<<< HEAD
---
title: Codeeval Openenv
emoji: 🏆
colorFrom: purple
colorTo: red
sdk: docker
pinned: false
license: mit
short_description: 'AI-powered coding evaluator using LLM + reinforcement '
---

Check out the configuration reference at https://huggingface.co/docs/hub/spaces-config-reference
=======
💀 CodeEval OpenEnv — RL Environment for LLM Coding Agents

🚀 Overview

CodeEval OpenEnv is a LeetCode-style reinforcement learning environment where Large Language Models (LLMs) generate code solutions that are evaluated through a sandboxed execution system with structured reward scoring.

This project simulates a real-world coding evaluation platform, combining:

- AI-based code generation
- Secure execution
- Automated grading
- Reinforcement learning feedback loops

---

🎯 Problem Statement

Evaluating AI-generated code is challenging due to:

- Lack of standardized environments
- Unsafe code execution risks
- No feedback-driven improvement mechanism

---

💡 Solution

CodeEval OpenEnv provides a complete pipeline:

Problem → LLM → Code Generation → Sandbox Execution → Evaluation → Reward

This enables:

- Safe execution of untrusted code
- Partial scoring using hidden test cases
- Iterative improvement using reward feedback

---

🧠 Key Features

✅ Multi-Level Tasks

- Easy → Medium → Hard
- Real-world coding problems
- Structured datasets with public + hidden test cases

---

🤖 LLM Code Generation

- AI agent generates solutions dynamically
- Prompt-based reasoning
- Retry mechanism for improvement

---

🛡️ Secure Sandbox Execution

- Code runs inside isolated environment
- Timeout protection
- Prevents unsafe operations

---

📊 Reward-Based Evaluation

- Score range: 0.0 → 1.0
- Partial credit for passing test cases
- Penalty for inefficient/long code
- Bonus for optimal solutions

---

🔁 Self-Improving Agent (Retry System)

- Multiple attempts per problem
- Best solution selected based on reward
- Simulates learning behavior

---

⚙️ Tech Stack

- Python
- Streamlit (Frontend UI)
- Hugging Face Transformers (LLM)
- Docker (Sandbox execution)
- Pydantic (Data validation)

---

🏗️ Project Structure

codeeval-openenv/
│
├── env/              # Core RL environment
├── agent/            # LLM agent
├── tasks/            # Problem dataset
├── scripts/          # Baseline runner
├── app.py            # Streamlit UI
├── requirements.txt
└── README.md

---

▶️ How to Run Locally

# Install dependencies
pip install -r requirements.txt

# Run baseline system
python -m scripts.baseline

# Launch UI
streamlit run app.py

---

🌐 Live Demo

👉 (Paste your Hugging Face Space link here)

---

🧪 Example Output

Problem: Two Sum

Attempt 1 → Reward: 0.3  
Attempt 2 → Reward: 0.6  
Attempt 3 → Reward: 1.0  

Best Code:
def solution(...)

Final Score: 1.0

---

🔥 Why This Project Stands Out

- Combines LLM + Reinforcement Learning concepts
- Implements real-world evaluation pipeline
- Includes secure sandbox execution
- Demonstrates AI system design thinking
- Fully deployable and interactive

---

🚀 Future Improvements

- PPO-based learning for true RL optimization
- Leaderboard and scoring analytics
- Larger dataset (100+ problems)
- Multi-language code support
- Fine-tuned LLM for better performance

---

👩‍💻 Author

Isha Singh Rathore
Engineering Student | AI & Cybersecurity Enthusiast

---

⭐ Final Note

This project is not just a coding assignment —
it is a mini AI system that simulates how modern coding platforms evaluate intelligent agents.

💀 Built with a focus on real-world applicability, scalability, and AI integration.
>>>>>>> 9b757d0 (Initial commit - RL LLM project)
