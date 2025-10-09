import google.generativeai as genai
import os
import re
from typing import Optional

# Try to load .env file if python-dotenv is available
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

class CalculatorAgent:
    """
    An intelligent calculator agent powered by Google's Gemini API.
    Performs mathematical calculations through natural language processing.
    """
    
    def __init__(self, api_key: Optional[str] = None, model_name: str = "gemini-2.5-flash"):
        """
        Initialize the Calculator Agent.
        
        Args:
            api_key: Google API key. If None, reads from gemini_api_key env variable
            model_name: Model to use (gemini-2.5-flash, gemini-2.5-pro, or gemini-2.5-flash-latest)
        """
        self.api_key = api_key or os.getenv('gemini_api_key')
        if not self.api_key:
            raise ValueError("API key required. Set gemini_api_key env variable or pass api_key parameter")
        
        genai.configure(api_key=self.api_key)
        self.model_name = model_name
        
        # Configure the model with calculator-specific instructions
        self.model = genai.GenerativeModel(
            model_name=self.model_name,
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,  # Low temperature for accurate calculations
                top_p=1,
                top_k=1,
                max_output_tokens=1024,
            ),
            system_instruction="""You are a mathematical calculator assistant. 
            Your primary task is to solve mathematical problems accurately.
            
            Rules:
            1. Always show the calculation steps
            2. Provide the final answer clearly marked as "Answer: "
            3. Support basic arithmetic, algebra, trigonometry, calculus concepts
            4. Explain complex calculations briefly
            5. For word problems, extract the mathematical expression first
            6. Be precise and accurate in all calculations
            
            Format your response as:
            Steps: [show calculation steps]
            Answer: [final numerical result]
            """
        )
        
        self.chat = self.model.start_chat(history=[])
        self.calculation_history = []
    
    def calculate(self, expression: str) -> dict:
        """
        Perform a calculation based on natural language input.
        
        Args:
            expression: Mathematical expression or word problem
            
        Returns:
            dict: Contains 'expression', 'steps', 'answer', and 'full_response'
        """
        try:
            # Send the calculation request
            response = self.chat.send_message(expression)
            full_response = response.text
            
            # Extract answer from response
            answer = self._extract_answer(full_response)
            
            # Store in history
            result = {
                'expression': expression,
                'full_response': full_response,
                'answer': answer,
                'status': 'success'
            }
            
            self.calculation_history.append(result)
            return result
            
        except Exception as e:
            error_result = {
                'expression': expression,
                'full_response': f"Error: {str(e)}",
                'answer': None,
                'status': 'error'
            }
            self.calculation_history.append(error_result)
            return error_result
    
    def _extract_answer(self, response: str) -> Optional[str]:
        """Extract the numerical answer from the response."""
        # Look for "Answer:" pattern
        answer_match = re.search(r'Answer:\s*([^\n]+)', response, re.IGNORECASE)
        if answer_match:
            return answer_match.group(1).strip()
        
        # Look for final number in the response
        numbers = re.findall(r'-?\d+\.?\d*', response)
        if numbers:
            return numbers[-1]
        
        return None
    
    def get_history(self) -> list:
        """Get calculation history."""
        return self.calculation_history
    
    def clear_history(self):
        """Clear calculation history."""
        self.calculation_history = []
        self.chat = self.model.start_chat(history=[])
        print("✓ History cleared!\n")
    
    def show_history(self):
        """Display calculation history in a formatted way."""
        if not self.calculation_history:
            print("No calculations yet.\n")
            return
        
        print("\n" + "=" * 60)
        print("CALCULATION HISTORY")
        print("=" * 60)
        for i, calc in enumerate(self.calculation_history, 1):
            print(f"\n[{i}] {calc['expression']}")
            if calc['answer']:
                print(f"    Answer: {calc['answer']}")
            print("-" * 60)
        print()


def print_help():
    """Print help information."""
    print("\n" + "=" * 60)
    print("CALCULATOR AGENT - Commands & Examples")
    print("=" * 60)
    print("\n📝 Commands:")
    print("  /help     - Show this help menu")
    print("  /history  - Show calculation history")
    print("  /clear    - Clear calculation history")
    print("  /quit     - Exit the calculator")
    
    print("\n🔢 Example Calculations:")
    print("  • 25 + 37 * 2")
    print("  • What is the square root of 144?")
    print("  • Calculate 15% of 250")
    print("  • If I have 5 apples and buy 3 more, how many do I have?")
    print("  • Solve: 2x + 5 = 15")
    print("  • What is sin(30 degrees)?")
    print("  • Convert 100 Fahrenheit to Celsius")
    print("=" * 60 + "\n")


def main():
    """Main function to run the calculator agent."""
    print("\n" + "🧮 " + "=" * 58)
    print("   CALCULATOR AGENT - Powered by Gemini AI")
    print("=" * 60 + "\n")
    
    try:
        # Initialize calculator agent
        calculator = CalculatorAgent()
        
        print("✓ Calculator initialized! Type your mathematical expression.")
        print("  Type /help for examples and commands.\n")
        
        # Main calculation loop
        while True:
            try:
                user_input = input("Calculate: ").strip()
                
                if not user_input:
                    continue
                
                # Handle commands
                if user_input.startswith('/'):
                    command = user_input.lower()
                    
                    if command == '/quit' or command == '/exit':
                        print("\n👋 Goodbye! Happy calculating!")
                        break
                    
                    elif command == '/help':
                        print_help()
                        continue
                    
                    elif command == '/history':
                        calculator.show_history()
                        continue
                    
                    elif command == '/clear':
                        calculator.clear_history()
                        continue
                    
                    else:
                        print("❌ Unknown command. Type /help for available commands.\n")
                        continue
                
                # Perform calculation
                print("\n🔄 Calculating...\n")
                result = calculator.calculate(user_input)
                
                if result['status'] == 'success':
                    print("📊 " + "=" * 58)
                    print(result['full_response'])
                    print("=" * 60 + "\n")
                else:
                    print(f"❌ {result['full_response']}\n")
                
            except KeyboardInterrupt:
                print("\n\n👋 Goodbye!")
                break
            except EOFError:
                break
    
    except ValueError as e:
        print(f"\n❌ {e}")
        print("\n📝 Setup Instructions:")
        print("1. Install: pip install google-generativeai python-dotenv")
        print("2. Get API key: https://makersuite.google.com/app/apikey")
        print("3. Create a .env file with:")
        print("   gemini_api_key=your-api-key-here\n")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}\n")


if __name__ == "__main__":
    main()