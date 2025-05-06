import string

letters_library = string.ascii_letters

while True:
    user_input = input(
        "Введіть дві літери через дефіс (наприклад a-c, b-y, a-z):"
    ).strip()
    start, end = user_input.split("-")
    start_index = letters_library.index(start)
    end_index = letters_library.index(end)
    result = letters_library[start_index : end_index + 1]
    print(f"Результат: {result}")

    while True:
        repeat = (
            input("Бажаєте повторити дію ще раз? Так (y) або Ні (n): ").strip().lower()
        )
        if repeat == "y":
            break
        elif repeat == "n":
            exit()
        else:
            print(
                "Невірний вибір! Оберіть потрібну відповідь ще раз - Так(Y) або Ні(N): "
            )
