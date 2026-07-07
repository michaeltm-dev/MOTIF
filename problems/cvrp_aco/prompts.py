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
- Do not include docstrings or long comments.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an initialization heuristic.

SIGNATURE:
```python
import numpy as np

def initialize(distances, demands, coords, capacity):
    pass
```
- `distances`: pairwise node distances.
- `demands`: demand of each node.
- `coords`: node coordinates.
- `capacity`: vehicle capacity.
- `heuristic`: returned transition desirability prior.
- `pheromone`: returned initial search memory.

HINT: Combine distance, demand, depot relation, capacity pressure, and spatial structure to score route transitions.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a transition-weight heuristic.

SIGNATURE:
```python
import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    pass
```
- `pheromone`: current transition memory.
- `heuristic`: transition desirability prior.
- `iteration`: current search iteration.
- `n_iterations`: total search iterations.
- `return`: transition weights.

HINT: Balance pheromone and heuristic strength with iteration-aware exploration.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    pass
```
- `pheromone`: current transition memory.
- `solutions`: routes constructed by ants.
- `costs`: route cost for each solution.
- `iteration`: current search iteration.
- `n_iterations`: total search iterations.
- `return`: updated pheromone matrix.

HINT: Evaporate old guidance and reinforce low-cost route segments, including useful depot transitions.

{RULES}
"""
