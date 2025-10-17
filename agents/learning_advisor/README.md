# 🎓 Learning Path Advisor

An AI-powered tool that helps you create and explore personalized learning paths for any topic with interactive Q&A support.

## ✨ Features

- 🚀 Generate structured learning paths with clear milestones
- 🎯 Customize based on your current level (beginner, intermediate, advanced)
- ⏱️ Set specific learning goals and time commitments
- 💬 Interactive Q&A mode for your learning path
- 🔄 Navigate between paths and questions seamlessly
- 🎨 Clean, user-friendly command-line interface

## 🚀 Usage

1. Run the learning advisor:
   ```bash
   python agent.py
   ```

2. Follow the interactive prompts to create your learning path:
   - Enter the topic you want to learn
   - Specify your current level (beginner/intermediate/advanced)
   - Add an optional learning goal
   - Receive a structured learning path

3. After generating a path, you can:
   - Ask questions about any part of the learning path
   - Type `/newPath` to create a new learning path
   - Type `/exit` to quit the program

### Example Commands in Q&A Mode
- "What are the key concepts in phase 2?"
- "Can you explain more about the milestone project?"
- "What resources do you recommend for learning about [topic]?"
- "/newPath" - Start a new learning path
- "/exit" - Exit the program

## 💡 Example Session

```
🎓 LEARNING PATH ADVISOR
================================================================================

Welcome! I'll help you create a personalized learning path.
Type 'quit' or 'exit' to end the session.

--------------------------------------------------------------------------------

What would you like to learn? Python for data analysis

Your current level? [beginner/intermediate/advanced] beginner

Your learning goal (optional): Be able to analyze and visualize datasets

⏳ Creating your learning path...

================================================================================
[Learning path content displayed here...]
================================================================================

🤖 You can now ask questions about this learning path.
  Type /newPath to create a new learning path
  Type /exit to quit

❓ Your question: What are the key concepts in phase 2?

💡 In phase 2, you'll learn about data structures in Python including:
   - Lists and list operations
   - Dictionaries and their methods
   - Tuples and sets
   - Data manipulation techniques

❓ Your question: /newPath

Creating a new learning path...

[New learning path creation starts...]
```

## 📝 Prerequisites

- Python 3.7+
- Gemini API key (get one from [Google AI Studio](https://aistudio.google.com/))
- Required packages in `requirements.txt`

## 🛠️ Installation

1. Clone the repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project root:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

## 🤝 Contributing

This agent is part of Hacktoberfest 2025! We welcome contributions:
- Add new features (persistent storage, spaced repetition)
- Improve learning path generation prompts
- Add integration with learning platforms
- Create example learning paths for popular topics
- Enhance documentation and error handling

## 📄 License

MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

Built with Google's Gemini AI for Hacktoberfest 2025.

## 📄 License

See main repository LICENSE file.

## 🙏 Acknowledgments

Built with Google's Gemini AI for Hacktoberfest 2025.
