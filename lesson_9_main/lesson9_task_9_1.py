from typing import List, Dict


def popular_words(
    text: str, words: List[str]
) -> Dict[
    str, int
]:  # List of rows and dictionary - where the key is a row and the value is an integer
    """
    Counts the numbers of tomes each word from the given list appears in the text.
    The comprasion is case-insensitive. If a word is not found, its count will be zero
    :param text (str): the input text to search in
    :param words (List[str): A list words to count
    :return Dict[str, int]: A dictionary with the search words as keys and their counts as values.
    """
    word_list = text.lower().split()
    unique_words = set(words)
    result = {}
    for word in unique_words:
        result[word] = word_list.count(word)
    return {word: result.get(word, 0) for word in words}


assert popular_words(
    """When I was One I had hust begun When I was Two I was nearly new""",
    ["i", "was", "three", "near"],
) == {"i": 4, "was": 3, "three": 0, "near": 0}, "Test1"
print("Ok")
