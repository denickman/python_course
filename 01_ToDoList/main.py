
import os


# print(os.getcwd())  # покажи текущую папку
# print(os.listdir('.'))  # покажи что в папке

print(os.listdir('files/'))

while True:

    user_action = input("enter your action: ").strip().lower()
    # user_action = user_action.strip()

    # match user_action:
    # case 'show' | 'display': for match operator

    # if 'add' in user_action and 'new' in user_action:
    # if 'add' in user_action and 'new' not in user_action:

    # if 'add' in user_action or 'new' in user_action:

    if user_action.startswith('show'):


        todo = user_action[4:] # remove first 3 symbols in string
        #  todo = user_action[4:6] # get symbol from 4 to 6


        # Check if file exist
        if not os.path.exists('files/todos.txt'):
            print("DEBUG: файла нет, пытаемся создать")

            with open('files/todos.txt', 'w') as file:
                pass

            # код дальше ← вне with (нет отступа)
        print(f"DEBUG: файл существует после создания? {os.path.exists('files/todos.txt')}")
        print(f"DEBUG: файлы в папке: {os.listdir('files/')}")

        print("⚠️  File didn't exist, created it. Please try again!")
        continue

        # # Чтение
        # with open('todos.txt', 'r') as file:
        #     todos = file.readlines()
        #
        # # Запись
        # with open('todos.txt', 'w') as file:
        #     file.writelines(todos)
        #
        # # Добавление в конец файла (не стирает старое)
        # with open('todos.txt', 'a') as file:
        #     file.write("новая задача\n")

        # Option 1 read
        # file = open('files/todos.txt', 'r') # read mode
        # todos = file.readlines()
        # file.close()

        #Option 2 read
        with open('files/todos.txt', 'r') as file:
            todos = file.readlines()

        todos.append(f'{todo}\n')

        # Option 1 read store in file
        # file = open('files/todos.txt', 'w')  # write mode
        # file.writelines(todos)
        # file.close()

        # Option 2 read store in file
        with open(f'files/todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):
        todo = user_action[4:].strip()  # Добавил .strip()

        # Check if file exist
        if not os.path.exists('files/todos.txt'):
            print("📁 File created!")

            with open('files/todos.txt', 'w') as file:
                pass
            # НЕ используем continue - продолжаем дальше!

        # Теперь код выполнится:
        try:
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            if todo:  # Если пользователь ввел текст после "show"
                todos.append(f'{todo}\n')

                with open('files/todos.txt', 'w') as file:
                    file.writelines(todos)

                print(f"✅ Added: {todo}")
            else:
                print("❌ Please enter a task after 'show'")

        except FileNotFoundError:
            print("❌ File not found!")



    elif user_action in ['show', 'display']:
        # or -> if 'show' in user_action or 'display' in user_action:

       file = open('files/todos.txt', 'r')
       todos = file.readlines()
       file.close()

        # First Option
       # new_todos = []
       #
       # for item in todos:
       #     new_item = item.strip('\n')
       #     new_todos.append(new_item)

       # Second Option
       new_todos = [item.strip('\n') for item in todos]

       for index, item in enumerate(new_todos):
           # Third Option
           item = item.strip('\n')

           row = f'{index + 1}. {item}'
           print(row)
       # print("XXX:", index, item)

    # Previous Option with is not
    # elif 'edit' in user_action:
    #     with open('files/todos.txt', 'r') as file:
    #         todos = file.readlines()
    #
    #         if not todos:
    #             print("❌ No todos to edit")
    #             continue
    #
    #
    #     number = int(input("number of edit: "))
    #     number = number - 1
    #
    #     if number < 0 or number >= len(todos):
    #         print(f"❌ Todo #{number + 1} doesn't exist. You have {len(todos)} todos")
    #         continue
    #
    #     new_todo = input("Enter new todo: ")
    #     todos[number] = new_todo
    #
    #     with open('files/todos.txt', 'w') as file:
    #         file.writelines(todos)


    # New approach with try
    elif 'edit' in user_action:
        try:
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            if not todos:
                print("❌ No todos to edit")
                continue

            number = int(input("Number to edit: ")) - 1

            if number < 0 or number >= len(todos):
                print(f"❌ Todo #{number + 1} doesn't exist. You have {len(todos)} todos")
                continue

            new_todo = input("Enter new todo: ").strip()

            if not new_todo:
                print("❌ Todo cannot be empty!")
                continue

            todos[number] = f"{new_todo}\n"

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"✅ Todo #{number + 1} updated!")

        except ValueError:
            print("❌ Please enter a valid number!")
            continue
        except FileNotFoundError:
            print("❌ File not found!")
            continue
        except Exception as e:
            print(f"❌ Error: {e}")
            continue



    elif 'remove' in user_action:
        try:
            with open('files/todos.txt', 'r') as file:
                todos = file.readlines()

            number = int(user_action[7:])
            index = number - 1

            if index < 0 or index >= len(todos):
                print(f"❌ Todo #{number} doesn't exist!")
                continue

            todo_to_remove = todos.pop(index)

            with open('files/todos.txt', 'w') as file:
                file.writelines(todos)

            print(f"✅ todo '{todo_to_remove.strip()}' was removed!")

        except ValueError:
            print("❌ Please enter a valid number!")
            continue
        except Exception as e:
            print(f"❌ Error: {e}")
            continue


    elif 'exit' in user_action:
        todos = []
        break

    # case _:
    else:
        print("FUCK OFF DUDE! Try AGAIN")

print("Finish")