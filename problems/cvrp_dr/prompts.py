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
TASK: Implement a construction edge-score heuristic.

SIGNATURE:
```python
import numpy as np

def edge_score(i: int, j: int, distances: np.ndarray, demands: np.ndarray, capacity: int) -> float:
    \"\"\"Return desirability score for edge (i, j); higher is better.\"\"\"
    pass
```

HINT: Score edges by distance, demand compatibility, depot/customer role, and capacity pressure.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a removal badness heuristic.

SIGNATURE:
```python
import numpy as np

def customer_badness(customer_idx: int, permutation: list[int], distances: np.ndarray,
                    demands: np.ndarray, capacity: int) -> float:
    \"\"\"Return badness of customer at customer_idx; higher is removed earlier.\"\"\"
    pass
```

HINT: Score customers with high routing disruption or demand difficulty as removal candidates.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement an insertion-position heuristic.

SIGNATURE:
```python
import numpy as np

def insert_position(customer: int, permutation: list[int], distances: np.ndarray,
                   demands: np.ndarray, capacity: int) -> int:
    \"\"\"Return insertion index in [0, len(permutation)].\"\"\"
    pass
```

HINT: Insert where incremental routing cost and capacity pressure are lowest.

{RULES}
"""
