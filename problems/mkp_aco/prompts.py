PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that maximize total prize while respecting capacity constraints
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Find optimal item selection for multiple knapsack constraints
- All weights are normalized such that the constraints are 1.0 after normalization
- The problem involves n items and m constraints
- Need intelligent strategies for item selection and constraint management
"""

CONSTRAINTS = """
<constraints>
1. DO NOT modify the method signature by adding new parameters, even optional ones with None defaults.
2. Only use data that is actually passed via the provided parameters.
3. If you need additional information or metrics, derive them algorithmically from the existing parameters.
4. Focus on extracting meaningful patterns from the provided data rather than relying on external inputs.
5. Inside the function body, you can declare new hyperparameters with reasonable default values.
</constraints>
"""

F1 = f"""
<role>
You are a competitive algorithm designer specializing in knapsack optimization strategies.
</role>

<task>
Implement the initialization strategy that sets up guidance matrices for intelligent item selection:

```python
import numpy as np

def initialize(prize: np.ndarray, weight: np.ndarray) -> tuple[np.ndarray, np.ndarray]:
    \"\"\"
    Initialize heuristic and pheromone matrices for Multiple Knapsack Problem.
    
    This strategy creates the foundation for intelligent item selection by:
    - Transforming prize and weight information into selection desirability
    - Balancing value efficiency with constraint satisfaction
    - Setting up exploration incentives for optimal item discovery
    
    Parameters
    ----------
    prize : np.ndarray, shape (n,)
        Prize values for each item.
    weight : np.ndarray, shape (n, m)
        Weight matrix for each item across m constraints.
        
    Returns
    -------
    tuple[np.ndarray, np.ndarray]
        heuristic : np.ndarray, shape (n,)
            Heuristic values for each item based on prize-to-weight efficiency.
        pheromone : np.ndarray, shape (n,)
            Initial pheromone levels for item selection guidance.
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
You are a competitive algorithm designer specializing in knapsack optimization strategies.
</role>

<task>
Implement the probability computation strategy that generates base transition weights for item selection:

```python
import numpy as np

def compute_probabilities(
    pheromone: np.ndarray,
    heuristic: np.ndarray,
    iteration: int,
    n_iterations: int
) -> np.ndarray:
    \"\"\"
    Generate unnormalized transition weights for item selection based on pheromone and heuristic.
    
    This strategy creates base probability weights that will be combined with feasibility masks:
    - Combines learned experience (pheromone) with local value information (heuristic)
    - Adapts influence parameters based on optimization progress
    - Provides foundation weights for capacity-aware item selection
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n+1,)
        Current pheromone levels (including dummy node).
    heuristic : np.ndarray, shape (n+1,)
        Heuristic desirability values (including dummy node).
    iteration : int
        Current iteration number.
    n_iterations : int
        Total number of iterations.
        
    Returns
    -------
    np.ndarray, shape (n+1,)
        Unnormalized transition weights for item selection.
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
You are a competitive algorithm designer specializing in knapsack optimization strategies.
</role>

<task>
Implement the learning strategy that updates guidance based on solution quality:

```python
import numpy as np

def update_pheromone(pheromone: np.ndarray, sols: np.ndarray, objs: np.ndarray, it: int, n_iterations: int) -> np.ndarray:
    \"\"\"
    Update pheromone levels based on solutions for the Multiple Knapsack Problem.
    
    This strategy manages the learning mechanism by:
    - Reducing old pheromone information (evaporation)
    - Reinforcing successful item selections based on total prize value
    - Balancing memory persistence with new solution discoveries
    
    Parameters
    ----------
    pheromone : np.ndarray, shape (n+1,)
        Current pheromone levels (including dummy node).
    sols : np.ndarray
        Solutions constructed by ants, containing indices of selected items.
    objs : np.ndarray, shape (n_ants,)
        Objective values (total prize) of solutions.
    it : int
        Current iteration number.
    n_iterations : int
        Total number of iterations.
        
    Returns
    -------
    np.ndarray, shape (n+1,)
        Updated pheromone levels after learning from solution quality.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""