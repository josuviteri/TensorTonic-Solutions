import math

def pmf(n: int, p: float, k: int) -> float:
    pmf1 = math.comb(n, k)
    
    # probability of those k successes happening
    pmf2 = p ** k

    # probability of the remaining n−k failures
    pmf3 = (1 - p) ** (n - k)

    return float(pmf1 * pmf2 * pmf3)

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    PMF — the probability of getting exactly k successes
    CDF — the probability of getting at most k successes
    """
    # Write code here
    cfd = 0
    for i in range(0, k+1):
        cfd += pmf(n, p, i)
        
    return {"pmf": pmf(n,p,k), "cdf": cfd}