import codecs
import re


def delete_html_tags(html_file: str, result_file: str = "cleaned.txt") -> None:
    """
    Removes HTML tags from a file and writes cleaned text to another file.
    Also logs how many tags and empty lines were removed.

    Parameters:
    - html_file (str): Path to the file containing HTML.
    - result_file (str): Path to save the cleaned text.
    """
    try:
        print("🔍 Функція запущена...")

        with codecs.open(html_file, "r", "utf-8") as file:
            html = file.read()

        # Знайти всі теги перед видаленням
        tags_found = re.findall(r"<.*?>", html)
        tag_count = len(tags_found)

        # Заміна HTML-тегів включно з багаторядковими
        cleaned_text = re.sub(r"<.*?>", "", html, flags=re.DOTALL)

        # Розбити на рядки, видалити порожні
        original_lines = cleaned_text.splitlines()
        non_empty_lines = [line.strip() for line in original_lines if line.strip()]
        removed_lines = len(original_lines) - len(non_empty_lines)

        # Записати у файл
        with codecs.open(result_file, "w", "utf-8") as output:
            output.write("\n".join(non_empty_lines))

        # Логи
        print(f"✔ Видалено тегів: {tag_count}")
        print(f"✔ Видалено порожніх рядків: {removed_lines}")
        print("Ок")

    except Exception as e:
        print(f"Сталася помилка: {e}")


# Виклик функції
if __name__ == "__main__":
    delete_html_tags("draft.html")  # ← Замінити на актуальний файл, якщо ім'я інше
