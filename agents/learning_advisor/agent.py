"""
Learning Path Advisor
A simple agent that creates personalized learning paths for any topic.
"""

import google.generativeai as genai
from datetime import datetime
from typing import Dict


class LearningPathAdvisor:
    """
    An intelligent learning advisor that helps users:
    - Create personalized learning paths
    - Break down complex topics into manageable milestones
    - Track learning progress
    - Get adaptive recommendations based on skill level
    - Receive curated resource suggestions
    """
    
    def __init__(self):
        """Initialize the Learning Path Advisor with Gemini AI"""
        self.model = genai.GenerativeModel('gemini-2.0-flash')
        self.learning_paths = {}
    
    def create_learning_path(
        self,
        topic: str,
        current_level: str = "beginner",
        goal: str = "",
        time_commitment: str = "1-2 hours/day"
    ) -> Dict:
        """
        Create a personalized learning path for a topic.
        
        Args:
            topic: The subject or skill to learn
            current_level: beginner, intermediate, or advanced
            goal: Specific learning goal or outcome desired
            time_commitment: Available time per day/week
            
        Returns:
            Dictionary containing the learning path or error message
        """
        try:
            prompt = f"""Create a structured learning path with these details:
            Topic: {topic}
            Level: {current_level}
            Goal: {goal or 'Master the topic'}
            Time: {time_commitment}
            
            Include:
            1. 3-5 phases with clear objectives
            2. Key concepts for each phase
            3. Practical exercises
            4. Milestone projects
            """
            
            response = self.model.generate_content(prompt)
            
            # Store the learning path
            path_id = f"{topic.lower().replace(' ', '_')}_{datetime.now().strftime('%Y%m%d')}"
            learning_path = {
                "id": path_id,
                "topic": topic,
                "level": current_level,
                "goal": goal,
                "time_commitment": time_commitment,
                "created_at": datetime.now().isoformat(),
                "content": response.text,
                "context": f"""Learning Path Details:
                Topic: {topic}
                Level: {current_level}
                Goal: {goal or 'Master the topic'}
                Time Commitment: {time_commitment}
                """
            }
            
            self.learning_paths[path_id] = learning_path
            return learning_path
            
        except Exception as e:
            print(f"\n❌ Error generating learning path: {str(e)}")
            return {"error": str(e)}
    
    def answer_question(self, path_id: str, question: str) -> str:
        """
        Answer a question about the learning path
        
        Args:
            path_id: ID of the learning path
            question: The question to answer
            
        Returns:
            String with the answer or error message
        """
        if path_id not in self.learning_paths:
            return "❌ Learning path not found. Please create a learning path first."
            
        path = self.learning_paths[path_id]
        
        prompt = f"""You are a helpful learning assistant. Answer the following question 
        about the learning path. Be specific and refer to the learning path details.
        
        Learning Path Context:
        {path['context']}
        
        Learning Path Content:
        {path['content']}
        
        Question: {question}
        
        Please provide a clear, concise answer that helps the learner understand better.
        """
        
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"❌ Error generating answer: {str(e)}"


def main():
    """Main interactive loop for the Learning Path Advisor"""
    import os
    from dotenv import load_dotenv
    
    # Load environment variables
    load_dotenv()
    
    # Configure Gemini API
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key:
        print("❌ Error: GEMINI_API_KEY not found in .env file")
        print("Please add your Gemini API key to the .env file:")
        print("GEMINI_API_KEY=your_api_key_here")
        exit(1)
    
    genai.configure(api_key=api_key)
    
    print("\n" + "="*80)
    print("🎓 LEARNING PATH ADVISOR")
    print("="*80)
    print("\nWelcome! I'll help you create a personalized learning path.")
    print("Type 'quit' or 'exit' to end the session.\n")
    
    advisor = LearningPathAdvisor()
    
    while True:
        print("\n" + "-"*80)
        topic = input("\nWhat would you like to learn? ").strip()
        
        if not topic:
            print("⚠️  Please enter a topic.")
            continue
            
        if topic.lower() in ['quit', 'exit', 'q']:
            print("\n👋 Happy learning! Goodbye!")
            break
        
        level = input("Your current level? [beginner/intermediate/advanced] ").strip().lower()
        if level not in ['beginner', 'intermediate', 'advanced']:
            level = "beginner"
            
        goal = input("Your learning goal (optional): ").strip()
        
        print("\n⏳ Creating your learning path...")
        
        path = advisor.create_learning_path(
            topic=topic,
            current_level=level,
            goal=goal
        )
        
        if "error" in path:
            print("\n❌ Failed to create learning path. Please try again.")
            continue
            
        print("\n" + "="*80)
        print(path["content"])
        print("="*80)
        
        # Enter Q&A mode
        print("\n🤖 You can now ask questions about this learning path.")
        print("  Type /newPath to create a new learning path")
        print("  Type /exit to quit\n")
        
        while True:
            user_input = input("❓ Your question: ").strip()
            
            # Handle commands
            if user_input.startswith('/'):
                cmd = user_input[1:].lower()
                if cmd in ['exit', 'quit', 'q']:
                    print("\n👋 Happy learning! Goodbye!")
                    return
                elif cmd in ['new', 'newpath', 'create']:
                    print("\nCreating a new learning path...\n")
                    break
                else:
                    print("\n❌ Unknown command. Available commands:")
                    print("  /newPath - Create a new learning path")
                    print("  /exit    - Exit the program\n")
                    continue
            
            # Handle empty input
            if not user_input:
                continue
                
            # Process as a question
            answer = advisor.answer_question(path["id"], user_input)
            print("\n" + "💡 " + answer + "\n")
        
        # Ask if user wants to create another learning path
        again = input("\nWould you like to create another learning path? (y/n) ").strip().lower()
        if again != 'y':
            print("\n👋 Happy learning! Goodbye!")
            break


if __name__ == "__main__":
    main()
