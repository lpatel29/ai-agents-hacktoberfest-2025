"""Code generation and review agent"""
import google.generativeai as genai


class CodeAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="""You are an expert programming assistant. 
            Generate clean, well-documented code with explanations."""
        )
    
    def generate_code(self, description: str, language: str = "python") -> str:
        """Generate code based on description"""
        prompt = f"""Generate {language} code for the following task:
        
        {description}
        
        Include:
        - Clean, readable code
        - Comments explaining key parts
        - Example usage if applicable"""
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def review_code(self, code: str) -> str:
        """Review and suggest improvements for code"""
        prompt = f"""Review the following code and suggest improvements:
        
        ```
        {code}
        ```
        
        Provide:
        1. Code quality assessment
        2. Potential bugs or issues
        3. Optimization suggestions
        4. Best practice recommendations"""
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def explain_code(self, code: str) -> str:
        """Explain what code does"""
        prompt = f"Explain what this code does:\n\n{code}"
        response = self.model.generate_content(prompt)
        return response.text
