import streamlit as st
import functions

st.set_page_config(layout="wide")

hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)


st.title("My Todo App ")
st.subheader("This is my todo app.")
st.write("This app is to increase your <b>productivity</b>.", unsafe_allow_html=True)

# EXPERIMENT 1: Move text_input before checkboxes
st.text_area(label="", placeholder="Add new todo...",  # EXP 2: Change input with area
             on_change=add_todo, key='new_todo')

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        print("Before experiment, before del")
        del st.session_state[todo]
        print("Before experiment after del")
        st.experimental_rerun()
        print("After experiments")