import functions
import PySimpleGUI as sg

layout = [
    [sg.Text("Type in a to-do")],
    [sg.InputText(), sg.Button("Add")],
    [sg.Button("Edit"), sg.Button("Complete")],
    [ sg.Button("Exit")]
]
window = sg.Window('My To-Do App', layout)
window.read()
window.close()