while True:  # Entering a loop to check of the input is correct
    s = input("Введіть будь яке п'ятизначне число:")  # Ask the user to enter numbers
    if (
        len(s) == 5 and s.isdigit()
    ):  # Checking the length of the entered data and the type of data
        reverse_number = (
            s[4] + s[3] + s[2] + s[1] + s[0]
        )  # Creating a new variable and outputting it via index countdown
        print("Введене число навпаки: ", f"{reverse_number}")
        break  # Stoping program when successful
    else:  # request for re-entry if the user entered data incorrectly
        print("Ви ввели не п'ятизначне число, спробуйте ще раз: ")
