import streamlit as st
import numpy as np
import pandas as pd

st.title("Task list 😃")

option = st.selectbox(label="Action", options=['Add', 'Remove', 'Recommend'])

if 'tasks' not in st.session_state:
    st.session_state['tasks'] = pd.DataFrame(columns=['Task', 'Priority'])

# To show the task list


def show_table():
    st.table(st.session_state['tasks'])


# Add task
if option == 'Add':
    task_name = st.text_input(label="Task name")
    task_priority = st.selectbox(label="Task priority", options=[
                                 'Low', 'Medium', 'High'])
    temp_df = pd.DataFrame(data=[[task_name, task_priority]],
                           columns=['Task', 'Priority'])
    if st.button("Add ✅"):
        st.session_state['tasks'] = pd.concat(
            [st.session_state['tasks'], temp_df], ignore_index=True, axis=0)
        st.write(
            f"#### :blue[{task_name}] with :blue[{task_priority}] priority :green[added] successfully!")
    show_table()
# Remove task
elif option == 'Remove':
    task_remove = st.selectbox(
        label="Task to remove", options=st.session_state['tasks']['Task'])
    if st.button("Remove ❌"):
        df = st.session_state['tasks'].copy()
        st.session_state['tasks'] = df[~df['Task'].str.contains(task_remove)]
        st.write(f"#### :blue[{task_remove}] :red[removed] successfully!")
    show_table()
# Recommend task
elif option == 'Recommend':
    df = st.session_state['tasks'].copy()
    if st.button("Recommend 👍"):
        df['priority_num'] = df['Priority'].map({
            'High': 0,
            'Medium': 1,
            'Low': 2
        })
        recommend_task = df.sort_values(by='priority_num').head()[
            'Task'].to_numpy()[0]
        st.write(f"#### Recommended task: :blue[{recommend_task}]")
    show_table()
