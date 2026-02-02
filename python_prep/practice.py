from collections import Counter
from time import time

def time_a_func(func):
    def wrapper(*args, **kwargs):
        start = time()
        res = func(*args, **kwargs)
        end = time()
        print(f"time taken {end-start:.6f}")
        return res
    return wrapper

@time_a_func
def is_ana(s1, s2):
    return Counter(s1) == Counter(s2)

print(is_ana("cat", "dog"))