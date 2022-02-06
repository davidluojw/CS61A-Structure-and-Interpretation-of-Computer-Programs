def curried_pow(x):
    def h(y):
        return pow(x, y)
    return h

def map_to_range(start, end, f):
    """Return the value of f that takes argument from start to end.
    
    >>> map_to_range(0, 10, curried_pow(2))
    1
    2
    4
    8
    16
    32
    64
    128
    256
    512
    >>> map_to_range(0, 10, curried_pow(3))
    1
    3
    9
    27
    81
    243
    729
    2187
    6561
    19683
    >>> map_to_range(0, 10, pow_curried(2))
    1
    2
    4
    8
    16
    32
    64
    128
    256
    512
    >>> map_to_range(0, 10, pow_curried(3))
    1
    3
    9
    27
    81
    243
    729
    2187
    6561
    19683
    >>> pow_from_inverse(2, 9)
    512
    >>> pow_from_inverse(3, 9)
    19683
    """
    while start < end:
        print(f(start))
        start = start + 1

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

def uncurry2(g):
    def f(x, y):
        return g(x)(y)
    return f


map_to_range(0, 10, curried_pow(2))
map_to_range(0, 10, curried_pow(3))
pow_curried = curry2(pow)
map_to_range(0, 10, pow_curried(2))
map_to_range(0, 10, pow_curried(3))
pow_from_inverse = uncurry2(pow_curried)
print(pow_from_inverse(2, 9))
print(pow_from_inverse(3, 9))
