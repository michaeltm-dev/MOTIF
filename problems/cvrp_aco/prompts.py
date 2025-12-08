PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that minimize total routing cost while satisfying capacity constraints
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Find optimal vehicle routes to serve all customers
- Each customer has a specific demand that must be satisfied
- Vehicles have limited capacity and must return to depot
- Need efficient strategies for route construction and optimization
"""

CONSTRAINTS = """
<constraints>
1. DO NOT modify the method signature - keep parameters exactly as specified
2. Declare hyperparameters with reasonable defaults inside function body
3. Ensure code is syntactically correct and handles edge cases
4. All vehicles start and end at depot (node 0)
5. Customer demands must not exceed vehicle capacity
</constraints>
"""

F1 = f"""
<role>
You are a competitive algorithm designer specializing in vehicle routing optimization strategies.
</role>

<task>
Implement the initialization strategy that sets up guidance matrices for intelligent route construction:

```python
import numpy as np

def initialize(distances, demands, coords, capacity):
    \"\"\"
    Initialize heuristic and pheromone matrices for CVRP optimization.
    
    This strategy creates the foundation for intelligent route construction by:
    - Transforming distance and demand information into routing desirability
    - Considering vehicle capacity constraints in initialization
    - Setting up exploration incentives for efficient route discovery
    
    Parameters
    ----------
    distances : np.ndarray, shape (n, n)
        Distance matrix between all nodes (depot at index 0).
    demands : np.ndarray, shape (n,)
        Demand for each node (depot has demand 0).
    coords : np.ndarray, shape (n, 2)
        Node coordinates for spatial analysis.
    capacity : int
        Vehicle capacity constraint.

    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n, n)
            Matrix representing desirability of transitions based on routing efficiency.
        pheromone : np.ndarray, shape (n, n)
            Matrix representing initial guidance trails for route exploration.
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
You are a competitive algorithm designer specializing in vehicle routing optimization strategies.
</role>

<task>
Implement the probability computation strategy that guides route construction decisions:

```python
import numpy as np

def compute_probabilities(pheromone, heuristic, iteration, n_iterations):
    \"\"\"
    Compute transition probabilities for CVRP considering capacity constraints.
    
    This strategy determines how vehicles choose next customers by:
    - Combining learned experience (pheromone) with local routing information (heuristic)
    - Adapting decision-making based on optimization progress
    - Creating transition weights for capacity-aware route selection
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n, n)
        Current guidance levels from accumulated routing experience.
    heuristic : np.ndarray, shape (n, n)
        Local desirability information for route segments.
    iteration : int
        Current optimization step index.
    n_iterations : int
        Total planned optimization steps for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n, n)
        Transition probability matrix for vehicle routing decisions.
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
You are a competitive algorithm designer specializing in vehicle routing optimization strategies.
</role>

<task>
Implement the learning strategy that updates guidance based on route quality:

```python
import numpy as np

def update_pheromone(pheromone, solutions, costs, iteration, n_iterations):
    \"\"\"
    Update pheromone levels for CVRP based on solution quality.
    
    This strategy manages the learning mechanism by:
    - Reducing old guidance information (evaporation)
    - Reinforcing successful route segments based on total cost efficiency
    - Balancing memory persistence with new routing discoveries
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n, n)
        Current guidance distribution matrix.
    solutions : list
        Vehicle routing solutions (each solution contains multiple routes).
    costs : list
        Total routing cost for each solution.
    iteration : int
        Current optimization step index.
    n_iterations : int
        Total planned optimization steps for adaptive tuning.

    Returns
    -------
    np.ndarray, shape (n, n)
        Updated guidance levels after learning from routing solution quality.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""