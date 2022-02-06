def fizzbuzz(n):
    """
    >>> result = fizzbuzz(16)
    1
    2
    fizz
    4
    buzz
    fizz
    7
    8
    fizz
    buzz
    11
    fizz
    13
    14
    fizzbuzz
    16
    >>> result == None
    True
    """
    "*** YOUR CODE HERE ***"
    i = 1
    while i <= n:
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
            i = i + 1
        elif i % 3 == 0 and i % 5 != 0:
            print("fizz")
            i = i + 1
        elif i % 5 == 0 and i % 3 != 0:
            print("buzz")
            i = i + 1
        else:
            print(i)
            i = i + 1
        