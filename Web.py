import streamlit as st
import module.function as function 

todos = function.readFile()

st.set_page_config(layout = 'wide')

def add_todo():
    todo = st.session_state['new_todo'].title() + "\n"
    todos.append(todo)
    function.writeFile(todos)



st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>", unsafe_allow_html=True)

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key = todo)
    if checkbox:
        todos.pop(index)
        function.writeFile(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="New todo: ", placeholder = "Add new todo...",
            on_change = add_todo, key = 'new_todo')
