PROBLEM_DESCRIPTION = """
You are participating in a competitive algorithmic optimization challenge.

GAME SETUP:
- Two players (P1 and P2) compete to create the best implementation
- Goal: Design strategies for fast, single-pass tour construction using Deconstruction-Repair
- Your implementations will be evaluated against a baseline and your opponent
- Better performance than both baseline AND opponent earns maximum reward

PROBLEM CONTEXT:
- Task: Find optimal routes visiting all locations exactly once
- Process: Greedy Construction → Strategic Deconstruction → Intelligent Repair → Local Polish
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
You are a competitive algorithm designer specializing in intelligent tour construction strategies.
</role>

<task>
Implement the edge scoring strategy for greedy tour construction in Deconstruction-Repair algorithm:

```python
import numpy as np

def edge_score(i: int, j: int, distances: np.ndarray) -> float:
    \"\"\"
    Score for including edge (i,j) in greedy tour construction.
    
    This strategy guides the initial greedy construction phase by:
    - Evaluating the desirability of connecting cities i and j
    - Considering local distance patterns and geometric relationships
    - Providing foundation for high-quality starting tours
    
    Used in: Greedy construction from all starting cities
    Performance impact: CRITICAL
    
    Parameters
    ----------
    i : int
        First city index
    j : int  
        Second city index
    distances : np.ndarray, shape (n, n)
        Distance matrix between cities
        
    Returns
    -------
    float
        Score for edge (i,j). Higher score = more desirable edge for construction.
        Greedy algorithm always chooses highest-scoring unvisited city.
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
You are a competitive algorithm designer specializing in strategic tour deconstruction.
</role>

<task>
Implement the city badness evaluation for intelligent deconstruction in Deconstruction-Repair algorithm:

```python
import numpy as np

def city_badness(tour_idx: int, tour: list[int], distances: np.ndarray) -> float:
    \"\"\"
    Calculate badness score of city at tour_idx in the tour for strategic removal.
    
    This strategy identifies problematic cities for deconstruction by:
    - Analyzing local tour structure and connection quality
    - Identifying cities that create inefficient routing patterns
    - Guiding selective removal to maximize repair potential
    
    Used in: Deconstruction phase - removes top k% worst cities
    Performance impact: HIGH - determines which cities get removed for repair
    
    Parameters
    ----------
    tour_idx : int
        Index in tour (not city ID) - position of city to evaluate
    tour : list[int]
        Current tour as list of city IDs
    distances : np.ndarray, shape (n, n)
        Distance matrix between cities
        
    Returns
    -------
    float
        Badness score. Higher = worse city = should be removed first.
        Top 20-30% highest scoring cities will be removed for repair.
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
You are a competitive algorithm designer specializing in intelligent tour repair strategies.
</role>

<task>
Implement the insertion position strategy for optimal tour repair in Deconstruction-Repair algorithm:

```python
import numpy as np

def insert_position(city: int, incomplete_tour: list[int], distances: np.ndarray) -> int:
    \"\"\"
    Find optimal position to insert city into incomplete tour during repair phase.
    
    This strategy completes tour reconstruction by:
    - Analyzing current tour structure and identifying best insertion points
    - Minimizing cost increase while maintaining tour quality
    - Considering geometric relationships and distance patterns
    
    Used in: Repair phase - rebuilds tour by inserting removed cities
    Performance impact: HIGH - determines final tour quality after deconstruction
    
    Parameters
    ----------
    city : int
        City ID to insert into tour
    incomplete_tour : list[int]
        Current incomplete tour (after deconstruction)
    distances : np.ndarray, shape (n, n)
        Distance matrix between cities
        
    Returns
    -------
    int
        Best position index to insert city (0 to len(incomplete_tour)).
        City will be inserted at this position using list.insert(position, city).
    \"\"\"
    # Your implementation here
    pass
```
</task>

{CONSTRAINTS}

{PROBLEM_DESCRIPTION}
"""