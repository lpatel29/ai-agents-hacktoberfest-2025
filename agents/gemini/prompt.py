import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel('gemini-2.5-flash')

query = "What are AI agents?"
prompt = f"Search and summarize: {query}"
response = model.generate_content(prompt)

print(f"Query: {query}\n\nAnswer:\n{response.text}")