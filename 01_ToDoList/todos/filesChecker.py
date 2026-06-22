import os


def ensure_file_exists(filepath='../txtFiles/todos.txt'):
    """Создаёт файл и папку если их нет"""
    # Шаг 1: Проверяем существует ли файл
    if not os.path.exists(filepath):  # Файла нет?

        # Шаг 2: Выделяем папку из пути
        directory = os.path.dirname(filepath)  # '../txtFiles'

        # Шаг 3: Проверяем существует ли папка
        if directory and not os.path.exists(directory):
            # Папка нет → создаём
            print("Folder is not available, create it")
            os.makedirs(directory)  # Создаёт '../txtFiles'

        # Шаг 4: Создаём пустой файл
        with open(filepath, 'w') as file:
            print("Folder has been created")
            pass  # Создаёт '../txtFiles/todos.txt'
