def get_common_multiplies(limit, divide_a, divide_b):
    multiplies_a = {x for x in range(limit) if x % divide_a == 0}
    multiplies_b = {x for x in range(limit) if x % divide_b == 0}
    return multiplies_a & multiplies_b


# test
assert get_common_multiplies(100, 3, 5) == {0, 15, 30, 45, 60, 75, 90}
print("OK")
