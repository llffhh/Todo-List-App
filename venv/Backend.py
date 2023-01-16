import module.function as function 
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is ", now)

while True:
    user_action = input("Type add, show, edit, complete or exit:")
    todos = function.readFile()
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo:") + "\n"
            todos.append(todo.title())
            function.writeFile(todos)  
        case 'show':
            function.showTodo(todos)
        case 'exit':
            break
        case 'edit':
            function.showTodo(todos)
            try:
                number = int(input("Number of the todo to edit:"))
                todoNew = input("Please enter new todo:") + "\n"
                todos[number - 1] = todoNew.title()
                function.writeFile(todos)
            except IndexError:
                print("There is no item inside the todo list.")
        case 'complete':
            function.showTodo(todos)
            try:
                number = int(input("Number of the todo to complete: "))
                complete_todo = todos.pop(number - 1)
                function.writeFile(todos)
                print("Congratulation you had finished your todo list: {}".format(complete_todo.strip('\n')))
            except IndexError:
                print("There is no item inside the todo list.")
            except:
                print("You have enter a none value.")
        case whatever:
            print("Hey, you entered an unknown comment!")

print('Bye')





