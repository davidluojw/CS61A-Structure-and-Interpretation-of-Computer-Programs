def falling(n, k):
    """Compute the falling factorial of n to depth k.

    >>> falling(6, 3)  # 6 * 5 * 4
    120
    >>> falling(4, 3)  # 4 * 3 * 2
    24
    >>> falling(4, 1)  # 4
    4
    >>> falling(4, 0)
    1
    """
    "*** YOUR CODE HERE ***"
    i = 0
    fac = 1
    while i < k :
        fac = fac * n
        n = n - 1
        i = i + 1
    return fac



def sum_digits(y):
    """Sum all the digits of y.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> a = sum_digits(123) # make sure that you are using return rather than print
    >>> a
    6
    """
    "*** YOUR CODE HERE ***"
    from operator import mod, floordiv
    sum = 0
    while y != 0:
        sum = sum + mod(y, 10)
        y = floordiv(y, 10)
    return sum
        



def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    from operator import mod, floordiv
    pre = 0
    cur = 0
    while n != 0:
        cur = mod(n, 10)
        if cur == 8:
            if cur == pre:
                return True
        pre = cur
        n = floordiv(n, 10)
    return False
