import module.function as function 
import PySimpleGUI as sg
import time
import os

if not os.path.exists("venv/todos.txt"):
    with open("venv/todos.txt", "w") as file:
        pass

sg.theme('LightBrown13')

clock = sg.Text('',key = 'clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key = "todo")
add_button = sg.Button(size = 1, image_source = "venv/add1.png",
                        key = "Add")

Listbox = sg.Listbox(values = function.readFile(), key = "todos", 
                    enable_events = True, size = [45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")


window = sg.Window('My To-Do App', 
                    layout = [[clock],
                            [label], [input_box, add_button], 
                            [Listbox, edit_button, complete_button],
                            [exit_button]],
                    font = ('Time New Roman', 15))


while True:
    event, values = window.read()
    print(event)
    print(values)
    window['clock'].update(value = time.strftime("%b %d, %Y %H:%M:%S"))
    todos = function.readFile()
    match event:
        case "Add":
            newtodo = values['todo'].title() + "\n"
            todos.append(newtodo)
            function.writeFile(todos)
            window["todos"].update(values = todos)
        case "Edit":
            try:
                selectedTODO = values['todos'][0]
                newTODO = values['todo'].title() + "\n"
                index = todos.index(selectedTODO)
                todos[index] = newTODO
                function.writeFile(todos)
                window["todos"].update(values = todos)
            except IndexError:
                sg.popup("Please select a todo first", font =('Helvetica', 15))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos.remove(todo_to_complete)
                function.writeFile(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value = '')
            except IndexError:
                sg.popup("Please select a todo first", font =('Helvetica', 15))
        case "Exit":
            break
        case "todos":
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()