def compose1(f, g):
    """Return the compound function f(g(x)) = f(x + 1) = (x + 1)^2

    >>> compose1(lambda x: x * x, lambda y : y + 1)(12)
    169
    >>> compose1(lambda x: x * x, lambda y : y + 1)(13)
    196
    """
    return lambda x: f(g(x))

f = compose1(lambda x: x * x, lambda y : y + 1)


