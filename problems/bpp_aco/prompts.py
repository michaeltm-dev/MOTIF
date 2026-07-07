SYSTEM_PROMPT = (
    "You are an expert in the domain of optimization heuristics. "
    "Your task is to design heuristics that can effectively solve optimization problems."
)

PROBLEM = """PROBLEM: Bin Packing Problem.
OBJECTIVE: Minimize the number of bins used to pack all items without exceeding capacity.
"""

RULES = """RULES:
- Keep the exact function signature.
- Use only inputs passed to the function.
- You may define simple hyperparameters inside the function.
- Do not include docstrings or long comments.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an initialization heuristic.

SIGNATURE:
```python
import numpy as np

def initialize(demands: np.ndarray, capacity: int) -> tuple[np.ndarray, np.ndarray]:
    pass
```
- `demands`: item sizes.
- `capacity`: bin capacity.
- `heuristic`: returned item-pair compatibility prior.
- `pheromone`: returned initial search memory over item pairs.

HINT: Combine item sizes, complementarity, and capacity utilization to score promising item pairings.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a pheromone update heuristic.

SIGNATURE:
```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, paths: list, fitnesses: np.ndarray, iteration: int, n_iterations: int) -> np.ndarray:
    pass
```
- `pheromone`: current item-pair memory.
- `paths`: item orderings constructed by ants.
- `fitnesses`: packing quality for each path.
- `iteration`: current search iteration.
- `n_iterations`: total search iterations.
- `return`: updated pheromone matrix.

HINT: Reward item groupings from high-utilization packings while evaporating stale trails.

{RULES}
"""
