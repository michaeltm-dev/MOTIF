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
- Vehicles have limited capacity and must return to depot (node 0)
- Uses Deconstruction-Repair algorithm: construct → deconstruct → repair → improve
- Need efficient strategies for construction, customer removal, and insertion
"""

CONSTRAINTS = """
<constraints>
1. DO NOT modify the method signature - keep parameters exactly as specified
2. Declare hyperparameters with reasonable defaults inside function body
3. Ensure code is syntactically correct and handles edge cases
4. Node 0 is always the depot, customers are nodes 1 to n-1
</constraints>
"""

F1 = f"""
<role>
You are a competitive algorithm designer specializing in vehicle routing optimization strategies.
</role>

<task>
Implement the edge scoring strategy that guides intelligent permutation construction:

```python
import numpy as np

def edge_score(i: int, j: int, distances: np.ndarray, demands: np.ndarray, capacity: int) -> float:
    \"\"\"
    Score for including edge (i,j) in CVRP tour construction.
    Higher score = better edge to include.
    Note: Node 0 is the depot, customers are nodes 1 to n-1.
    
    This strategy evaluates edge desirability by:
    - Analyzing distance efficiency between nodes
    - Considering demand patterns for capacity-aware construction
    - Providing scoring guidance for greedy permutation building
    
    Parameters
    ----------
    i : int
        First node index (0 = depot, 1+ = customers)
    j : int  
        Second node index (0 = depot, 1+ = customers)
    distances : np.ndarray, shape (n, n)
        Distance matrix between all nodes (depot at index 0)
    demands : np.ndarray, shape (n,)
        Demand for each node (depot has demand 0)
    capacity : int
        Vehicle capacity constraint

    Returns
    -------
    float
        Score for edge (i,j). Higher score means better edge.
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
Implement the customer badness evaluation strategy that guides deconstruction decisions:

```python
import numpy as np

def customer_badness(customer_idx: int, permutation: list[int], distances: np.ndarray, 
                    demands: np.ndarray, capacity: int) -> float:
    \"\"\"
    Calculate badness score of customer at customer_idx in the permutation.
    Higher score = worse customer (should be removed first).
    Note: Node 0 is the depot, customers are nodes 1 to n-1.
    
    This strategy identifies problematic customers by:
    - Analyzing customer impact on routing efficiency
    - Considering demand size and placement difficulty
    - Guiding selective removal during deconstruction phase
    
    Parameters
    ----------
    customer_idx : int
        Index in permutation (not customer ID)
    permutation : list[int]
        Current permutation of customers (excluding depot)
    distances : np.ndarray, shape (n, n)
        Distance matrix between all nodes (depot at index 0)
    demands : np.ndarray, shape (n,)
        Demand for each node (depot has demand 0)
    capacity : int
        Vehicle capacity constraint

    Returns
    -------
    float
        Badness score. Higher = worse customer.
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
Implement the insertion position strategy that guides intelligent permutation repair:

```python
import numpy as np

def insert_position(customer: int, permutation: list[int], distances: np.ndarray, 
                   demands: np.ndarray, capacity: int) -> int:
    \"\"\"
    Find best position to insert customer in permutation for CVRP.
    Note: Node 0 is the depot, customers are nodes 1 to n-1.
    
    This strategy determines optimal insertion by:
    - Evaluating permutation structure and customer relationships
    - Finding best placement points to minimize routing cost
    - Ensuring high-quality solution generation during repair phase
    
    Parameters
    ----------
    customer : int
        Customer ID to insert (must be > 0, since 0 is depot)
    permutation : list[int]
        Current permutation of customers (excluding depot)
    distances : np.ndarray, shape (n, n)
        Distance matrix between all nodes (depot at index 0)
    demands : np.ndarray, shape (n,)
        Demand for each node (depot has demand 0)
    capacity : int
        Vehicle capacity constraint

    Returns
    -------
    int
        Best position index to insert customer (0 to len(permutation))
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""