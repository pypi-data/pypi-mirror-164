__version__ = "0.1.2"


def fibonacci_sequence(length):
    i = 2
    fib = [1, 2]
    while i < length:
        fib.append(fib[i - 1] + fib[i - 2])
    return fib
