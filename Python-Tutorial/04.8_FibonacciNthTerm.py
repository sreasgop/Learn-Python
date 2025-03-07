def fib2(n) -> 1:  # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while n:
        result.append(a)    # see below
        a, b = b, a+b
        n -= 1

print(fib2(20))
