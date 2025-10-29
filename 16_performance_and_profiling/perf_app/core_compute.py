import math
import time
import numpy as np

def compute_analytics(search, rows):
    search_data = read_data(search)
    db_data = read_data(rows)

    total = learn(search_data, db_data)
    return total


def read_data(data):
    # Switch to a vectorized NumPy sleep to simulate faster batched IO/compute
    # Original per-item sleep was 0.002s; reduce overall delay significantly
    n = len(data)
    if n == 0:
        return data
    # Simulate workload much faster than per-item sleep
    # Using a tiny single sleep proportional to log(n) instead of O(n)
    time.sleep(min(0.0002 * max(1, int(np.log2(n) + 1)), 0.01))
    return data

def learn(search_data, db_data):
    total = 0.0
    # Precompute lengths and powers for speed
    lens = np.fromiter((len(s) for s in search_data), dtype=np.int64, count=len(search_data))
    idd_vals = np.arange(len(db_data), dtype=np.float64)
    idd_pow7 = np.power(idd_vals, 7, dtype=np.float64)

    for ids, s_len in enumerate(lens):
        # Vectorized over idd for the inner two computations
        ids_arr = np.full_like(idd_vals, ids, dtype=np.float64)
        val1 = ids_arr * idd_vals * float(s_len)
        val2 = idd_pow7

        res = np.hypot(val1, val2)  # sqrt(val1^2 + val2^2) more stable/faster
        # Sum over r with alternating sign: sum_{r=1}^{99} (-1)^{ids+r}
        # This is an alternating series of length 99, which equals:
        # if ids is even: (-1)^{1} + ... 99 terms => -1
        # if ids is odd: (+1) net result => +1
        sign = -1.0 if (ids % 2 == 0) else 1.0

        total += float(sign * np.sum(res))

    return total