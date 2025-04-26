while True:
    # Request for user input elements
    user_input = input(
        "Введіть елементи через пробіл для створення списку та його поділу: "
    ).strip()
    # Create a common list
    list = user_input.split()
    result = []
    i = 0  # Increment
    if len(list) == 0:  # condition if the list is empty
        result.append([])
        result.append([])
    elif len(list) == 1:  # condition if list has 1 element
        result.append([list[0]])
        result.append([])
    elif len(list) == 2:  # condition if list has 2 element
        result.append([list[0]])
        result.append([list[1]])
    elif len(list) == 3:  # condition if list has 3 element
        result.append(list[0:2])
        result.append(list[2:3])
    elif (
        len(list) % 3
    ):  # Condition if the list has more than three elements (division into lists containing 3 elements each + the remainder in a separate list)
        while i < len(list):
            result.append(list[i : i + 3])
            i += 3
    else:
        while i + 3 <= len(list):
            result.append(list[i : i + 3])
            i += 3
        if i < len(list):
            result.append(list[i:])
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
