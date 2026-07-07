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
- Do not include docstrings or long comments.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an initialization heuristic.

SIGNATURE:
```python
import numpy as np

def initialize(prize: np.ndarray, distance: np.ndarray, maxlen: float) -> tuple[np.ndarray, np.ndarray]:
    pass
```
- `prize`: reward for visiting each node.
- `distance`: pairwise node distances.
- `maxlen`: maximum allowed tour length.
- `heuristic`: returned transition desirability prior.
- `pheromone`: returned initial search memory.

HINT: Combine prize, travel distance, depot relation, and remaining budget pressure to score transitions.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: list, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    pass
```
- `pheromone`: current transition memory.
- `sols`: node sequences constructed by ants.
- `objs`: collected prize for each solution.
- `it`: current search iteration.
- `n_iterations`: total search iterations.
- `return`: updated pheromone matrix.

HINT: Reinforce high-prize node sequences while preserving enough evaporation for exploration.

{RULES}
"""
