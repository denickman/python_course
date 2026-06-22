import FreeSimpleGUI as sg
import todos.todosFunctions as todoFunc

label = sg.Text('type in a to-do')
input_box = sg.InputText(tooltip="Enter a to-do", key="input_box")
add_button = sg.Button('Add')

window = sg.Window('My To-do App',
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 22))


while True:
    event, values = window.read()

    print("Event (Кнопка):", event)           # Add, Cancel, etc.
    print("Values (Данные):", values)         # {'input_box': 'fuck off'}


    match event:
        case "add":
            todos = todoFunc.get_todos()
            new_todo = values['todo'] + "\n"  # get value from dict 'values'
            todos.append(new_todo)
            todoFunc.write_todos(todos)

        case sg.WIN_CLOSED:
            break




# Получить значение
    todo_text = values['input_box']
    print("Юзер ввел:", todo_text)

# Проверить какую кнопку нажали
    if event == 'Add':
        print("Добавляем:", todo_text)
    elif event == sg.WINDOW_CLOSED:
        print("Окно закрыто")

    window.close()