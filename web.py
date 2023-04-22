import streamlit as st
import functions as fn

todos = fn.get_todos()


def add_todo():
    todo_item = st.session_state['new_todo']
    todos.append(todo_item+'\n')
    fn.write_todos(items=todos)
    st.session_state['new_todo']=''


st.title("My Todo App")
st.subheader('This is my todo app')
st.write('This app is to increase your productivity.')

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo,key=todo)
    if checkbox:
        todos.pop(index)
        fn.write_todos(items=todos)
        del st.session_state[todo]
        st.session_state['new_todo'] = ''
        st.experimental_rerun()

st.text_input(label='Enter a todo', placeholder='Add new todo...', on_change=add_todo, key='new_todo')

