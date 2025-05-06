def time_convert(seconds):
    days = seconds // (24 * 60 * 60)
    seconds %= 24 * 60 * 60
    hours = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    if days == 1:
        day_word = "день"
    elif 2 <= days % 10 <= 4 and not (12 <= days % 100 <= 14):
        day_word = "дні"
    else:
        day_word = "днів"

    return f"{days} {day_word}, {str(hours).zfill(2)}:{str(minutes).zfill(2)}:{str(seconds).zfill(2)}"


while True:
    user_input = input("Введіть кількість секунд (від 0 до 8639999): ").strip()

    if not user_input.isdigit():
        print("Будь ласка, введіть лише ціле число. ")
        continue

    seconds = int(user_input)
    if 0 <= seconds < 8640000:
        print(time_convert(seconds))
    else:
        print("Число повинно бути в дозволенному діапазоні. Від 0 до 8639999.")

    while True:
        repeat = (
            input("Хочете повторити ще раз конвертування числа? Так (Y) або Ні (N): ")
            .strip()
            .lower()
        )
        if repeat == "y":
            break
        elif repeat == "n":
            exit()
        else:
            print(
                "Невірний вибір! Оберіть потрібну відповідь ще раз - Так(Y) або Ні(N): "
            )
