def common_elements():
    div3 = {x for x in range(100) if x % 3 == 0}
    div5 = {x for x in range(100) if x % 5 == 0}
    return div3 & div5

#test
assert common_elements() == {0, 15, 30, 45, 60, 75, 90}
print("OK")
