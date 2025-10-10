"""Research agent for in-depth topic analysis"""
import google.generativeai as genai


class ResearchAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="""You are a research assistant. Your job is to:
            1. Analyze questions thoroughly
            2. Provide well-structured, factual information
            3. Cite reasoning when making claims
            4. Ask clarifying questions when needed"""
        )
    
    def research(self, topic: str) -> str:
        """Research a topic and provide detailed information"""
        prompt = f"""Research the following topic and provide a comprehensive overview:
        
        Topic: {topic}
        
        Please structure your response with:
        1. Main concepts
        2. Key points
        3. Important considerations
        4. Summary"""
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def quick_fact(self, question: str) -> str:
        """Get a quick factual answer"""
        prompt = f"Provide a concise, factual answer: {question}"
        response = self.model.generate_content(prompt)
        return response.text
