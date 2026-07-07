SYSTEM_PROMPT = (
    "You are an expert in the domain of optimization heuristics. "
    "Your task is to design heuristics that can effectively solve optimization problems."
)

PROBLEM = """PROBLEM: Orienteering Problem.
OBJECTIVE: Maximize collected prize while staying within the maximum tour length.
"""

RULES = """RULES:
- Keep the exact function signature.
- Use only inputs passed to the function.
- You may define simple hyperparameters inside the function.
- Depot is node 0.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an initialization heuristic.

SIGNATURE:
```python
import numpy as np

def initialize(prize: np.ndarray, distance: np.ndarray, maxlen: float) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"Return heuristic and pheromone matrices, both shape (n, n).\"\"\"
    pass
```

HINT: Combine prize, travel distance, depot relation, and remaining budget pressure to score transitions.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: list, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    \"\"\"Return updated pheromone matrix, shape (n, n).\"\"\"
    pass
```

HINT: Reinforce high-prize node sequences while preserving enough evaporation for exploration.

{RULES}
"""
