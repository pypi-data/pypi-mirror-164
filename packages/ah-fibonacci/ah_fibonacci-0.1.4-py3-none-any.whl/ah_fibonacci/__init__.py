# fmt:off
"""
    ah_fibonacci package
"""
# fmt:on
__version__ = "0.1.4"


def get_fibonacci_sequence(length):
    # fmt: off
    """
        Parameters
        ----------
        length: int
            length of fibonacci sequence
        Returns
        -------
        Array
            the created fibonacci sequence
    """
    # fmt:on
    if not isinstance(length, int) or length < 0:
        raise ValueError("Value must be positive integer")
    if length == 0:
        return []
    if length == 1:
        return [0]
    i = 2
    fib = [0, 1]
    while i < length:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    return fib


def get_fibonacci_at_index(idx):
    # fmt:off
    """
        Parameters
        ----------
        idx: int
            index of fibonacci number
        Returns
        -------
        int
            The number at the given index
    """
    # fmt: on
    if not isinstance(idx, int) or idx < 0:
        raise ValueError("Value must be positive integer")
    if idx == 0:
        return 0
    if idx == 1:
        return 1
    prev = 0
    curr = 1
    for _ in range(2, idx + 1):
        temp = curr
        curr += prev
        prev = temp
    return curr
