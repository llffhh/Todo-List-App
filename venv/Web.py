import streamlit as st
import module.function as function 

todos = function.readFile()

def add_todo():
    todo = st.session_state['new_todo'].title() + "\n"
    todos.append(todo)
    function.writeFile(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="New todo: ", placeholder = "Add new todo...",
            on_change = add_todo, key = 'new_todo')

st.session_state

print("hello")