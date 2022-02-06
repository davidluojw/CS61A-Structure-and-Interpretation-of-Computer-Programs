def split(n):
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive integer n.

    n:
        n : integer n 

    >>> sum_digits(9)
    9
    >>> sum_digits(18117)
    18
    >>> sum_digits(9437184)
    36
    >>> sum_digits(11408855402054064613470328848384)
    126
    """
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last


    
def fact(n):
    """Return the factorial of n.

    >>> fact(4)
    24
    >>> fact(10)
    3628800
    """
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)
    
def is_even(n):
    if n == 0:
        return True
    else:
        return is_odd(n - 1)

def is_odd(n):
    if n == 0:
        return False
    else:
        return is_even(n - 1)

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(last * 2)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit
    
def cascade(n):
    """Print a cascade of prefixes of n.
    
    >>> cascade(12345)
    12345
    1234
    123
    12
    1
    12
    123
    1234
    12345
    """
    if n < 10:
        print(n)
    else:
        print(n)
        cascade(n // 10)
        print(n)

def inverse_cascade(n):
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)

def play_alice(n):
    """Return who win the game

    >>> play_alice(20)
    Bob wins!
    """
    if n == 0:
        print("Bob wins!")
    else:
        play_bob(n - 1)

def play_bob(n):
    if n == 0:
        print("Alice wins!")
    elif is_even(n):
        return play_alice(n - 2)
    else:
        return play_alice(n - 1)
    
# Tree Recursion

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n -2) + fib(n -1)
    
def count_partitions(n, m):
    """Count the ways to partition n using parts up to m.

    Args:
        n ([type]): a positive integer
        m ([type]): the parts up to size m
    >>> count_partitions(6, 4)
    9
    >>> count_partitions(5, 5)
    7
    >>> count_partitions(10, 10)
    42
    >>> count_partitions(15, 15)
    176
    >>> count_partitions(20, 20)
    627
    """
    # if n == 0:
    #     return 1
    # elif n < 0:
    #     return 0
    # elif m == 0:
    #     return 0
    # else:
    #     return count_partitions(n - m, m) + count_partitions(n, m - 1)
    if n < 0 or m == 0:
        return 0
    else:
        exact_match = 0
        if n == m:
            exact_match = 1
        return exact_match + count_partitions(n - m, m) + count_partitions(n, m - 1)
    
def list_partitions(n, m):
    """Count the ways to partition n using parts up to m.

    >>> for p in list_partitions(6, 4): print(p)
    [2, 4]
    [1, 1, 4]
    [3, 3]
    [1, 2, 3]
    [1, 1, 1, 3]
    [2, 2, 2]
    [1, 1, 2, 2]
    [1, 1, 1, 1, 2]
    [1, 1, 1, 1, 1, 1]
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [[m]]
        with_m = [p + [m] for p in list_partitions(n - m, m)]
        without_m = list_partitions(n, m - 1)
        return exact_match + with_m + without_m
def partitions(n, m):
    """Count the ways to partition n using parts up to m.

    >>> for p in partitions(6, 4): print(p)
    2 + 4
    1 + 1 + 4
    3 + 3
    1 + 2 + 3
    1 + 1 + 1 + 3
    2 + 2 + 2
    1 + 1 + 2 + 2
    1 + 1 + 1 + 1 + 2
    1 + 1 + 1 + 1 + 1 + 1
    """
    if n < 0 or m == 0:
        return []
    else:
        exact_match = []
        if n == m:
            exact_match = [str(m)]
        with_m = [p + ' + ' + str(m) for p in partitions(n - m, m)]
        without_m = partitions(n, m - 1)
        return exact_match + with_m + without_m


def accu(n):
    """Return the factorial of n.

    >>> accu(4)
    10
    >>> accu(10)
    55
    """
    result = 0
    for i in range(n + 1):
        result += i
    return result
    





