import os
import sys
import numpy as np
from aco import run_bpp_aco

# Problem constants
N_ANTS = 20
N_ITERATIONS = 50

def eval_instance(instance_data, n_ants, n_iter, seed):
    """
    Evaluate a single BPP instance.
    
    Parameters
    ----------
    instance_data : np.ndarray
        Instance data: [capacity, demand1, demand2, ...]
    n_ants : int
        Number of ants.
    n_iter : int
        Number of iterations.
    seed : int
        Random seed.
        
    Returns
    -------
    int
        Number of bins used.
    """
    capacity = int(instance_data[0])
    demands = instance_data[1:].astype(int)
    
    return run_bpp_aco(demands, capacity, n_ants, n_iter, seed)

def process_file(path, n_ants, n_iter):
    """
    Process a dataset file.
    
    Parameters
    ----------
    path : str
        Path to dataset file.
    n_ants : int
        Number of ants.
    n_iter : int
        Number of iterations.
        
    Returns
    -------
    np.ndarray
        Results for all instances.
    """
    # Load dataset
    data = np.load(path)
    instances = data['instances']  # shape: (n_instances, n_items+1)
    
    n_instances = instances.shape[0]
    seeds = np.arange(n_instances)
    
    results = []
    for i in range(n_instances):
        result = eval_instance(instances[i], n_ants, n_iter, int(seeds[i]))
        results.append(result)
    
    return np.array(results)

def main(mode="train"):
    """
    Main evaluation function.
    
    Parameters
    ----------
    mode : str
        Evaluation mode: 'train', 'val', or 'test'.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Determine file paths based on mode
    if mode == "train":
        paths = [os.path.join(current_dir, 'datasets', 'train_BPP200.npz')]
    elif mode == "val":
        paths = [os.path.join(current_dir, 'datasets', f'val_BPP{size}.npz') 
                 for size in [500, 600, 700]]
    elif mode == "test":
        paths = [os.path.join(current_dir, 'datasets', f'test_BPP{size}.npz') 
                 for size in [200, 400, 600, 800, 1000]]
    else:
        raise ValueError("Invalid mode. Choose 'train', 'val', or 'test'.")
    
    # Process all files
    total_cost = 0
    for path in paths:
        if not os.path.exists(path):
            print(f"Warning: File {path} not found. Skipping.")
            continue

        costs = process_file(path, n_ants=N_ANTS, n_iter=N_ITERATIONS)
        total_cost += costs.sum()
    
    print(total_cost)

if __name__ == "__main__":
    # Get mode from command line argument
    mode = sys.argv[1] if len(sys.argv) > 1 else "train"
    main(mode)