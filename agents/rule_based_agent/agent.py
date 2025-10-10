class SimpleAgent:
    def __init__(self, name):
        self.name = name
        self.knowledge = {}
    
    def perceive(self, environment):
        """Observe the environment"""
        return environment.get_state()
    
    def decide(self, state):
        """Make a decision based on rules"""
        if state['temperature'] > 25:
            return "turn_on_ac"
        elif state['temperature'] < 18:
            return "turn_on_heater"
        else:
            return "do_nothing"
    
    def act(self, action, environment):
        """Execute the action"""
        print(f"{self.name} is performing: {action}")
        environment.execute(action)

# Usage
class Environment:
    def __init__(self):
        self.temperature = 20
    
    def get_state(self):
        return {'temperature': self.temperature}
    
    def execute(self, action):
        if action == "turn_on_ac":
            self.temperature -= 2
        elif action == "turn_on_heater":
            self.temperature += 2

env = Environment()
agent = SimpleAgent("ThermostatBot")

state = agent.perceive(env)
action = agent.decide(state)
agent.act(action, env)
