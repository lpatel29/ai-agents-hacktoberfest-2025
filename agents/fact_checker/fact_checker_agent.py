import os
import requests
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")

if not GEMINI_API_KEY or not SERPER_API_KEY:
    raise RuntimeError("Set API keys in .env")

genai.configure(api_key=GEMINI_API_KEY)
gemini = genai.GenerativeModel("gemini-2.0-flash")

def search_serper(query):
    url = "https://google.serper.dev/search"
    headers = {"X-API-KEY": SERPER_API_KEY, "Content-Type": "application/json"}
    data = {"q": query}
    resp = requests.post(url, headers=headers, json=data)
    resp.raise_for_status()
    results = resp.json()
    snippets = [r.get("snippet", "") for r in results.get("organic", [])]
    return "\n".join(snippets[:5])

def fact_check_with_gemini(query, search_snippets):
    prompt = f"""
You are a fact-checking agent.

Search Results:
{search_snippets}

Task:
Check the following query for accuracy:
'{query}'
Provide a factual assessment based only on the search results.
"""
    response = gemini.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    query = input("Enter your query: ")
    search_results = search_serper(query)
    summary = fact_check_with_gemini(query, search_results)

    print(f"\n✅ Fact Check Result for '{query}':\n")
    print(summary)
