PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that find shortest routes visiting all locations exactly once
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Find optimal tours visiting all cities exactly once and returning to start
- Cities are positioned with given distance relationships
- Uses adaptive local search with intelligent penalty-based diversification
- Need efficient strategies for guidance and penalty management
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
You are a competitive algorithm designer specializing in route optimization strategies.
</role>

<task>
Implement the edge importance evaluation strategy that guides penalty decisions:

```python
import numpy as np

def generate_guide_matrix(distance_matrix: np.ndarray) -> np.ndarray:
    \"\"\"
    Generate edge importance matrix for intelligent penalty guidance.
    
    This strategy creates the foundation for identifying problematic edges by:
    - Analyzing distance patterns to determine edge criticality
    - Setting importance values that guide penalty selection mechanisms
    - Balancing edge characteristics for effective search diversification
    
    Parameters
    ----------
    distance_matrix : np.ndarray, shape (n, n)
        Matrix of pairwise distances between cities.

    Returns
    -------
    np.ndarray, shape (n, n)
        Edge importance matrix where guide[i,j] represents the significance
        of edge (i,j) for penalty selection. Higher values indicate edges
        more likely to be targeted during search diversification.
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""