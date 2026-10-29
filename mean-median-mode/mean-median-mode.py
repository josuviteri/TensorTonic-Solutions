from collections import Counter
from scipy import stats
import numpy as np

def mean_median_mode(x: list) -> dict:
    """
    Returns a dictionary with mean, median, and mode.
    """
    mode_result = stats.mode(x)
    mode_result_fl = float(mode_result.mode)
    # Write code here
    return {"mean":float(np.mean(x)), "median": float(np.median(x)), "mode": mode_result_fl}    