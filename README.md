# AI Agents - Hacktoberfest 2025

[![Hacktoberfest 2025](https://img.shields.io/badge/Hacktoberfest-2025-blueviolet)](https://hacktoberfest.com/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)

🎃 This repository is participating in Hacktoberfest 2025!


A collection of small AI/utility agents and examples to learn, contribute, and collaborate during Hacktoberfest 2025.

## 🧠 Demo Video

Here’s a demo video showing the project setup and AI agent interaction:

https://github.com/user-attachments/assets/0b9ecd5b-3a41-4aec-957f-675a7dab2b53

> **Note:** Make sure you have a `.env` file in the project root with your Gemini API key:  
> `GEMINI_API_KEY=your_api_key_here`

### What’s inside
- `agents/` – individual agents and examples
  - `gemini/` – minimal Gemini content generation example
  - `gemini_chatbot/` – simple chat-style interaction (example)
  - `calculator/` – utility agent example

### Quick start
```bash
python -m venv .venv
# Windows PowerShell
. .venv/Scripts/Activate.ps1
pip install -r requirements.txt
```

### Environment variables
Create a `.env` file in the project root:
```bash
GEMINI_API_KEY=your_api_key_here
```

### Run a demo
```bash
python agents/gemini/prompt.py
```

### Contributing (Hacktoberfest 2025)
Contributions are welcome! Please read `/.github/CONTRIBUTING.md` for guidelines. This repository is intended to participate in Hacktoberfest 2025. Substantive PRs are appreciated; maintainers may use the `hacktoberfest-accepted` label when appropriate.

### Troubleshooting
- If your IDE shows `Import "google.generativeai" could not be resolved` but `pip` shows it installed, restart your IDE and ensure it uses the same Python interpreter as your shell.

### License
See `LICENSE`.


