while True:  # Entering a loop to check of the input is correct
    user_input = input(
        "Введіть будь яке чотирьозначне число: "
    )  # Ask the user to enter numbers
    if (
        len(user_input) == 4 and user_input.isdigit()
    ):  # Checking the length of the entered data and the type of data
        print(
            f"{user_input[0]}\n{user_input[1]}\n{user_input[2]}\n{user_input[3]}"
        )  # Using index and formatting we output the result according to the task
        break  # Stoping program when successful
    else:  # request for re-entry if the user entered data incorrectly
        print("Помилка, ви ввели не чотирьозначне число. Спробуйте ще раз: ")
