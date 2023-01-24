import module.function as function 
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key = "todo")
add_button = sg.Button("Add")

Listbox = sg.Listbox(values = function.readFile(), key = "todos", 
                    enable_events = True, size = [45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")

exit_button = sg.Button("Exit")


window = sg.Window('My To-Do App', 
                    layout = [[label], [input_box, add_button], 
                            [Listbox, edit_button, complete_button],
                            [exit_button]],
                    font = ('Helvetica', 15))


while True:
    event, values = window.read()
    print("event: ",event)
    print("values: ",values)
    todos = function.readFile()
    match event:
        case "Add":
            newtodo = values['todo'].title() + "\n"
            todos.append(newtodo)
            function.writeFile(todos)
            window["todos"].update(values = todos)
        case "Edit":
            selectedTODO = values['todos'][0]
            newTODO = values['todo'].title() + "\n"
            index = todos.index(selectedTODO)
            todos[index] = newTODO
            function.writeFile(todos)
            window["todos"].update(values = todos)
        case "Complete":
            todo_to_complete = values['todos'][0]
            todos.remove(todo_to_complete)
            function.writeFile(todos)
            window['todos'].update(values = todos)
            window['todo'].update(value = '')
        case "Exit":
            break
        case "todos":
            window['todo'].update(value = values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()