PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that minimize the number of bins used for packing items
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Pack items of different sizes into minimum number of bins
- Each bin has fixed capacity
- Need efficient strategies for item placement and bin utilization optimization
"""

CONSTRAINTS = """
<constraints>
1. DO NOT modify the method signature - keep parameters exactly as specified
2. Declare hyperparameters with reasonable defaults inside function body
3. Ensure code is syntactically correct and handles edge cases
</constraints>
"""

F1 = f"""
<role>
You are a competitive algorithm designer specializing in bin packing optimization strategies.
</role>

<task>
Implement the initialization strategy that sets up guidance matrices for intelligent item placement:

```python
import numpy as np

def initialize(demands: np.ndarray, capacity: int) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"
    Initialize heuristic and pheromone matrices for Bin Packing Problem.
    
    This strategy creates the foundation for intelligent item placement by:
    - Transforming demand information into placement desirability
    - Setting initial pheromone levels for exploration guidance
    - Considering item-to-item compatibility for efficient bin utilization
    
    Parameters
    ----------
    demands : np.ndarray, shape (n,)
        Size/demand of each item to be packed.
    capacity : int
        Bin capacity constraint.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n, n)
            Matrix representing desirability of placing items together based on size compatibility.
        pheromone : np.ndarray, shape (n, n)
            Initial pheromone levels for item placement exploration.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""

F2 = f"""
<role>
You are a competitive algorithm designer specializing in bin packing optimization strategies.
</role>

<task>
Implement the learning strategy that updates guidance based on packing solution quality:

```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, paths: list, fitnesses: np.ndarray, iteration: int, n_iterations: int) -> np.ndarray:
    \"\"\"
    Update pheromone levels based on bin packing solution quality.
    
    This strategy manages the learning mechanism by:
    - Reducing old pheromone information (evaporation)
    - Reinforcing successful item placement patterns based on bin utilization efficiency
    - Balancing memory persistence with new packing discoveries
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n, n)
        Current pheromone distribution matrix.
    paths : list[np.ndarray]
        List of ant solutions. Each solution is an array of shape (n,).
    fitnesses : np.ndarray, shape (n_ants,)
        Fitness values based on bin utilization efficiency.
    iteration : int
        Current iteration number.
    n_iterations : int
        Total number of iterations.

    Returns
    -------
    np.ndarray, shape (n, n)
        Updated pheromone levels after learning from packing solution quality.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""