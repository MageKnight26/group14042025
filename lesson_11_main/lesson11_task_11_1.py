def prime_generator(end: int):
    """
    Generates prime numbers from 2 up to the specified end value

    parameters:
    - end (int): Upper bound of the range (inclusive).
    Yields:
    - int: The next prime number in sequence.
    """
    for num in range(2, end + 1):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            yield num


from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, "Test0"
assert list(prime_generator(10)) == [2, 3, 5, 7], "Test1"
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], "Test2"
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "Test3"
print("Ok")
