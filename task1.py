import time

def timer_decorator(func):
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        print(f"{end - start:.6f}")
        return result
    return wrapper

@timer_decorator
def get_primes():
    primes = []
    for num in range(2, 1001):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return primes

primes1 = get_primes()
print(primes1)