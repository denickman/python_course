import FreeSimpleGUI as sg
import todos.todosFunctions as todoFunc


# =============ПРАВИЛА==============

# # КНОПКИ → используют свой текст
# sg.Button('Add')         → event = 'Add'
# sg.Button('Delete')      → event = 'Delete'
#
# # ДРУГИЕ ЭЛЕМЕНТЫ → используют key (если enable_events=True)
# sg.Listbox(key='todos', enable_events=True)   → event = 'todos'
# sg.Checkbox(key='agree', enable_events=True)  → event = 'agree'
#
# # ЭЛЕМЕНТЫ БЕЗ enable_events → только в values
# sg.InputText(key='todo')  → НЕТ события, только values['todo']
# sg.Listbox(key='list')    → НЕТ события, только values['list']






label = sg.Text('type in a to-do')
input_box = sg.InputText(tooltip="Enter a to-do", key="todo")
add_button = sg.Button('Add')  # ← event = 'Add' при клике

# Listbox с enable_events=True → event = 'todos' при клике
list_box = sg.Listbox(values=todoFunc.get_todos(),
                      key="todos",
                      enable_events=True,  # ← Включить события!
                      size=[45, 10])

edit_button = sg.Button('Edit')  # ← event = 'Edit' при клике

window = sg.Window('My To-do App',
                   layout=[[label], [input_box, add_button], [list_box, edit_button]],
                   font=('Helvetica', 22))

while True:
    event, values = window.read()

    # event = 'Add', 'Edit', 'todos', sg.WIN_CLOSED или None
    # values = {'todo': 'текст', 'todos': ['выбранные', 'элементы']}

    print("Event:", event)
    print("Values:", values)

    match event:
        case sg.WIN_CLOSED:
            # Закрыто окно
            break

        case "Add":
            # ✅ event = 'Add' (текст кнопки)
            new_todo = values['todo'].strip()  # ← Получить из values

            if new_todo:
                todos = todoFunc.get_todos()
                todos.append(new_todo + "\n")

                todoFunc.write_todos(todos)
                
                window['todos'].update(values=todos)
                window['todo'].update('')  # Очистить input
                print(f"✅ Добавлен: {new_todo}")

        case "Edit":
            # ✅ event = 'Edit' (текст кнопки)
            selected = values['todos']  # ← Получить выбранные из values
            new_text = values['todo'].strip()  # ← Получить текст input из values

            if selected and new_text:
                todo_to_edit = selected[0].strip()
                todos = todoFunc.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_text + "\n"
                todoFunc.write_todos(todos)
                window['todos'].update(values=todos)
                print("✅ Отредактирован:", todo_to_edit)

        case 'todos':
            # ✅ event = 'todos' (key элемента, потому что enable_events=True)
            # Кликнули на список
            selected = values['todos']
            if selected:
                window['todo'].update(value=selected[0])
                print("Выбран:", selected[0])

        case _:
            pass

window.close()