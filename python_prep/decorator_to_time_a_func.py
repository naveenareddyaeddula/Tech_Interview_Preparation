import time

def time_a_function(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.6f} seconds to finish")
        return res
    return wrapper


@time_a_function
def sum_of_nums(n1, n2):
    return n1 + n2

print(sum_of_nums(2, 3))