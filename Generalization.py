"""Generalization."""

from math import pi, sqrt

def area_square(r):
    return area(r, 1)

def area_circle(r):
    return area(r, pi)

def area_hexagon(r):
    return area(r, 3 * sqrt(3) /2)

def area(r, shape_constant):
    assert r > 0, 'A length must be positive'
    return r * r * shape_constant

def identity(k):
    return k

def cube(k):
    return pow(k, 3)

def summation(n, term):
    """Sum the first N term of a sequece.
    
    >>> summation(5, cube)
    225
    """
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def sum_naturals(n):
    """Sum the first N natural numbers

    >>> sum_naturals(5)
    15
    """

    total, k = 0, 1
    """while k <= n:    
        total,  k = total + k, k + 1"""
    return summation(n, identity)

def sum_cubes(n):
    """Sum the first N cubes of natural numbers
    
    >>> sum_cubes(5)
    225
    """

    """total, k = 0, 1
    while k <= n:
        total, k = total + pow(k, 3), k + 1"""
    return summation(n, cube)

def make_adder(n):
    """Return a function that takes one argument
    K and return K + N.
    
    >>> add_three = make_adder(3)
    >>> add_three(4)
    7
    """
    def adder(k):
        return k + n
    return adder


def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonble(n):
    return n == 0 or 1 / n != 0




