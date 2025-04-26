while True:
    # Request for user input elements
    user_input = input(
        "Введіть елементи через пробіл для створення списку та його поділу: "
    ).strip()
    # Create a common list
    custom_list = user_input.split()
    result = []
    increment = 0  # Increment
    if len(custom_list) == 0:  # condition if the list is empty
        result.append([])
        result.append([])
    elif len(custom_list) == 1:  # condition if list has 1 element
        result.append([custom_list[0]])
        result.append([])
    elif len(custom_list) == 2:  # condition if list has 2 element
        result.append([custom_list[0]])
        result.append([custom_list[1]])
    elif len(custom_list) == 3:  # condition if list has 3 element
        result.append(custom_list[0:2])
        result.append(custom_list[2:3])
    elif (
        len(custom_list) % 3
    ):  # Condition if the list has more than three elements (division into lists containing 3 elements each + the remainder in a separate list)
        while increment < len(custom_list):
            result.append(custom_list[increment : increment + 3])
            increment += 3
    else:
        while increment + 3 <= len(custom_list):
            result.append(custom_list[increment : increment + 3])
            increment += 3
        if increment < len(custom_list):
            result.append(custom_list[increment:])
    print(result)
    # Request to continue the program or exit it
    while True:
        repeat = (
            input("\nБажаєте повторити створення списків? Так(Y) або Ні(N): ")
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
