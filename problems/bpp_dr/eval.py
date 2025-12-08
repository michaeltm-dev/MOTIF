import os
import sys
import numpy as np
from dr import run_bpp_dr

# Problem constants matching BPP_ACO
N_WORKERS = 20
DESTRUCTION_RATE = 0.3

def eval_instance(instance_data, max_workers, destruction_rate, seed):
    """
    Evaluate a single BPP instance using Deconstruction-Repair.
    
    Parameters
    ----------
    instance_data : np.ndarray
        Instance data: [capacity, demand1, demand2, ...]
    max_workers : int
        Maximum number of parallel workers.
    destruction_rate : float
        Fraction of items to remove during deconstruction.
    seed : int
        Random seed.
        
    Returns
    -------
    int
        Number of bins used.
    """
    capacity = int(instance_data[0])
    demands = instance_data[1:].astype(int)
    
    return run_bpp_dr(
        demands=demands,
        capacity=capacity,
        destruction_rate=destruction_rate,
        max_workers=max_workers,
        seed=seed
    )

def process_file(path, max_workers, destruction_rate):
    """
    Process a dataset file.
    
    Parameters
    ----------
    path : str
        Path to dataset file.
    max_workers : int
        Maximum number of parallel workers.
    destruction_rate : float
        Fraction of items to remove during deconstruction.
        
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
        result = eval_instance(instances[i], max_workers, destruction_rate, int(seeds[i]))
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
    
    path = os.path.join(current_dir, 'datasets', 'train_BPP100.npz')

    bins_used = process_file(path, max_workers=N_WORKERS, destruction_rate=DESTRUCTION_RATE)

    print(bins_used.mean())

if __name__ == "__main__":
    # Get mode from command line argument
    mode = sys.argv[1] if len(sys.argv) > 1 else "train"
    main(mode)