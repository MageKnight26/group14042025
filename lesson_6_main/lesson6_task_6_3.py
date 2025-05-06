def multiply_digits(num):
    while num > 9:
        product = 1
        for digit in str(num):
            product *= int(digit)
        num = product
    return num


while True:
    user_input = input("Введіть ціле число: ").strip()
    if not user_input.isdigit():
        print("Будь ласка, введіть лише позитивне ціле число.")
        continue

    number = int(user_input)
    result = multiply_digits(number)
    print(f"Результат: {result}")

    while True:
        repeat = (
            input("Хочете ввести ще одне число? Так (Y) або Ні (N): ").strip().lower()
        )
        if repeat == "y":
            break
        elif repeat == "n":
            exit()
        else:
            print(
                "Невірний вибір! Оберіть потрібну відповідь ще раз - Так(Y) або Ні(N): "
            )
