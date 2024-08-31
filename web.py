"""
To run program type "streamlit run web.py"
in terminal in this directory
"""
import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'].strip() +'\n'
    if todo not in todos:
        todos.append(todo)
        functions.write_todos(todos)
    st.session_state["new_todo"] = ""

st.title('Keep track of tasks')
#st.subheader('Add tasks in box below.')
st.write('Click on box to remove task')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label=' ', placeholder='Add new todo - repeats will be ignored: ',
              on_change=add_todo, key='new_todo')

# st.session_state
