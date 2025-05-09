def second_index(text, some_str):
    first = text.find(some_str)  # Find first entry in index
    if first == -1:  # If not found - stop, there is no point in continuing the search
        return None
    second = text.find(
        some_str, first + 1
    )  # We search for the second input but starting from the position after the first
    return (
        second if second != -1 else None
    )  #  If found we return the index, otherwise None


assert second_index("sims", "s") == 3, "Test1"
assert second_index("find the river", "e") == 12, "Test2"
assert second_index("hi", "h") is None, "Test3"
assert second_index("Hello, hello", "lo") == 10, "Test4"
print("ОК")
