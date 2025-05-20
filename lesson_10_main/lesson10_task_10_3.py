def is_even(digit: int) -> bool:
    """
    Checks whether a given integer is even

    :param digit: the number to check
    :return: true if the number is even, False otherwise
    """

    return digit % 2 == 0


assert is_even(2) == True, "Test1"
assert is_even(5) == False, "Test2"
assert is_even(0) == True, "Test3"
print("Ok")
