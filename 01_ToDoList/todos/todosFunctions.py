# from todos import ensure_file_exists - wrong
from .filesChecker import ensure_file_exists

FILEPATH = "../txtFiles/todos.txt"

def get_todos(filepath='../txtFiles/todos.txt') -> list:
    ensure_file_exists(filepath)  # ← ВЫЗОВИ ФУНКЦИЮ!
    with open(filepath, 'r') as file:  # ✅ Правильно
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath_arg='../txtFiles/todos.txt'):
    ensure_file_exists(filepath_arg)  # ← ВЫЗОВИ ФУНКЦИЮ!
    with open(filepath_arg, 'w') as file:  # ✅ Правильно
        file.writelines(todos_arg)


# ===== ВСПОМОГАТЕЛЬНЫЙ КОД (только для тестирования) =====
if __name__ == "__main__":
    print("🧪 Тестирую todosFunctions.py")
    print(f"__name__ = {__name__}")

    todos = get_todos()
    print(f"Todos: {todos}")