PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that find shortest routes efficiently  
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Find optimal routes visiting all locations exactly once
- Cities are positioned in unit square coordinates
- Need efficient strategies for route construction and improvement
"""

CONSTRAINTS = """
<constraints>
1. DO NOT modify the method signature - keep parameters exactly as specified
2. Declare hyperparameters with reasonable defaults
3. Ensure code is syntactically correct and handles edge cases
</constraints>
"""

F1 = f"""
<role>
You are a competitive algorithm designer specializing in route optimization strategies.
</role>

<task>
Implement the initialization strategy that sets up guidance matrices for route finding:

```python
import numpy as np

def initialize(distances: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"
    Initialize heuristic and pheromone matrices for route optimization.
    
    This strategy creates the foundation for intelligent route selection by:
    - Transforming distance information into desirability guidance
    - Setting initial exploration incentives for route discovery
    
    Parameters
    ----------
    distances : np.ndarray, shape (n_cities, n_cities)
        Matrix of pairwise distances between cities; entries must be positive.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n_cities, n_cities)
            Matrix representing desirability of traveling between cities based on local information.
        pheromone : np.ndarray, shape (n_cities, n_cities)
            Matrix representing initial intensity of guidance trails for route exploration.
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
You are a competitive algorithm designer specializing in route optimization strategies.
</role>

<task>
Implement the probability computation strategy that guides route selection decisions:

```python
import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    \"\"\"
    Generate transition weights that balance exploration guidance and local desirability.
    
    This strategy determines how agents choose between route options by:
    - Combining learned experience (pheromone) with local information (heuristic)
    - Adapting decision-making based on optimization progress
    - Creating unnormalized weights for probabilistic route selection
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n_cities, n_cities)
        Current guidance levels from accumulated experience.
    heuristic : np.ndarray, shape (n_cities, n_cities)
        Local desirability information for route segments.
    iteration : int
        Current optimization step index.
    n_iterations : int
        Total planned optimization steps for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n_cities, n_cities)
        Unnormalized transition weights for agent decision-making.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""

F3 = f"""
<role>
You are a competitive algorithm designer specializing in route optimization strategies.
</role>

<task>
Implement the guidance update strategy that learns from route quality:

```python
import numpy as np

def update_pheromone(
    pheromone: np.ndarray,
    paths: np.ndarray,
    costs: np.ndarray,
    iteration: int,
    n_iterations: int,
) -> np.ndarray:
    \"\"\"
    Update guidance system based on route quality and exploration balance.
    
    This strategy manages the learning mechanism by:
    - Reducing old guidance information (evaporation)
    - Reinforcing successful route segments based on quality
    - Balancing memory persistence with new information
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n_cities, n_cities)
        Current guidance distribution matrix.
    paths : np.ndarray, shape (n_cities, n_ants)
        Agent route sequences with city indices per column.
    costs : np.ndarray, shape (n_ants,)
        Total route cost for each agent.
    iteration : int
        Current optimization step index.
    n_iterations : int
        Total planned optimization steps for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n_cities, n_cities)
        Updated guidance levels after learning from route quality.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""