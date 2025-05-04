import string


def generate_hashtag(text):
    for char in string.punctuation:  # removing punctuation
        text = text.replace(char, "")

        words = text.strip().split()  # We break it down into words and capital letters
        hashtag = "#" + "".join(word.capitalize() for word in words)

        return hashtag[:140]


while True:
    user_input = input("Введіть рядок для створення хештегу: ")
    result = generate_hashtag(user_input)
    print(f"Результат: {result}")

    while True:
        repeat = (
            input("\nБажаєте створити ще один хештег? Так (Y) або Ні (N): ")
            .strip()
            .lower()
        )
        if repeat == "y":
            break
        elif repeat == "n":
            exit()
        else:
            print(
                "Невірна відповідь! Оберіть між Так (Y) або Ні (N). Спробуйте ще раз: "
            )
