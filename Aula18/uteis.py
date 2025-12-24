def factorial(n):
    f = 1
    for c in range(n, 1, -1):
        f *= c
    return f