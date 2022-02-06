def special_case():
    """The difference between of if and elif.
    
    >>> special_case()
    12
    """
    x = 10
    if x > 0:
        x += 2
    elif x < 13:
        x += 3
    elif x % 2 == 1:
        x += 4
    return x


def just_in_case():
    """The difference between of if and elif.
    
    >>> just_in_case()
    19
    """
    x = 10
    if x > 0:
        x += 2
    if x < 13:
        x += 3
    if x % 2 == 1:
        x += 4
    return x


def case_in_point():
    """The difference between of if and elif.
    
    >>> case_in_point()
    12
    """
    x = 10
    if x > 0:
        return x + 2
    if x < 13:
        return x + 3
    if x % 2 == 1:
        return x + 4
    return x
