import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    # Write code here
    disc_dist = 0
    for i in range(len(x)):
        disc_dist += (x[i] * p[i])
    return float(disc_dist)