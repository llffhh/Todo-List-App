def readFile():
    """Read todo from a todos.txt"""
    with open('todos.txt','r') as file:
        todos = file.readlines()
    return todos

def writeFile(todos):
    """ Write todos list into todos.txt """
    with open('todos.txt','w') as file:
        file.writelines(todos)

def showTodo(todos):
    """ Show the todos as a list """
    for index, item in enumerate(todos):
        item = item.strip("\n")
        row = f"{index + 1}-{item}"
        print(row)

if __name__ == "__main__":
    print(readFile())