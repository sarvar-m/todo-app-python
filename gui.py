import functions
import PySimpleGUI as sg

layout = [
    [sg.Text("Type in a to-do")],
    [sg.InputText(tooltip="Enter todo", key="todo"), sg.Button("Add")],
    [
        sg.Listbox(values=functions.get_todos(), key="todos", enable_events=True, size=[45, 10]),
        sg.Button("Edit"),
        sg.Button("Complete")
    ],
    [sg.Button("Exit")]
]
window = sg.Window('My To-Do App', layout, font = ("Helvetica", 18))

while True:
    event, values = window.read()
    print('Event:', event)
    print('Values:', values)
    print(values["todos"])
    match event:
        case "Add":
            # print("Todos before adding:", todos)
            new_todo = values['todo'].strip()
            if new_todo:
                todos = functions.get_todos()
                todos.append(new_todo)
                functions.write_todos(todos)
                updated_todos = functions.get_todos()
                window["todos"].update(updated_todos)
                window["todo"].update("")
        case "Edit":
            todo_to_edit = values["todos"]
            new_todo = values["todo"]

            todos = functions.get_todos()
            if todo_to_edit:
                todo_to_edit_str = todo_to_edit[0]
                if todo_to_edit_str in todos:
                    index = todos.index(todo_to_edit_str)
            todos[index] = new_todo
            functions.write_todos(todos)
            updated_todos = functions.get_todos()
            window["todos"].update(updated_todos)
            window["todo"].update("")
        case "Complete":
            todo_to_complete = values["todos"][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            window["todos"].update(values=todos)
            window["todo"].update(value="")
        case "Exit":
            break
        case "todos":
            window["todo"].update(value=str(values["todos"][0]))
        case sg.WINDOW_CLOSED:
            break
print("Bye")
window.close()