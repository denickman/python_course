from todos import ensure_file_exists, get_todos, write_todos
import time

print("======time=======")
now = time.strftime("%b %d, %Y %H:%M:%S")
print(now)

print(f"📍 Запущен файл: {__file__}")
print(f"📍 __name__ = {__name__} \n")


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


print(help(ensure_file_exists))

