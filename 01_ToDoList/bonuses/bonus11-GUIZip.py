import FreeSimpleGUI as sg

label1 = sg.Text("Select files to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")



def create_file_input_row(label_text, button_text="Choose"):
    """Создает набор элементов для выбора файла"""

    label = sg.Text(label_text)
    input_box = sg.Input()
    button = sg.FileBrowse(button_text)

    return [label, input_box, button]

row1 = create_file_input_row("Select files to compress")
row2 = create_file_input_row("Select backup folder", "Choose")

layout = [
    row1,
    row2,
    [sg.Button('Compress')]
]

window = sg.Window('Zip File', layout)
window.read()

window.close()
print("close")