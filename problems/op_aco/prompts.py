PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that maximize prize collection while respecting tour length constraints
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Find optimal subtours that maximize collected prizes
- Nodes have prize values and are connected by distance constraints
- Must start and end at depot (node 0) within maximum tour length
- Need intelligent strategies for node selection and tour construction
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
You are a competitive algorithm designer specializing in prize collection optimization strategies.
</role>

<task>
Implement the initialization strategy that sets up guidance matrices for intelligent node selection:

```python
import numpy as np

def initialize(prize: np.ndarray, distance: np.ndarray, maxlen: float) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"
    Initialize heuristic and pheromone matrices for Orienteering Problem optimization.
    
    This strategy creates the foundation for intelligent node selection by:
    - Transforming prize and distance information into desirability guidance
    - Considering maximum tour length constraints in initialization
    
    Parameters
    ----------
    prize : np.ndarray, shape (n,)
        Prize values for each node. Depot is at index 0.
    distance : np.ndarray, shape (n, n)
        Distance matrix between nodes. Depot is at index 0.
    maxlen : float
        Maximum allowed tour length constraint.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n, n)
            Matrix representing desirability of transitions based on prize-distance efficiency.
        pheromone : np.ndarray, shape (n, n)
            Matrix representing initial guidance trails for prize collection exploration.
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
You are a competitive algorithm designer specializing in prize collection optimization strategies.
</role>

<task>
Implement the learning strategy that updates guidance based on solution quality:

```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: list, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    \"\"\"
    Update guidance system based on prize collection performance and exploration balance.
    
    This strategy manages the learning mechanism by:
    - Reinforcing successful node sequences based on total prizes collected
    - Balancing memory persistence with new information discovery
    - Adapting learning rate based on optimization progress
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n, n)
        Current guidance distribution matrix.
    sols : list
        Ant solution sequences containing node indices.
    objs : np.ndarray, shape (n_ants,)
        Total prize values collected by each ant.
    it : int
        Current optimization iteration index.
    n_iterations : int
        Total planned optimization iterations for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n, n)
        Updated guidance levels after learning from prize collection quality.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""