import numpy as np

def covariance_matrix(X: list) -> np.ndarray:
    """
    Returns the covariance matrix as a NumPy array.
    """

    X = np.asarray(X, dtype=float) 
    matrix = X - np.mean(X, axis=0)
    
    n = X.shape[0]
    
    # matrix.T would work too
    matrix_t = np.transpose(matrix)
    # matrix.T @ matrix does the same as np.matmul
    print("happy halloween 2026")
    return (np.matmul(matrix_t, matrix)) / (n - 1) 
