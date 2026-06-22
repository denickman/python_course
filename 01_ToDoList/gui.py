import FreeSimpleGUI as sg
import todos.todosFunctions as todoFunc
import os


print("📍 Текущая директория:", os.getcwd())


label = sg.Text('type in a to-do')
input_box = sg.InputText(tooltip="Enter a to-do", key="input_box")
add_button = sg.Button('Add')

window = sg.Window('My To-do App',
                   layout=[[label, input_box, add_button]],
                   font=('Helvetica', 22))

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break


    if event == "Add":  # Просто проверяем кнопку
        print("====================")
        todo_text = values['input_box'].strip()

        print("Add new text:", todo_text)

        if todo_text:  # ← Проверка на не-пустой текст!
            # Загрузить, добавить, сохранить
            todos = todoFunc.get_todos()
            todos.append(todo_text + "\n")
            print("добавилено в туду лист", todos)

            todoFunc.write_todos(todos)

            # Очистить поле ввода
            window['input_box'].update('')

            print(f"✅ Добавлен: {todo_text}")
        else:
            print("❌ Введите что-то!")

window.close()
print("✅ Приложение закрыто")