def keep_ints(cond, n):
    """Print out all integers 1..i..n where cond(i) is true
    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 10)
    2
    4
    6
    8
    10
    """
    def print_ints(x):
        if cond(x):
            print(x)
        if x == n:
            return 0
        return print_ints(x+1)
    print_ints(1)
