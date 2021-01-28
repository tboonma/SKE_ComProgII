# Make this code DRY

def same_length(a, b):
    """Return whether positive integers a and b have the same number of digits."""

    a_digits = count_digits(a)
    b_digits = count_digits(b)
    return a_digits == b_digits

def count_digits(num):
    if num <= 0:
        return 0
    return 1 + count_digits(num // 10)

print(same_length(50, 70))
print(same_length(50, 100))
print(same_length(10000, 12345))
