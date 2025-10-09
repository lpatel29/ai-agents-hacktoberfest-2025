# AI Agents - Hacktoberfest 2025

A Python-based AI agent project utilizing Google's Gemini API for intelligent query processing and content generation.

## Overview

This project demonstrates the implementation of AI agents using Google's Generative AI (Gemini) model. It provides a simple yet powerful interface to interact with state-of-the-art language models for various natural language processing tasks.

## Features

- **Gemini AI Integration**: Leverages Google's Gemini Pro model for advanced language understanding
- **Environment Configuration**: Secure API key management using environment variables
- **Simple Query Interface**: Easy-to-use Python interface for AI interactions
- **Modular Architecture**: Clean, maintainable code structure for future enhancements

## Prerequisites

Before running this project, ensure you have:

- Python 3.8 or higher
- pip (Python package manager)
- A Google Gemini API key ([Get one here](https://aistudio.google.com/app/apikey))

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/ai-agents-hacktoberfest-2025.git
   cd ai-agents-hacktoberfest-2025
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv .venv
   ```

3. **Activate the virtual environment:**
   - Windows:
     ```bash
     .venv\Scripts\activate
     ```
   - macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

5. **Set up environment variables:**
   - Create a `.env` file in the project root
   - Add your Gemini API key:
     ```
     GEMINI_API_KEY=your_api_key_here
     ```

## Usage

Run the main script to interact with the AI agent:

```bash
python prompt.py
```

### Example Code

```python
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel('gemini-pro')
query = "What are AI agents?"
response = model.generate_content(query)

print(response.text)
```

## Project Structure

```
ai-agents-hacktoberfest-2025/
├── .venv/                 # Virtual environment
├── prompt.py              # Main script
├── .env                   # Environment variables (not tracked)
├── .gitignore            # Git ignore file
├── requirements.txt       # Python dependencies
└── README.md             # Project documentation
```

## Dependencies

- `google-generativeai`: Google's Gemini AI SDK
- `python-dotenv`: Environment variable management

## Troubleshooting

**Import errors**: Ensure your virtual environment is activated and all packages are installed.

**API key issues**: Verify your API key is valid and properly set in the `.env` file.

**Module not found**: Run `pip install -r requirements.txt` to install all dependencies.

## Contributing

Contributions are welcome! This project is part of Hacktoberfest 2025. Please feel free to submit pull requests or open issues for bugs and feature requests.

## License

This project is open source and available under the MIT License.

## Acknowledgments

- Google Generative AI team for the Gemini API
- Hacktoberfest 2025 organizers and participants

---

**Happy Coding! 🚀**