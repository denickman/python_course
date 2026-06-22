import os

def ensure_file_exists(filepath='../files/todos.txt'):
    """Создаёт файл и папку если их нет"""
    # Шаг 1: Проверяем существует ли файл
    if not os.path.exists(filepath):  # Файла нет?

        # Шаг 2: Выделяем папку из пути
        directory = os.path.dirname(filepath)  # '../files'

        # Шаг 3: Проверяем существует ли папка
        if directory and not os.path.exists(directory):
            # Папка нет → создаём
            os.makedirs(directory)  # Создаёт '../files'

        # Шаг 4: Создаём пустой файл
        with open(filepath, 'w') as file:
            pass  # Создаёт '../files/todos.txt'


def get_todos(filepath='../files/todos.txt') -> list:
    ensure_file_exists(filepath)  # ← ВЫЗОВИ ФУНКЦИЮ!
    with open(filepath, 'r') as file:  # ✅ Правильно
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg='../files/todos.txt'):
    ensure_file_exists(filepath_arg)  # ← ВЫЗОВИ ФУНКЦИЮ!
    with open(filepath_arg, 'w') as file:  # ✅ Правильно
        file.writelines(todos_arg)



# 2️⃣ ГЛАВНАЯ ФУНКЦИЯ (main):
def main():
    """Главная логика программы"""
    print("=== TODO App ===\n")

    while True:
        user_action = input("Type add, show, edit, complete or exit: ").strip().lower()

        if user_action.startswith("add"):
            todo = user_action[4:].strip()
            if not todo:
                print("❌ Please enter a todo\n")
                continue

            todos = get_todos()
            todos.append(todo + '\n')
            write_todos(todos)
            print(f"✅ Added: {todo}\n")

        elif user_action.startswith('show'):
            todos = get_todos()
            if not todos:
                print("📝 No todos yet!\n")
                continue

            for index, item in enumerate(todos):
                print(f"{index + 1}. {item.strip()}")
            print()

        elif user_action.startswith('edit'):
            try:
                number = int(user_action[5:]) - 1
                todos = get_todos()

                if number < 0 or number >= len(todos):
                    print("❌ Invalid todo number\n")
                    continue

                new_todo = input("Enter new todo: ").strip()
                if not new_todo:
                    print("❌ Todo cannot be empty\n")
                    continue

                todos[number] = new_todo + '\n'
                write_todos(todos)
                print(f"✅ Updated!\n")
            except ValueError:
                print("❌ Your command is not valid.\n")
                continue

        elif user_action.startswith('complete'):
            try:
                number = int(user_action[9:]) - 1
                todos = get_todos()

                todo_to_remove = todos[number].strip('\n')
                todos.pop(number)
                write_todos(todos)

                print(f"✅ Removed: {todo_to_remove}\n")
            except (ValueError, IndexError):
                print("❌ Invalid todo number\n")
                continue

        elif user_action.startswith('exit'):
            break
        else:
            print("❌ Command is not valid.\n")

    print("👋 Bye!") 


main()



# Это означает:
# "Запусти main() только если этот файл запущен напрямую,
#  а не импортирован в другой файл"")