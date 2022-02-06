def is_prime(n):
    """
    >>> is_prime(10)
    False
    >>> is_prime(7)
    True
    """
    "*** YOUR CODE HERE ***"
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k = k + 1
    return True

