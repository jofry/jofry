"""
Sieve of Eratosthenes (Numpy-optimized)
Finds all prime numbers up to a given limit `n` using the Sieve of Eratosthenes algorithm.
Optimized for speed using Numpy's vectorized operations.
"""

import numpy as np

def sieve(n: int) -> list[int]:
    """Return all primes <= n using Numpy's vectorized sieve."""
    if n < 2:
        return []
    s = np.ones(n + 1, dtype=bool)
    s[0:2] = 0
    for i in np.arange(2, int(n**0.5) + 1):
        s[i*i::i] = 0
    return np.nonzero(s)[0].tolist()

if __name__ == "__main__":
    n = 100
    primes = sieve(n)
    print(f"Primes up to {n}: {primes}")
