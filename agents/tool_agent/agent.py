"""Agent with function calling capabilities"""
import google.generativeai as genai
import time


class ToolAgent:
    def __init__(self):
        self.tools = [
            {
                "function_declarations": [
                    {
                        "name": "calculate",
                        "description": "Perform mathematical calculations",
                        "parameters": {
                            "type": "object",
                            "properties": {
                                "expression": {
                                    "type": "string",
                                    "description": "Mathematical expression to evaluate"
                                }
                            },
                            "required": ["expression"]
                        }
                    },
                    {
                        "name": "get_current_time",
                        "description": "Get the current time",
                        "parameters": {"type": "object", "properties": {}}
                    }
                ]
            }
        ]
        
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            tools=self.tools
        )
        self.chat = self.model.start_chat()
    
    def calculate(self, expression: str) -> float:
        """Execute calculation"""
        try:
            return eval(expression)
        except Exception as e:
            return f"Error: {str(e)}"
    
    def get_current_time(self) -> str:
        """Get current time"""
        return time.strftime("%Y-%m-%d %H:%M:%S")
    
    def process_request(self, message: str) -> str:
        """Process request and execute functions if needed"""
        response = self.chat.send_message(message)
        
        if response.candidates[0].content.parts[0].function_call:
            function_call = response.candidates[0].content.parts[0].function_call
            function_name = function_call.name
            function_args = dict(function_call.args)
            
            print(f"🔧 Calling function: {function_name} with args: {function_args}")
            
            if function_name == "calculate":
                result = self.calculate(function_args.get("expression"))
            elif function_name == "get_current_time":
                result = self.get_current_time()
            else:
                result = "Function not found"
            
            response = self.chat.send_message({
                "function_response": {
                    "name": function_name,
                    "response": {"result": result}
                }
            })
        
        return response.text
