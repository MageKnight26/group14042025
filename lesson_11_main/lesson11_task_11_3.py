def is_even(number: int | float) -> bool:
    """
    Checks if a number is even without using division or modulus

    - number (int | float): The number to check.
    Returns:
    - bool: True if even integer, False otherwise.
    """
    if isinstance(number, float):
        # якщо це дробове — воно не може бути парним
        if not number.is_integer():
            return False
        number = int(number)

    return (number & 1) == 0


assert is_even(2494563894038**2) == True, "Test1"
assert is_even(1056897**2) == False, "Test2"
assert is_even(24945638940387**3) == False, "Test3"

print("Ok")
