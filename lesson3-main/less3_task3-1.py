print("Вітаємо у примітивному калькуляторі!")
while True:  # First input number
    first_numb_input = input("Введіть перше число:")
    if first_numb_input.strip() == "":
        print("Ви нічого не ввели. Спробуйте ще раз ввести перше число: ")
    elif first_numb_input.replace(".", "", 1).isdigit():
        break
    else:
        print("Це не число, спробуй ще раз: ")
first_numb = int(first_numb_input)

while True:  # Second input number
    second_numb_input = input("Введіть друге число:")
    if second_numb_input.strip() == "":
        print("Ви нічого не ввели. Спробуйте ще раз ввести перше число: ")
    elif second_numb_input.replace(".", "", 1).isdigit():
        break
    else:
        print("Це не число, спробуй ще раз: ")
second_numb = int(second_numb_input)

while True:  # Action selected
    action = input("Введіть бажану дію над числами (+ - * /):")
    if action in ["+", "-", "*", "/"]:
        break
    else:
        print(
            "Невірна дія, можливо вводити лише:\nДодавання +,\nВіднімання -,\nМоження *,\nДілення / \nСпробуйте ще раз:"
        )

if action == "+":
    summa = first_numb + second_numb
    print(f"Результат: {summa}")
elif action == "-":
    summa = first_numb - second_numb
    print(f"Результат: {summa}")
elif action == "*":
    summa = first_numb * second_numb
    print(f"Результат: {summa}")
elif action == "/":
    while second_numb == 0:
        print("Ділення на нуль неможливе!")
        second_numb = input("Введіть інше число замість нуля: ")
        if second_numb_input == "":
            print("Порожнє поле, спробуйте ще раз: ")
        elif second_numb_input.isdigit():
            second_numb = int(second_numb_input)
        else:
            print("Це не ціле число, спробуйте ще раз :")
        summa = first_numb / second_numb
        print(f"Результат: {summa}")
