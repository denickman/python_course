


# Способ 1 — явно указываешь режим чтения
with open('../txtFiles/doc.txt', 'r') as file:
    print(file.read())  # ← здесь прочитал и вывел

    # or you can store into var - content = file.read()

file.read() # ← ошибка! файл уже закрыт после with


# # Способ 2 — режим 'r' подразумевается по умолчанию
# with open('txtFiles/doc.txt') as file:
#     print(file.read())
#
# # Добавление в конец (НУЖНО писать 'a'!)
# with open('file.txt', 'a') as file:
#     file.write("ещё текст")

#
# # Оба условия выполнены
# if 'add' in user_action and 'new' in user_action:
#     print("есть и add и new")  # "add new task"
#
# # Одно условие с исключением
# if 'add' in user_action and 'new' not in user_action:
#     print("есть add но нет new")  # "add task" но не "add new task"



#
# valid_commands = ['add', 'show', 'edit', 'remove', 'exit']
# user_action = input("Enter: ").strip().lower()
#
# # Проверка что команда правильная И не пустая
# if user_action in valid_commands and user_action != '':
#     print("команда принята")
#
# # Проверка что команда неправильная
# if user_action not in valid_commands:
#     print("неизвестная команда")
#
# # Проверка нескольких вариантов
# if 'show' in user_action or 'display' in user_action or 'list' in user_action:
#     print("показываем список")
