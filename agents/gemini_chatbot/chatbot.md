# 🤖 Gemini Chatbot

An intelligent conversational AI agent powered by Google's Gemini API with conversation memory and customizable personality.

## 📋 Specification

**Version:** 1.0.0  
**Model:** Gemini 2.5 Flash  
**Language:** Python 3.7+  
**License:** MIT

## ✨ Features

- 💬 **Context-Aware Conversations** - Maintains full conversation history
- 🎭 **Customizable Personality** - Define bot behavior with system instructions
- 📊 **Session Management** - Save, clear, and summarize conversations
- 💾 **Export Functionality** - Save chat logs to text files
- ⚡ **Fast Responses** - Powered by Gemini 2.5 Flash
- 🔐 **Secure Configuration** - Environment-based API key management
- 🎯 **Command System** - Built-in slash commands for control

## 🏗️ Architecture

```
GeminiChatbot
├── Configuration Layer
│   ├── API Key Management (env/direct)
│   ├── Model Selection (gemini-2.5-flash/pro)
│   └── .env File Support (python-dotenv)
│
├── Core Components
│   ├── GenerativeModel Instance
│   ├── Chat Session Manager
│   └── Conversation History Store
│
├── Features
│   ├── send_message() - Message handling
│   ├── set_personality() - Behavior customization
│   ├── get_conversation_summary() - History analysis
│   ├── save_conversation() - Export to file
│   └── clear_conversation() - Reset session
│
└── CLI Interface
    ├── Interactive Input Loop
    ├── Command Parser (/help, /clear, etc.)
    └── Error Handling & Display
```

## 🚀 Quick Start

### Installation

```bash
# Install dependencies
pip install google-generativeai python-dotenv
```

### Configuration

Create a `.env` file in the project directory:

```env
gemini_api_key=your-api-key-here
```

Get your API key from: https://makersuite.google.com/app/apikey

### Usage

```bash
python chatbot.py
```

## 📚 API Reference

### Class: `GeminiChatbot`

#### Constructor
```python
GeminiChatbot(api_key=None, model_name="gemini-2.5-flash")
```

**Parameters:**
- `api_key` (str, optional): Google API key
- `model_name` (str): Model identifier

#### Methods

| Method | Description | Returns |
|--------|-------------|---------|
| `set_personality(personality)` | Configure bot behavior | None |
| `start_conversation()` | Initialize chat session | None |
| `send_message(message)` | Send user message | str (response) |
| `get_conversation_summary()` | Retrieve chat history | str (formatted summary) |
| `save_conversation(filename)` | Export to file | None |
| `clear_conversation()` | Reset history | None |

## ⌨️ Commands

| Command | Action |
|---------|--------|
| `/help` | Show command list |
| `/clear` | Clear conversation history |
| `/summary` | Display conversation summary |
| `/save` | Export chat to file |
| `/personality` | Change bot personality |
| `/quit` | Exit application |

## 🔧 Configuration Options

### Generation Parameters

```python
GenerationConfig(
    temperature=0.9,      # Creativity (0.0-1.0)
    top_p=1,              # Nucleus sampling
    top_k=1,              # Top-k sampling
    max_output_tokens=2048 # Response length
)
```

### Supported Models

- `gemini-2.5-flash` (default) - Fast, efficient
- `gemini-2.5-pro` - More capable, slower

## 📊 Data Flow

```
User Input → Command Parser → Chat Session → Gemini API
                                    ↓
                            Response Processing
                                    ↓
                            History Storage → Display
```

## 🛡️ Security

- API keys loaded from environment variables
- `.env` file support (excluded from version control)
- No hardcoded credentials in source code

## 🐛 Error Handling

- Invalid API key detection
- Network error recovery
- Graceful exception handling
- User-friendly error messages

## 📝 Example

```python
from chatbot import GeminiChatbot

# Initialize
bot = GeminiChatbot()

# Customize personality
bot.set_personality("You are a Python expert assistant")

# Chat
response = bot.send_message("Explain list comprehensions")
print(response)

# Save conversation
bot.save_conversation("python_help.txt")
```

## 🔗 Resources

- [Gemini API Documentation](https://ai.google.dev/docs)
- [Get API Key](https://makersuite.google.com/app/apikey)

## 📄 License

MIT License - Free for personal and commercial use

---

**Built with Google Gemini API** | Version 1.0.0