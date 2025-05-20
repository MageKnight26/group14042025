from inspect import isgenerator


def pow(x):
    return x**2


def some_gen(begin, end, func):
    """
    Generates a sequence where each next value is produced by applying func to the previous one.
    :param begin: starting value
    :param end: number of values to yield
    :param func: function to apply to get the next value
    :return:
    """
    current = begin
    for _ in range(end + 1):
        yield current
        current = func(current)


gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, "Test1"
assert list(gen) == [2, 4, 16, 256, 65536], "Test2"
print("Ok")
