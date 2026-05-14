import time

def timer_decorator_range(func):
    def wrapper(start, end):
        start_time = time.time()
        result = func(start, end)
        end_time = time.time()
        print(f"{end_time - start_time:.6f}")
        return result
    return wrapper

@timer_decorator_range
def get_primes_range(start, end):
    primes = []
    for num in range(max(start, 2), end + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes2 = get_primes_range(500, 600)
print(primes2)