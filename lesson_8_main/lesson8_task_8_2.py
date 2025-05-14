def is_palindrome(text):
    clean = "".join(
        char.lower() for char in text if char.isalnum()
    )  # We convert each character to lower case, skip only letters and numbers
    return clean == clean[::-1]  # expand the line


assert is_palindrome("A man, a plan, a canal: Panama") == True, "Test1"
assert is_palindrome("OP") == False, "Test2"
assert is_palindrome("a.") == True, "Test3"
assert is_palindrome("aurora") == False, "Test4"
print("Ok")
