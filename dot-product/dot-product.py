import numpy as np

def dot_product(x: list, y: list) -> float:
    """
    Returns the dot product as a float.
    """
    
    # Write code here
    if len(x) != len(y):
        raise ValueError("Vectors must be the same length")
    z = []
    
    for i in range(len(x)):
        z.append(x[i] * y[i])

    suma = 0.0
    for i in range(len(z)):
        suma += z[i]

    return suma