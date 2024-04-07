# input.py
def input_text_from_console():
    """
    Функція для вводу тексту з консолі.

    Returns:
        str: Введений текст.
    """
    return input("Введіть текст з консолі: ")

def read_text_from_file(file_path):
    """
    Функція для зчитування тексту з файлу за допомогою вбудованих можливостей Python.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        str: Текст, зчитаний з файлу.
    """
    with open(file_path, 'r') as file:
        return file.read()

def read_text_from_file_with_pandas(file_path):
    """
    Функція для зчитування тексту з файлу за допомогою бібліотеки pandas.

    Args:
        file_path (str): Шлях до файлу.

    Returns:
        str: Текст, зчитаний з файлу.
    """
    import pandas as pd
    data = pd.read_csv(file_path)
    return data.to_string(index=False)
