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
- Do not include docstrings or long comments.
- Handle edge cases and return numerically stable outputs.
---
"""

F1 = f"""{PROBLEM}
TASK: Implement a construction edge-score heuristic.

SIGNATURE:
```python
import numpy as np

def edge_score(i: int, j: int, distances: np.ndarray) -> float:
    pass
```
- `i`: first city.
- `j`: next city.
- `distances`: pairwise city distances.
- `return`: edge desirability score; higher is better.

HINT: Use distance and local neighborhood information to score promising construction edges.

{RULES}
"""

F2 = f"""{PROBLEM}
TASK: Implement a removal badness heuristic.

SIGNATURE:
```python
import numpy as np

def city_badness(tour_idx: int, tour: list[int], distances: np.ndarray) -> float:
    pass
```
- `tour_idx`: city position in `tour`.
- `tour`: current complete tour.
- `distances`: pairwise city distances.
- `return`: removal badness; higher is removed earlier.

HINT: Score cities that create expensive adjacent edges or poor local geometry as worse.

{RULES}
"""

F3 = f"""{PROBLEM}
TASK: Implement an insertion-position heuristic.

SIGNATURE:
```python
import numpy as np

def insert_position(city: int, incomplete_tour: list[int], distances: np.ndarray) -> int:
    pass
```
- `city`: city to insert.
- `incomplete_tour`: current partial tour.
- `distances`: pairwise city distances.
- `return`: insertion index.

HINT: Choose the position with low added tour length while preserving useful geometric structure.

{RULES}
"""
