"""Multi-agent system for content creation"""
import google.generativeai as genai
from typing import Dict


class WriterAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="You are a creative writer. Write engaging, clear content."
        )
    
    def write_content(self, topic: str, style: str = "professional") -> str:
        """Write content on a topic"""
        prompt = f"Write a {style} article about: {topic}"
        response = self.model.generate_content(prompt)
        return response.text


class EditorAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="""You are an editor. Review content for:
            - Grammar and spelling
            - Clarity and coherence
            - Structure and flow
            - Fact-checking"""
        )
    
    def edit_content(self, content: str) -> str:
        """Edit and improve content"""
        prompt = f"""Edit the following content and provide:
        1. The improved version
        2. Key changes made
        3. Suggestions for further improvement
        
        Content:
        {content}"""
        
        response = self.model.generate_content(prompt)
        return response.text


class ContentCreationTeam:
    def __init__(self):
        self.writer = WriterAgent()
        self.editor = EditorAgent()
    
    def create_content(self, topic: str, style: str = "professional") -> Dict[str, str]:
        """Collaborative content creation"""
        print(f"📝 Writer is creating content about: {topic}")
        draft = self.writer.write_content(topic, style)
        
        print("✏️  Editor is reviewing the content...")
        edited = self.editor.edit_content(draft)
        
        return {
            "topic": topic,
            "draft": draft,
            "edited": edited
        }
