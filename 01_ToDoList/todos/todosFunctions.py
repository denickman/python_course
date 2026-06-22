# from todos import ensure_file_exists - wrong
from .filesChecker import ensure_file_exists

FILEPATH = "./txtFiles/todos.txt"

def get_todos(filepath=FILEPATH) -> list:
    ensure_file_exists(filepath)  # ← ВЫЗОВИ ФУНКЦИЮ!
    with open(filepath, 'r') as file:  # ✅ Правильно
        todos_local = file.readlines()
        print("✅ READ", todos_local)
    return todos_local


def write_todos(todos_arg, filepath_arg=FILEPATH):
    ensure_file_exists(filepath_arg)  # ← ВЫЗОВИ ФУНКЦИЮ!
    with open(filepath_arg, 'w') as file:  # ✅ Правильно
        file.writelines(todos_arg)
        print("✅ WRITTEN SUCCESSFULLY", todos_arg)


# ===== ВСПОМОГАТЕЛЬНЫЙ КОД (только для тестирования) =====
if __name__ == "__main__":
    print("🧪 Тестирую todosFunctions.py")
    print(f"__name__ = {__name__}")

    todos = get_todos()
    print(f"Todos: {todos}")