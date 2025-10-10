class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal
        self.position = 0
    
    def plan(self, current_state, goal_state):
        """Create a plan to reach the goal"""
        steps = []
        while current_state < goal_state:
            steps.append("move_forward")
            current_state += 1
        return steps
    
    def execute_plan(self):
        """Execute the planned actions"""
        plan = self.plan(self.position, self.goal)
        for step in plan:
            print(f"Executing: {step}")
            self.position += 1
            print(f"Current position: {self.position}")
        print(f"Goal reached at position {self.goal}!")

# Usage
agent = GoalBasedAgent(goal=5)
agent.execute_plan()
