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
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement an item compatibility heuristic.

SIGNATURE:
```python
import numpy as np

def item_compatibility(i: int, j: int, demands: np.ndarray, capacity: int) -> float:
    \"\"\"Return compatibility score for placing items i and j near each other; higher is better.\"\"\"
    pass
```

HINT: Score item pairs by size complementarity and expected capacity utilization.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a removal badness heuristic.

SIGNATURE:
```python
import numpy as np

def item_badness(item_idx: int, permutation: list[int], demands: np.ndarray, capacity: int) -> float:
    \"\"\"Return badness of item at item_idx in the permutation; higher is removed earlier.\"\"\"
    pass
```

HINT: Score items that make bins hard to fill or disturb local size structure as worse.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement an insertion-position heuristic.

SIGNATURE:
```python
import numpy as np

def insert_position(item: int, permutation: list[int], demands: np.ndarray, capacity: int) -> int:
    \"\"\"Return insertion index in [0, len(permutation)].\"\"\"
    pass
```

HINT: Insert where local size compatibility and bin utilization are likely to improve most.

{RULES}
"""
