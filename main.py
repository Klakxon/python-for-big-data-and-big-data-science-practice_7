# main.py
from app.io.input import input_text_from_console, read_text_from_file, read_text_from_file_with_pandas
from app.io.output import output_text_to_console, write_text_to_file

def main():
    """
    Основна функція, яка виконує всі дії програми.

    Вводить текст з консолі, зчитує текст з файлів, виводить результати у консоль та записує їх до файлу.
    """
    # Введення тексту з консолі
    text_console = input_text_from_console()
    # Зчитування тексту з файлу за допомогою вбудованих можливостей Python
    text_file = read_text_from_file()
    # Зчитування тексту з файлу за допомогою бібліотеки pandas
    text_file_pandas = read_text_from_file_with_pandas()

    # Виведення тексту у консоль
    output_text_to_console(text_console)
    output_text_to_console(text_file)
    output_text_to_console(text_file_pandas)

    # Запис тексту до файлу за допомогою вбудованих можливостей Python
    write_text_to_file(text_console)
    write_text_to_file(text_file)
    write_text_to_file(text_file_pandas)

if __name__ == "__main__":
    main()
