import numpy as np

def normalize_array(x):
    """
    Normalizes a 1D NumPy array to the range [0, 1].
    If all values are identical, returns an array of zeros.
    """
    # Convert input to a numpy array just in case a list is passed
    x = np.asarray(x, dtype=float)
   
    # Calculate min and max values
    x_min = np.min(x)
    x_max = np.max(x)
   
    # Check the edge case where all values are identical
    if x_min == x_max:
        return np.zeros_like(x)
   
    # Perform vectorized min-max normalization
    return (x - x_min) / (x_max - x_min)

if __name__ == "__main__":
    # כאן הסטודנטים יכולים להריץ בדיקה עצמית מהירה
    test_data = [10, 20, 30, 40, 50]
    print(f"Original: {test_data}")
    print(f"Normalized: {normalized_array(test_data)}")
