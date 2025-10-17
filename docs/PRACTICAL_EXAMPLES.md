# Practical Examples: Functions vs Agents

This document provides side-by-side comparisons using actual code from this repository.

## Table of Contents
1. [Mathematical Operations](#mathematical-operations)
2. [Text Generation](#text-generation)
3. [Decision Making](#decision-making)
4. [Data Analysis](#data-analysis)
5. [Web Search](#web-search)
6. [Code Generation](#code-generation)

---

## Mathematical Operations

### ❌ Traditional Function Approach

```python
def calculate(operation, a, b):
    """Traditional calculator function"""
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b == 0:
            return "Error: Division by zero"
        return a / b
    else:
        return "Unknown operation"

# Usage - must follow exact format
result = calculate("add", 10, 5)  # 15
result = calculate("multiply", 10, 5)  # 50

# Cannot handle:
# - "What's 10 plus 5?"
# - "Calculate 15% tip on $45"
# - "Square root of 144"
```

**Limitations:**
- Must define every operation explicitly
- No natural language support
- Limited to pre-programmed operations
- No explanation of steps

---

### ✅ AI Agent Approach (from `agents/calculator/calculator.py`)

```python
import google.generativeai as genai

class CalculatorAgent:
    def __init__(self, api_key):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-2.5-flash",
            generation_config=genai.types.GenerationConfig(
                temperature=0.1,  # Low for accuracy
            ),
            system_instruction="""You are a mathematical calculator assistant. 
            Your primary task is to solve mathematical problems accurately.
            
            Rules:
            1. Always show the calculation steps
            2. Provide the final answer clearly marked as "Answer: "
            3. Support basic arithmetic, algebra, trigonometry, calculus
            4. Explain complex calculations briefly"""
        )
    
    def calculate(self, query):
        """Calculate with natural language input"""
        response = self.model.generate_content(query)
        return response.text

# Usage - natural language!
agent = CalculatorAgent(api_key="YOUR_KEY")

agent.calculate("What's 10 plus 5?")
# Output: "10 + 5 = 15\nAnswer: 15"

agent.calculate("Calculate 15% tip on $45.50")
# Output: "15% of $45.50 = 0.15 × 45.50 = 6.825
#          Rounded tip: $6.83\nAnswer: $6.83"

agent.calculate("What's the square root of 144?")
# Output: "√144 = 12\nAnswer: 12"

agent.calculate("If I invest $1000 at 5% annual interest for 3 years, what's the total?")
# Output: "Using compound interest: A = P(1 + r)^t
#          A = 1000(1 + 0.05)^3
#          A = 1000(1.157625)
#          A = $1,157.63\nAnswer: $1,157.63"
```

**Advantages:**
- Handles natural language
- Shows work/reasoning
- Understands context
- Flexible problem types

---

## Text Generation

### ❌ Traditional Function Approach

```python
def generate_article(topic, length="short"):
    """Template-based text generation"""
    templates = {
        "AI": {
            "short": "Artificial Intelligence is transforming industries. "
                    "AI systems can learn from data and make decisions. "
                    "The future of AI looks promising.",
            "long": "Artificial Intelligence is transforming industries worldwide. "
                   "These intelligent systems can analyze data, learn patterns, "
                   "and make decisions with minimal human intervention. "
                   "From healthcare to finance, AI is revolutionizing how we work. "
                   "The future of AI holds immense potential."
        },
        "Python": {
            "short": "Python is a popular programming language. "
                    "It's easy to learn and powerful. "
                    "Many developers use Python daily.",
            "long": "Python is a versatile, high-level programming language. "
                   "Known for its clear syntax and readability, Python is "
                   "an excellent choice for beginners and experts alike. "
                   "It's used in web development, data science, AI, and more. "
                   "The Python community is large and supportive."
        }
    }
    
    return templates.get(topic, {}).get(length, "Topic not found")

# Usage - limited and repetitive
article = generate_article("AI", "short")
```

**Limitations:**
- Fixed templates
- No creativity
- Limited topics
- Always same output
- No style variation

---

### ✅ AI Agent Approach (from `agents/content_team/agent.py`)

```python
import google.generativeai as genai

class WriterAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="You are a creative writer. "
                             "Write engaging, clear content."
        )
    
    def write_content(self, topic, style="professional"):
        """Generate creative, unique content"""
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
            - Structure and flow"""
        )
    
    def edit_content(self, content):
        """Improve and refine content"""
        prompt = f"""Edit and improve:\n\n{content}"""
        response = self.model.generate_content(prompt)
        return response.text

class ContentCreationTeam:
    def __init__(self):
        self.writer = WriterAgent()
        self.editor = EditorAgent()
    
    def create_content(self, topic, style="professional"):
        """Collaborative content creation"""
        draft = self.writer.write_content(topic, style)
        edited = self.editor.edit_content(draft)
        return {"draft": draft, "edited": edited}

# Usage - dynamic and creative
team = ContentCreationTeam()
result = team.create_content("The Future of AI in Healthcare", 
                            style="engaging")

# Each generation is unique, contextual, and high-quality
```

**Advantages:**
- Unique, creative content
- Style customization
- Multi-agent collaboration
- Quality improvement loop

---

## Decision Making

### ❌ Traditional Function Approach

```python
def decide_action(temperature, humidity, is_occupied):
    """Simple decision function"""
    if not is_occupied:
        return "OFF"
    
    if temperature > 25:
        return "AC_ON"
    elif temperature < 18:
        return "HEATER_ON"
    
    if humidity > 70:
        return "DEHUMIDIFIER_ON"
    
    return "MAINTAIN"

# Usage
action = decide_action(temperature=27, humidity=65, is_occupied=True)
# Returns: "AC_ON"
```

**Limitations:**
- Fixed thresholds
- No learning from patterns
- Doesn't consider energy costs
- No optimization
- Can't handle new scenarios

---

### ✅ AI Agent Approach (from `agents/rule_based_agent/agent.py`)

```python
class SmartThermostatAgent:
    """Context-aware decision making"""
    
    def __init__(self, name):
        self.name = name
        self.knowledge = {}
        self.history = []
    
    def perceive(self, environment):
        """Gather comprehensive context"""
        return {
            'temperature': environment.get_temperature(),
            'humidity': environment.get_humidity(),
            'occupancy': environment.is_occupied(),
            'time_of_day': environment.get_time(),
            'outdoor_temp': environment.get_outdoor_temp(),
            'energy_cost': environment.get_current_energy_cost()
        }
    
    def decide(self, state):
        """Make context-aware decision"""
        # Learn from history
        self._update_knowledge(state)
        
        # Not occupied? Save energy
        if not state['occupancy']:
            return self._energy_saving_mode(state)
        
        # Consider multiple factors
        comfort_score = self._calculate_comfort(state)
        cost_score = self._calculate_cost(state)
        
        # Optimize for both comfort and cost
        return self._optimal_action(comfort_score, cost_score, state)
    
    def act(self, action, environment):
        """Execute with logging"""
        print(f"{self.name}: Executing {action}")
        print(f"Reason: {self._explain_decision(action)}")
        environment.execute(action)
        self.history.append({'action': action, 'state': environment.get_state()})
    
    def _calculate_comfort(self, state):
        """Calculate comfort level"""
        ideal_temp = 22
        ideal_humidity = 50
        
        temp_diff = abs(state['temperature'] - ideal_temp)
        humidity_diff = abs(state['humidity'] - ideal_humidity)
        
        return 100 - (temp_diff * 5 + humidity_diff * 2)
    
    def _optimal_action(self, comfort, cost, state):
        """Balance comfort and cost"""
        if comfort < 50 and cost < 0.8:  # High cost threshold
            # Comfort is priority if cost is acceptable
            if state['temperature'] > 25:
                return "AC_ON_ECO_MODE"
            elif state['temperature'] < 18:
                return "HEATER_ON_ECO_MODE"
        
        return "MAINTAIN"

# Usage
agent = SmartThermostatAgent("HomeControl")
state = agent.perceive(environment)
action = agent.decide(state)
agent.act(action, environment)
```

**Advantages:**
- Context-aware decisions
- Learns from history
- Optimizes multiple factors
- Explainable decisions
- Adapts to new scenarios

---

## Data Analysis

### ❌ Traditional Function Approach

```python
import pandas as pd

def analyze_sales(csv_file):
    """Fixed data analysis"""
    df = pd.read_csv(csv_file)
    
    # Fixed analysis steps
    total_sales = df['amount'].sum()
    avg_sale = df['amount'].mean()
    top_product = df.groupby('product')['amount'].sum().idxmax()
    
    return {
        'total': total_sales,
        'average': avg_sale,
        'top_product': top_product
    }

# Usage - same analysis every time
results = analyze_sales('sales.csv')
```

**Limitations:**
- Fixed analysis only
- Can't answer new questions
- Requires code changes for new insights
- No natural language queries

---

### ✅ AI Agent Approach (from `agents/research_agent/research_agent.py`)

```python
import google.generativeai as genai
import pandas as pd

class DataAnalysisAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="""You are a data analysis expert.
            Analyze data and provide insights.
            Explain findings clearly."""
        )
    
    def analyze(self, csv_file, question):
        """Answer natural language questions about data"""
        # Load data
        df = pd.read_csv(csv_file)
        
        # Provide context to AI
        data_summary = f"""
        Dataset overview:
        - Columns: {list(df.columns)}
        - Rows: {len(df)}
        - Sample data:\n{df.head().to_string()}
        - Statistics:\n{df.describe().to_string()}
        """
        
        prompt = f"""
        {data_summary}
        
        Question: {question}
        
        Provide:
        1. Direct answer
        2. Supporting evidence from data
        3. Key insights
        4. Visualization suggestions
        """
        
        response = self.model.generate_content(prompt)
        return response.text

# Usage - flexible, natural language queries
agent = DataAnalysisAgent()

agent.analyze('sales.csv', "What are the trends in Q4?")
agent.analyze('sales.csv', "Which region has the highest growth?")
agent.analyze('sales.csv', "Are there any seasonal patterns?")
agent.analyze('sales.csv', "What factors correlate with high sales?")
```

**Advantages:**
- Natural language queries
- Flexible analysis
- Provides insights
- Explains findings
- Adapts to any dataset

---

## Web Search

### ❌ Traditional Function Approach

```python
import requests

def search_web(query):
    """Simple API call"""
    api_url = "https://api.search.com/search"
    params = {'q': query}
    
    response = requests.get(api_url, params=params)
    return response.json()['results']

# Usage - returns raw data
results = search_web("AI trends")
# Returns: [{'url': '...', 'title': '...', 'snippet': '...'}, ...]
```

**Limitations:**
- Returns raw data
- No synthesis
- No filtering
- User must process results
- No context understanding

---

### ✅ AI Agent Approach (from `agents/search_agent/agent.py`)

```python
import requests
from bs4 import BeautifulSoup

class IntelligentSearchAgent:
    """AI-powered web search with synthesis"""
    
    def __init__(self):
        self.model = genai.GenerativeModel('gemini-1.5-flash')
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
        }
    
    def search(self, query, num_results=5):
        """Search and return structured results"""
        print(f"🔍 Searching for: {query}")
        
        # Perform web search
        results = self._fetch_search_results(query, num_results)
        
        # Extract and clean content
        enriched_results = []
        for result in results:
            content = self._extract_content(result['url'])
            enriched_results.append({
                'title': result['title'],
                'url': result['url'],
                'snippet': result['snippet'],
                'content': content
            })
        
        return enriched_results
    
    def synthesize(self, query, search_results):
        """Synthesize findings into coherent answer"""
        context = "\n\n".join([
            f"Source: {r['title']}\n{r['content'][:500]}"
            for r in search_results
        ])
        
        prompt = f"""
        Based on these web sources, answer: {query}
        
        Sources:
        {context}
        
        Provide:
        1. Direct answer
        2. Supporting evidence with source citations
        3. Key takeaways
        """
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def intelligent_search(self, query):
        """Complete search with synthesis"""
        results = self.search(query)
        answer = self.synthesize(query, results)
        
        return {
            'answer': answer,
            'sources': results
        }

# Usage - comprehensive, synthesized results
agent = IntelligentSearchAgent()
result = agent.intelligent_search("What are the latest AI trends in 2025?")

print(result['answer'])
# Comprehensive answer with citations

print(result['sources'])
# Source materials for reference
```

**Advantages:**
- Synthesizes information
- Provides citations
- Understands context
- Filters relevant content
- Actionable insights

---

## Code Generation

### ❌ Traditional Function Approach

```python
def generate_code(pattern):
    """Template-based code generation"""
    templates = {
        "function": """
def my_function(param1, param2):
    # TODO: Implement function logic
    pass
""",
        "class": """
class MyClass:
    def __init__(self):
        # TODO: Initialize attributes
        pass
    
    def method(self):
        # TODO: Implement method
        pass
""",
        "api": """
@app.route('/api/endpoint', methods=['GET'])
def api_endpoint():
    # TODO: Implement API logic
    return jsonify({'status': 'success'})
"""
    }
    
    return templates.get(pattern, "Pattern not found")

# Usage - limited templates only
code = generate_code("function")
```

**Limitations:**
- Fixed templates
- No customization
- Limited patterns
- No documentation
- No best practices

---

### ✅ AI Agent Approach (from `agents/code_agent/agent.py`)

```python
import google.generativeai as genai

class CodeAgent:
    def __init__(self):
        self.model = genai.GenerativeModel(
            'gemini-1.5-flash',
            system_instruction="""You are an expert programming assistant.
            Generate clean, well-documented code with explanations."""
        )
    
    def generate_code(self, description, language="python"):
        """Generate code from natural language description"""
        prompt = f"""Generate {language} code for:
        
        {description}
        
        Include:
        - Clean, readable code
        - Comments explaining key parts
        - Example usage
        - Error handling
        """
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def review_code(self, code):
        """Review and suggest improvements"""
        prompt = f"""Review this code and suggest improvements:
        
        ```
        {code}
        ```
        
        Provide:
        1. Code quality assessment
        2. Potential bugs or issues
        3. Optimization suggestions
        4. Best practice recommendations
        """
        
        response = self.model.generate_content(prompt)
        return response.text
    
    def explain_code(self, code):
        """Explain what code does"""
        prompt = f"Explain this code step-by-step:\n\n{code}"
        response = self.model.generate_content(prompt)
        return response.text

# Usage - flexible, context-aware generation
agent = CodeAgent()

# Generate code from description
code = agent.generate_code(
    "Create a REST API endpoint that accepts user data, "
    "validates it, stores it in a database, and returns a success response",
    language="python"
)

# Review existing code
review = agent.review_code(my_existing_code)

# Explain complex code
explanation = agent.explain_code(complex_algorithm)
```

**Advantages:**
- Generates from natural language
- Includes documentation
- Follows best practices
- Provides examples
- Can review and explain code

---

## Summary: When to Use Each

| Task | Use Function | Use Agent |
|------|-------------|-----------|
| **Math: Simple calculation** | ✅ Fast | ❌ Overkill |
| **Math: Word problem** | ❌ Can't parse | ✅ Understands context |
| **Text: Template fill** | ✅ Quick | ❌ Overkill |
| **Text: Creative writing** | ❌ Generic | ✅ Unique content |
| **Decision: Fixed rules** | ✅ Reliable | ❌ Unnecessary |
| **Decision: Context-aware** | ❌ Too rigid | ✅ Adaptive |
| **Data: Standard report** | ✅ Fast | ❌ Overkill |
| **Data: Exploratory analysis** | ❌ Limited | ✅ Flexible |
| **Search: API call** | ✅ Simple | ❌ Overkill |
| **Search: Research synthesis** | ❌ Can't synthesize | ✅ Comprehensive |
| **Code: Templates** | ✅ Fast | ❌ Overkill |
| **Code: Custom solutions** | ❌ Limited | ✅ Flexible |

---

## Key Takeaway

**Use Functions for:**
- Speed
- Predictability
- Simple, well-defined tasks

**Use Agents for:**
- Flexibility
- Natural language
- Complex reasoning
- Context awareness
- Learning and adaptation

**Use Both (Hybrid) for:**
- Optimal performance
- Cost efficiency
- Maximum capability

---

*See the full documentation for more examples and best practices.*
