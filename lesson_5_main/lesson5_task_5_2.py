while True:
    welcome = "Вітаємо у примітивному калькуляторі!"
    input_error = "Це не число, спробуй ще раз: "
    # Variable operation signs
    addition = "+"
    subtraction = "-"
    multiply = "*"
    divide = "/"
    all_operations = addition, subtraction, multiply, divide

    print(welcome)
    # First input number
    while True:
        first_number_input = input("Введіть перше число:").strip()
        if first_number_input == "":
            print("Ви нічого не ввели. Спробуйте ще раз ввести перше число: ")
        elif first_number_input.replace(".", "", 1).isdigit():
            first_number = float(first_number_input)
            break
        else:
            print(input_error)
    # Second input number
    while True:
        second_number_input = input("Введіть друге число:").strip()
        if second_number_input == "":
            print("Ви нічого не ввели. Спробуйте ще раз ввести друге число: ")
        elif second_number_input.replace(".", "", 1).isdigit():
            second_number = float(second_number_input)
            break
        else:
            print(input_error)
    # Action selected
    while True:
        action = input(f"Введіть бажану дію над числами ({all_operations}):").strip()
        if action in all_operations:
            break
        else:
            print(
                f"Невірна дія, можливо вводити лише:\nДодавання {addition},\nВіднімання {subtraction},\nМоження {multiply},\nДілення {divide} \nСпробуйте ще раз:"
            )
    # Checking for division by zero before operating on numbers
    if action == divide:
        while second_number == 0:
            print("Ділення на нуль неможливе!")
            second_number_input = input("Введіть інше число замість нуля: ").strip()
            if second_number_input == "":
                print("Порожній ввід. Спробуйте ще раз: ")
            elif second_number_input.replace(".", "", 1).isdigit():
                second_number = float(second_number_input)
            else:
                print(input_error)
    # Calculations for the selected action
    if action == addition:
        result = first_number + second_number
    elif action == subtraction:
        result = first_number - second_number
    elif action == multiply:
        result = first_number * second_number
    elif action == divide:
        result = first_number / second_number
    # Check result for integers
    if result.is_integer():
        result = int(result)
    # Result print
    print(f"Результат обчислення: {result}")
    while True:
        repeat = (
            input("\nПродовжити роботу калькулятора? Так(Y) або Ні(N): ")
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
