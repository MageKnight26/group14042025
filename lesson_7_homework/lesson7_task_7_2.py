def correct_sentence(text):
    text = text[0].upper() + text[1:]  # Capitalize the first letter
    if not text.endswith(
        "."
    ):  # Add a period at the end of the sentence if there is none
        text += "."
    return text


assert correct_sentence("greetings, friends") == "Greetings, friends.", "Test1"
assert correct_sentence("hello") == "Hello.", "Test2"
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", "Test3"
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", "Test4"
assert correct_sentence("greetings, friends.") == "Greetings, friends.", "Test5"
print("ОК")
