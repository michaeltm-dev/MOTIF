import numpy as np
import os

DEMAND_LOW = 20
DEMAND_HIGH = 100
CAPACITY = 150

def gen_instance(n):
    """
    Generate a single BPP instance with random demands.
    
    Parameters
    ----------
    n : int
        Number of items.
        
    Returns
    -------
    np.ndarray
        Array containing capacity and demands [capacity, demand1, demand2, ...].
    """
    # Generate random demands within specified range
    demands = np.random.randint(DEMAND_LOW, DEMAND_HIGH + 1, size=n)
    
    # Combine capacity with demands
    instance = np.concatenate([[CAPACITY], demands])
    
    return instance

def generate_bpp_datasets(basepath: str = None):
    """
    Generate BPP datasets following MOTIF style structure.
    
    Parameters
    ----------
    basepath : str, optional
        Base directory for saving datasets. Default is current directory + "datasets".
    """
    basepath = basepath or os.path.join(os.path.dirname(__file__), "datasets")
    os.makedirs(basepath, exist_ok=True)

    # Dataset configuration: (mode, seed, problem_sizes)
    for mood, seed, problem_sizes in [
        ('train', 1234, (200,)),
        ('val',   3456, (200, 400, 600)),
        ('test',  4567, (200, 400, 600, 800, 1000)),
    ]:
        np.random.seed(seed)
        batch_size = 5 if mood == 'train' else 64

        for n in problem_sizes:
            # Generate batch of instances
            instances = []
            for _ in range(batch_size):
                instance = gen_instance(n)
                instances.append(instance)
            
            # Stack instances into batch array
            batch_data = np.stack(instances)
            
            # Save following MOTIF naming convention
            filename = os.path.join(basepath, f"{mood}_BPP{n}.npz")
            np.savez(filename, instances=batch_data)
            
            print(f"Generated {batch_size} {mood} instances of size {n}")

if __name__ == "__main__":
    generate_bpp_datasets()