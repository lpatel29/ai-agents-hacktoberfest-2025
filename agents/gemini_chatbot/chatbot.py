import google.generativeai as genai
import os
from datetime import datetime
from typing import Optional

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load environment variables from .env file
except ImportError:
    pass  # python-dotenv not installed, will use system env variables

class GeminiChatbot:
    """
    An intelligent chatbot powered by Google's Gemini API.
    Features conversation memory, personality customization, and rich interactions.
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.5-flash"):
        """
        Initialize the Gemini Chatbot.
        
        Args:
            api_key: Google API key. If None, reads from gemini_api_key env variable
            model_name: Model to use (gemini-2.5-flash or gemini-2.5-pro)
        """
        self.api_key = api_key or os.getenv('gemini_api_key')
        if not self.api_key:
            raise ValueError("API key required. Set gemini_api_key env variable or pass api_key parameter")
        
        genai.configure(api_key=self.api_key)
        self.model_name = model_name
        self.model = genai.GenerativeModel(model_name)
        self.chat = None
        self.conversation_history = []
        self.bot_name = "Gemini"
        
    def set_personality(self, personality: str):
        """
        Set the chatbot's personality with a system instruction.
        
        Args:
            personality: Description of how the bot should behave
        """
        generation_config = genai.types.GenerationConfig(
            temperature=0.9,
            top_p=1,
            top_k=1,
            max_output_tokens=2048,
        )
        
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=generation_config,
            system_instruction=personality
        )
        self.chat = self.model.start_chat(history=[])
        print(f"✓ Personality set: {personality[:50]}...\n")
        
    def start_conversation(self):
        """Start a new conversation session."""
        if not self.chat:
            self.chat = self.model.start_chat(history=[])
        self.conversation_history = []
        print(f"🤖 {self.bot_name}: Hello! I'm ready to chat. How can I help you today?\n")
        
    def send_message(self, user_message: str) -> str:
        """
        Send a message to the chatbot and get a response.
        
        Args:
            user_message: The user's message
            
        Returns:
            The bot's response
        """
        if not self.chat:
            self.start_conversation()
        
        try:
            # Send message and get response
            response = self.chat.send_message(user_message)
            bot_response = response.text
            
            # Store in history
            self.conversation_history.append({
                'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'user': user_message,
                'bot': bot_response
            })
            
            return bot_response
            
        except Exception as e:
            error_msg = f"Error: {str(e)}"
            print(f"❌ {error_msg}")
            return error_msg
    
    def get_conversation_summary(self) -> str:
        """Get a summary of the current conversation."""
        if not self.conversation_history:
            return "No conversation yet."
        
        summary = f"Conversation Summary ({len(self.conversation_history)} exchanges):\n"
        summary += "=" * 50 + "\n"
        for i, entry in enumerate(self.conversation_history, 1):
            summary += f"\n[{entry['timestamp']}]\n"
            summary += f"You: {entry['user'][:100]}{'...' if len(entry['user']) > 100 else ''}\n"
            summary += f"Bot: {entry['bot'][:100]}{'...' if len(entry['bot']) > 100 else ''}\n"
        return summary
    
    def save_conversation(self, filename: str = "conversation.txt"):
        """Save the conversation history to a file."""
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Gemini Chatbot Conversation Log\n")
            f.write(f"{'=' * 50}\n\n")
            for entry in self.conversation_history:
                f.write(f"[{entry['timestamp']}]\n")
                f.write(f"USER: {entry['user']}\n")
                f.write(f"BOT: {entry['bot']}\n")
                f.write(f"{'-' * 50}\n\n")
        print(f"✓ Conversation saved to {filename}")
    
    def clear_conversation(self):
        """Clear conversation history and start fresh."""
        self.chat = self.model.start_chat(history=[])
        self.conversation_history = []
        print("✓ Conversation cleared!\n")


def print_commands():
    """Print available commands."""
    print("\n" + "=" * 50)
    print("Available Commands:")
    print("=" * 50)
    print("  /help       - Show this help menu")
    print("  /clear      - Clear conversation history")
    print("  /summary    - Show conversation summary")
    print("  /save       - Save conversation to file")
    print("  /personality- Set bot personality")
    print("  /quit       - Exit the chatbot")
    print("=" * 50 + "\n")


def main():
    """Main function to run the chatbot."""
    print("\n" + "🤖 " + "=" * 48)
    print("   GEMINI CHATBOT - Powered by Google AI")
    print("=" * 50 + "\n")
    
    try:
        # Initialize chatbot
        chatbot = GeminiChatbot()
        
        # Set default personality
        chatbot.set_personality(
            "You are a helpful, friendly, and knowledgeable AI assistant. "
            "Be conversational, engaging, and provide clear, concise answers. "
            "Show personality and warmth in your responses."
        )
        
        chatbot.start_conversation()
        print_commands()
        
        # Main conversation loop
        while True:
            try:
                user_input = input("You: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    command = user_input.lower()
                    
                    if command == '/quit' or command == '/exit':
                        print(f"\n👋 {chatbot.bot_name}: Goodbye! Have a great day!")
                        break
                    
                    elif command == '/help':
                        print_commands()
                        continue
                    
                    elif command == '/clear':
                        chatbot.clear_conversation()
                        continue
                    
                    elif command == '/summary':
                        print("\n" + chatbot.get_conversation_summary() + "\n")
                        continue
                    
                    elif command == '/save':
                        filename = input("Enter filename (default: conversation.txt): ").strip()
                        chatbot.save_conversation(filename if filename else "conversation.txt")
                        continue
                    
                    elif command == '/personality':
                        print("\nDescribe the personality you want the bot to have:")
                        personality = input("> ").strip()
                        if personality:
                            chatbot.set_personality(personality)
                            chatbot.clear_conversation()
                            chatbot.start_conversation()
                        continue
                    
                    else:
                        print("❌ Unknown command. Type /help for available commands.\n")
                        continue
                
                # Send message and display response
                response = chatbot.send_message(user_input)
                print(f"\n🤖 {chatbot.bot_name}: {response}\n")
                
            except KeyboardInterrupt:
                print(f"\n\n👋 {chatbot.bot_name}: Goodbye!")
                break
            except EOFError:
                break
                
    except ValueError as e:
        print(f"\n❌ {e}")
        print("\n📝 Setup Instructions:")
        print("1. Install: pip install google-generativeai python-dotenv")
        print("2. Get API key: https://makersuite.google.com/app/apikey")
        print("3. Create a .env file in the same directory with:")
        print("   gemini_api_key=your-api-key-here")
        print("\nAlternatively, set environment variable:")
        print("   export gemini_api_key='your-api-key-here'")
        print("\nOr pass the API key directly:")
        print("   chatbot = GeminiChatbot(api_key='your-key')\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")


if __name__ == "__main__":
    main()