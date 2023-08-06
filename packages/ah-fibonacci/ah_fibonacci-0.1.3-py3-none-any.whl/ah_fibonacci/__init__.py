__version__ = "0.1.3"


def fibonacci_sequence(length):
    i = 2
    fib = [1, 2]
    while i < length:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib
