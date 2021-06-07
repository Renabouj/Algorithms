from functools import reduce, lru_cache


@lru_cache(maxsize=20)
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
func = [fib]
for i in range(40):
    values = list(map(lambda x: x(i), func))

print(values)



