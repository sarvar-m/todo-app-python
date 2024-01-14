import functions
import PySimpleGUI as sg

layout = [
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add")],
    [sg.Button("Edit"), sg.Button("Complete")],
    [ sg.Button("Exit")]
]
window = sg.Window('My To-Do App', layout, font = ("Helvetica", 18))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WINDOW_CLOSED:
            break

window.close()