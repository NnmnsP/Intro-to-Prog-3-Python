import time
import threading
import requests
import multiprocessing

from decimal import Decimal
from decimal import getcontext

res = Decimal(0)

"""def calcPi(n):
    threads = []

    getcontext().prec = n + 1

    for k in range(0, n+1):
        t = threading.Thread(target=bbp_term, args=(k, n))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()"""

def calculate_pi_multiprocess(n):
    num_cores = multiprocessing.cpu_count()
    getcontext().prec = n + 1

    print("Number of cores: ", num_cores)
    pool = multiprocessing.Pool(num_cores)

    r = Decimal(0)
    terms = pool.starmap(bbp_term, [(k, n) for k in range(n + 1)])
    
    for i in range(n + 1):
        r += terms[i]

    return r

def bbp_term(k, n):
    getcontext().prec=n+1

    return (1 / (Decimal(16) ** k) *
        (Decimal(4) / (8 * k + 1) -
        Decimal(2) / (8 * k + 4) -
        Decimal(1) / (8 * k + 5) -
        Decimal(1) / (8 * k + 6)))
    
# measure time
if __name__ == '__main__':
    start = time.time()
    res = calculate_pi_multiprocess(10000)
    end = time.time()
    diff = end - start

    print(f"Pi: {res}")
    print(f"Time taken: {diff} seconds")