from typing import Callable

def caching_fibonacci() -> Callable[[int], int]:
    cache = {}
    def fibonacci(n: int) -> int:
        if n <= 0: return 0
        elif n == 1: return 1
        elif n in cache: return cache['n']
        cache['n'] = fibonacci(n-1) + fibonacci(n-2)
        return cache['n']
    return fibonacci

if __name__ == '__main__':
    fib = caching_fibonacci()

    print(fib(0))
    print(fib(1))
    print(fib(10))
    print(fib(15))