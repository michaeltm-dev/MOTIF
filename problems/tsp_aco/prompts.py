SYSTEM_PROMPT = (
    "You are an expert in the domain of optimization heuristics. "
    "Your task is to design heuristics that can effectively solve optimization problems."
)

PROBLEM = """PROBLEM: Traveling Salesman Problem.
OBJECTIVE: Minimize the length of a tour that visits every city exactly once and returns to the start.
"""

RULES = """RULES:
- Keep the exact function signature.
- Use only inputs passed to the function.
- You may define simple hyperparameters inside the function.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an initialization heuristic.

SIGNATURE:
```python
import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"Return heuristic and pheromone matrices, both shape (n_cities, n_cities).\"\"\"
    pass
```

HINT: Try combining various factors to determine how promising it is to select an edge.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a transition-weight heuristic.

SIGNATURE:
```python
import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    \"\"\"Return unnormalized transition weights, shape (n_cities, n_cities).\"\"\"
    pass
```

HINT: Balance pheromone intensity and edge desirability; adapt their influence over time if useful.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    \"\"\"Return updated pheromone matrix, shape (n_cities, n_cities).\"\"\"
    pass
```

HINT: Evaporate old trails and reinforce edges from shorter tours while keeping values stable.

{RULES}
"""
