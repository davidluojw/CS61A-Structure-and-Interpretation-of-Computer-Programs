# Q1
def make_keeper(n):
    """Returns a function which takes one parameter cond and prints
    out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     # Even numbers have remainder 0 when divided by 2.
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    "*** YOUR CODE HERE ***"
    def print_int(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
    return print_int



# Q3: Curry2Lambda
"*** YOUR CODE HERE ***"
curry2 = lambda h: lambda x: lambda y: h(x, y)

# Self Reference
def print_sums(n):
    print(n)
    def next_sum(k):
        return print_sums(n + k)
    return next_sum

print_sums(5)(6)

# Q4: Make Keeper Redux
def make_keeper_redux(n):
    """Returns a function. This function takes one parameter <cond>
    and prints out all integers 1..i..n where calling cond(i)
    returns True. The returned function returns another function
    with the exact same behavior.

    >>> def multiple_of_4(x):
    ...     return x % 4 == 0
    >>> def ends_with_1(x):
    ...     return x % 10 == 1
    >>> k = make_keeper_redux(11)(multiple_of_4)
    4
    8
    >>> k = k(ends_with_1)
    1
    11
    >>> k
    <function do_keep>
    """
    # Paste your code for make_keeper here!
    def do_keep(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
            i += 1
        return make_keeper_redux(n)
    return do_keep

# Q5: Print N
def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    >>> g("first")("second")("third")
    first
    done
    done
    <function inner_print>
    """
    
    def inner_print(x):
        
        if n <= 0: 
            print("done")
        else:
            print(x)
        return print_n(n - 1)
    return inner_print

# Q7: YY Diagram
#  Using the + operator with two strings results in the second 
# string being appended to the first. For example "C" + "S" 
# concatenates the two strings into one string "CS".
y = "y"
h = y
def y(y):
    h = "h"
    if y == h:
        return y + "i"
    y = lambda y: y(h)
    return lambda h: y(h)
y = y(y)(y)

# Q8: Match Maker
# Implement match_k, which takes in an integer k and returns a 
# function that takes in a variable x and returns True if all the
# digits in x that are k apart are the same.

# For example, match_k(2) returns a one argument function that takes
# in x and checks if digits that are 2 away in x are the same.

# match_k(2)(1010) has the value of x = 1010 and digits 1, 0, 1, 0 
# going from left to right. 1 == 1 and 0 == 0, so the match_k(2)(1010) 
# results in True.

# match_k(2)(2010) has the value of x = 2010 and digits 2, 0, 1, 0 
# going from left to right. 2 != 1 and 0 == 0, so the match_k(2)(2010) 
# results in False.

def match_k(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    from operator import floordiv
    def check(x):
        cond = True
        while cond == True:
            if x < 10:
                if k == 1:
                    return True
            elif floordiv(x, pow(10, k)) % 10 != x % 10:
                return False
            x = floordiv(x, 10)
            if floordiv(x, pow(10, k)) == 0:
                cond = False
        return True
    return check

def match_k_solution(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        i = 0
        while 10 ** (i + k) < x:
            if (x // 10**i) % 10 != (x // 10**(i + k)) % 10:
                return False
            i = i + 1
        return True
    return check

def match_k_solution_alt(k):
    """ Return a function that checks if digits k apart match

    >>> match_k(2)(1010)
    True
    >>> match_k(2)(2010)
    False
    >>> match_k(1)(1010)
    False
    >>> match_k(1)(1)
    True
    >>> match_k(1)(2111111111111111)
    False
    >>> match_k(3)(123123)
    True
    >>> match_k(2)(123123)
    False
    """
    def check(x):
        while x // (10**k):
            if (x % 10) != (x // (10**k)) % 10:
                return False
            x //= 10
        return True
    return check

# Q9: Three Memory

# A k-memory function takes in a single input, prints whether that
# input was seen exactly k function calls ago, and returns a new 
# k-memory function. For example, a 2-memory function will display
# "Found" if its input was seen exactly two function calls ago, 
# and otherwise will display "Not found".

# Implement three_memory, which is a 3-memory function. You may 
# assume that the value None is never given as an input to your 
# function, and that in the first two function calls the function 
# will display "Not found" for any valid inputs given.

def three_memory(n):
    """
    >>> f = three_memory('first')
    >>> f = f('first')
    Not found
    >>> f = f('second')
    Not found
    >>> f = f('third')
    Not found
    >>> f = f('second') # 'second' was not input three calls ago
    Not found
    >>> f = f('second') # 'second' was input three calls ago
    Found
    >>> f = f('third') # 'third' was input three calls ago
    Found
    >>> f = f('third') # 'third' was not input three calls ago
    Not found
    """
    def f(x, y, z):
        def g(i):
            if i == x:
                print("Found")
            else:
                print("Not found")
            return f(y, z, i)
        return g
    return f(None, None, n)

# Q10: Natural Chain

# For this problem, a chain_function is a higher order function 
# that repeatedly accepts natural numbers (positive integers).
# The first number that is passed into the function that chain_function
# returns initializes a natural chain, which we define as a consecutive
# sequence of increasing natural numbers (i.e., 1, 2, 3).
# A natural chain breaks when the next input differs from the expected
# value of the sequence. For example, the sequence (1, 2, 3, 5) is 
# broken because it is missing a 4.

# Implement the chain_function so that it prints out the value of the
# expected number at each chain break as well as the number of chain 
# breaks seen so far, including the current chain break. Each time the 
# chain breaks, the chain restarts at the most recently input number.

# For example, the sequence (1, 2, 3, 5, 6) would only print 4 and 1. 
# We print 4 because there is a missing 4, and we print 1 because the 
# 4 is the first number to break the chain. The 5 broke the chain and 
# restarted the chain, so from here on out we expect to see numbers 
# increasingly linearly from 5. See the doctests for more examples. 
# You may assume that the higher-order function is never given numbers ≤ 0.

def chain_function():
    """
    >>> tester = chain_function()
    >>> x = tester(1)(2)(4)(5) # Expected 3 but got 4, so print 3. 1st chain break, so print 1 too.
    3 1
    >>> x = x(2) # 6 should've followed 5 from above, so print 6. 2nd chain break, so print 2
    6 2
    >>> x = x(8) # The chain restarted at 2 from the previous line, but we got 8. 3rd chain break.
    3 3
    >>> x = x(3)(4)(5) # Chain restarted at 8 in the previous line, but we got 3 instead. 4th break
    9 4
    >>> x = x(9) # Similar logic to the above line
    6 5
    >>> x = x(10) # Nothing is printed because 10 follows 9.
    >>> y = tester(4)(5)(8) # New chain, starting at 4, break at 6, first chain break
    6 1
    >>> y = y(2)(3)(10) # Chain expected 9 next, and 4 after 10. Break 2 and 3.
    9 2
    4 3
    """
    def g(x, y):
        def h(n):
            if x == 0 or n == x:
               return g(n + 1, y)
            else:
               return print(x, y + 1) or g(n + 1, y + 1)
        return h
    return g(0, 0)




                




