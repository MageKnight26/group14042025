import keyword
import string


def is_valid_variable_name(name):  # checking variable name
    if name in keyword.kwlist:  # The name must not be a registered word.
        return False
    if name and name[0].isdigit():  # The name must not start with a number
        return False
    if any(char.isupper() for char in name):  # There should be no capital letters
        return False
    for char in name:  #
        if char in string.punctuation and char != "_":
            return False
        if char.isspace():  # Must not contain spaces or punctuation marks - except "_"
            return False
    if set(name) == {"_"} and len(name) > 1:  # Only one "_" in the whole name
        return False
    return True


while True:
    user_input_name = input("Введіть ім'я змінної для перевірки на валідність: ")
    print(is_valid_variable_name(user_input_name))
    while True:
        repeat = (
            input("\nБажаєте перевірити ще одне ім'я змінної? Так(Y) або Ні(N): ")
            .strip()
            .lower()
        )
        if repeat == "y":
            break
        elif repeat == "n":
            exit()
        else:
            print(
                "Невірний вибір! оберіть потрібну відповідь ще раз - Так(Y) або Ні(N): "
            )
