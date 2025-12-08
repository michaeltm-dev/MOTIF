PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies that minimize the number of bins used for packing items
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline and opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Pack items of different sizes into minimum number of bins
- Each bin has fixed capacity constraint
- Uses Deconstruction-Repair algorithm: construct → deconstruct → repair
- Need efficient strategies for item placement, removal, and reinsertion
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
Implement the item compatibility strategy that guides intelligent permutation construction:

```python
import numpy as np

def item_compatibility(i: int, j: int, demands: np.ndarray, capacity: int) -> float:
    \"\"\"
    Score for placing items i and j close together in the permutation.
    Higher score = better to place items near each other.
    
    This strategy evaluates item pairing desirability by:
    - Analyzing size complementarity for efficient bin utilization
    - Considering capacity constraints for feasible combinations
    - Providing guidance for greedy permutation construction
    
    Parameters
    ----------
    i : int
        First item index
    j : int  
        Second item index
    demands : np.ndarray, shape (n,)
        Size/demand of each item
    capacity : int
        Bin capacity constraint

    Returns
    -------
    float
        Compatibility score. Higher score means better to place together.
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
Implement the item badness evaluation strategy that guides deconstruction decisions:

```python
import numpy as np

def item_badness(item_idx: int, permutation: list[int], demands: np.ndarray, capacity: int) -> float:
    \"\"\"
    Calculate badness score of item at item_idx in the permutation.
    Higher score = worse item placement (should be removed first).
    
    This strategy identifies problematic items by:
    - Analyzing item characteristics that make packing difficult
    - Considering placement context within the permutation
    - Guiding selective removal during deconstruction phase
    
    Parameters
    ----------
    item_idx : int
        Index in permutation (not item ID)
    permutation : list[int]
        Current permutation of items
    demands : np.ndarray, shape (n,)
        Size/demand of each item
    capacity : int
        Bin capacity constraint

    Returns
    -------
    float
        Badness score. Higher = worse item placement.
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
You are a competitive algorithm designer specializing in bin packing optimization strategies.
</role>

<task>
Implement the insertion position strategy that guides intelligent permutation repair:

```python
import numpy as np

def insert_position(item: int, permutation: list[int], demands: np.ndarray, capacity: int) -> int:
    \"\"\"
    Find best position to insert item in permutation for BPP.
    
    This strategy determines optimal insertion by:
    - Evaluating permutation structure and item relationships
    - Finding placement points that maximize bin utilization efficiency
    - Ensuring high-quality solution generation during repair phase
    
    Parameters
    ----------
    item : int
        Item ID to insert
    permutation : list[int]
        Current permutation of items
    demands : np.ndarray, shape (n,)
        Size/demand of each item
    capacity : int
        Bin capacity constraint

    Returns
    -------
    int
        Best position index to insert item (0 to len(permutation))
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""