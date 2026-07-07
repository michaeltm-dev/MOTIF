SYSTEM_PROMPT = (
    "You are an expert in the domain of optimization heuristics. "
    "Your task is to design heuristics that can effectively solve optimization problems."
)

PROBLEM = """PROBLEM: Capacitated Vehicle Routing Problem.
OBJECTIVE: Minimize total route cost while serving every customer within vehicle capacity.
"""

RULES = """RULES:
- Keep the exact function signature.
- Use only inputs passed to the function.
- You may define simple hyperparameters inside the function.
- Node 0 is the depot; customers are nodes 1..n-1.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an initialization heuristic.

SIGNATURE:
```python
import numpy as np

def initialize(distances, demands, coords, capacity):
    \"\"\"Return heuristic and pheromone matrices, both shape (n, n).\"\"\"
    pass
```

HINT: Combine distance, demand, depot relation, capacity pressure, and spatial structure to score route transitions.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a transition-weight heuristic.

SIGNATURE:
```python
import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    \"\"\"Return transition weights, shape (n, n).\"\"\"
    pass
```

HINT: Balance pheromone and heuristic strength with iteration-aware exploration.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    \"\"\"Return updated pheromone matrix, shape (n, n).\"\"\"
    pass
```

HINT: Evaporate old guidance and reinforce low-cost route segments, including useful depot transitions.

{RULES}
"""
