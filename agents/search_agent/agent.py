"""
Simple Search Agent
Description: A basic AI agent that searches the web using DuckDuckGo (no API key needed)
Author: @lpatel29
"""

import requests
from bs4 import BeautifulSoup
import time


class SimpleSearchAgent:
    """
    A simple search agent that uses DuckDuckGo for web searches.
    No API keys required!
    
    Features:
    - Free web search
    - Extract text from search results
    - Summarize findings
    """
    
    def __init__(self):
        """Initialize the search agent"""
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
    
    def search(self, query, num_results=5):
        """
        Search the web using DuckDuckGo HTML version.
        
        Args:
            query: Search query string
            num_results: Number of results to return (default: 5)
            
        Returns:
            List of dictionaries with title, link, and snippet
        """
        print(f"🔍 Searching for: {query}\n")
        
        # Use DuckDuckGo HTML version (no API key needed)
        search_url = "https://html.duckduckgo.com/html/"
        params = {'q': query}
        
        try:
            response = requests.post(search_url, data=params, headers=self.headers)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.text, 'html.parser')
            results = []
            
            # Find search result elements
            for result in soup.find_all('div', class_='result')[:num_results]:
                title_elem = result.find('a', class_='result__a')
                snippet_elem = result.find('a', class_='result__snippet')
                
                if title_elem:
                    results.append({
                        'title': title_elem.get_text(strip=True),
                        'link': title_elem.get('href', ''),
                        'snippet': snippet_elem.get_text(strip=True) if snippet_elem else 'No description'
                    })
            
            return results
            
        except Exception as e:
            print(f"❌ Error during search: {e}")
            return []
    
    def display_results(self, results):
        """
        Display search results in a readable format.
        
        Args:
            results: List of search result dictionaries
        """
        if not results:
            print("❌ No results found.")
            return
        
        print(f"✅ Found {len(results)} results:\n")
        print("=" * 80)
        
        for i, result in enumerate(results, 1):
            print(f"\n{i}. {result['title']}")
            print(f"   🔗 {result['link']}")
            print(f"   📝 {result['snippet']}")
            print("-" * 80)
    
    def research(self, topic):
        """
        Conduct research on a topic and present findings.
        
        Args:
            topic: Research topic or question
        """
        print("\n" + "=" * 80)
        print(f"🤖 SIMPLE SEARCH AGENT")
        print("=" * 80)
        
        # Perform search
        results = self.search(topic)
        
        # Display results
        self.display_results(results)
        
        # Simple summary
        if results:
            print("\n📊 SUMMARY:")
            print(f"Searched for: '{topic}'")
            print(f"Found {len(results)} relevant results")
            print(f"Top result: {results[0]['title']}")
        
        print("\n" + "=" * 80)
        
        return results
    
    def multi_query_research(self, queries):
        """
        Perform multiple searches for comprehensive research.
        
        Args:
            queries: List of search queries
        """
        all_results = {}
        
        for query in queries:
            print(f"\n🔎 Query: {query}")
            results = self.search(query, num_results=3)
            all_results[query] = results
            time.sleep(1)  # Be nice to the server
        
        return all_results


# Example usage
if __name__ == "__main__":
    # Create agent instance
    agent = SimpleSearchAgent()
    
    # Example 1: Simple search
    print("\n" + "🚀 EXAMPLE 1: Simple Search" + "\n")
    agent.research("Python programming tutorials")
    
    # Wait a bit
    time.sleep(2)
    
    # Example 2: AI-related search
    print("\n\n" + "🚀 EXAMPLE 2: AI Research" + "\n")
    agent.research("What are AI agents?")
    
    # Wait a bit
    time.sleep(2)
    
    # Example 3: Multiple queries for comprehensive research
    print("\n\n" + "🚀 EXAMPLE 3: Multi-Query Research" + "\n")
    queries = [
        "AI agents 2025",
        "LangChain tutorial",
        "How to build chatbots"
    ]
    
    results = agent.multi_query_research(queries)
    
    print("\n📈 COMPREHENSIVE RESEARCH COMPLETE")
    print(f"Total queries: {len(queries)}")
    print(f"Total results: {sum(len(r) for r in results.values())}")