user_input = input(
    "Введіть елементи через пробіл (числа\слова\літери): "
)  # request input from user

if (
    user_input.strip() == ""
):  # check the list, if nothing is entered then we simply output the brackets of an empty list
    print("Cписок порожній, немає данних для обробки. Результат: []")

else:
    first_list = user_input.split()  # Turning it into a list
    last_element = first_list[-1]  # We take the last element in the list by index
    first_list.insert(
        0, last_element
    )  # We insert the last element at the beginning of the list
    first_list.pop()  # Remove the last element from the list (to avoid duplication)
    print(
        f"Новий список зі зміщенням останнього елементу на початок списку: {first_list}"
    )  # Output of the result
