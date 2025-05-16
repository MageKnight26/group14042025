from typing import Union


def difference(*args: Union[int, float]) -> Union[int, float]:
    """
    Returns the difference between the maximum and minimum values from the given arguments

    if not arguments are provided, returns 0
    if the result is mathematically an integer, returns int; otherwise returns float

    :param *args (int or float): A variable number of numeric values
    :return int or float: The difference between max and min
    """
    if not args:
        return 0

    result = max(args) - min(args)  # difference calculation
    result = round(result, 2)  # round to two digits as a result
    return (
        int(result) if result.is_integer() else result
    )  # Checks if a value looks like an integer


assert difference(1, 2, 3) == 2, "Test1"
assert difference(5, -5) == 10, "Test2"
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, "Test3"
assert difference() == 0, "Test4"
print("OK")
