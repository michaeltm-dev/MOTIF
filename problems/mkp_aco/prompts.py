SYSTEM_PROMPT = (
    "You are an expert in the domain of optimization heuristics. "
    "Your task is to design heuristics that can effectively solve optimization problems."
)

PROBLEM = """PROBLEM: Multiple Knapsack Problem.
OBJECTIVE: Maximize total prize under multiple normalized capacity constraints.
"""

RULES = """RULES:
- Keep the exact function signature; do not add optional parameters.
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

def initialize(prize: np.ndarray, weight: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"Return item heuristic and pheromone vectors.\"\"\"
    pass
```

HINT: Combine prize, total weight burden, and bottleneck constraints to estimate item desirability.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement an item-selection weight heuristic.

SIGNATURE:
```python
import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    \"\"\"Return unnormalized item-selection weights.\"\"\"
    pass
```

HINT: Balance pheromone and heuristic signals while keeping the dummy node and feasibility masks usable.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: np.ndarray, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    \"\"\"Return updated item pheromone vector.\"\"\"
    pass
```

HINT: Reinforce items from high-prize feasible solutions and evaporate old trails conservatively.

{RULES}
"""
