import streamlit as st

def view_tasks(tasks):
    if not tasks:
        st.write("No tasks found.")
    else:
        for index, task in enumerate(tasks, start=1):
            st.write(f"{index}. {task}")

def add_task(tasks, new_task):
    tasks.append(new_task)
    st.success(f"Task '{new_task}' added successfully!")

def mark_completed(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        st.success(f"Task '{completed_task}' marked as completed!")
    else:
        st.error("Invalid task index.")

def main():
    st.title("Simple To-Do List")
    
    tasks = st.session_state.get('tasks', [])

    if 'initialized' not in st.session_state:
        st.session_state.initialized = True

    choice = st.sidebar.selectbox("Select an action", ["View tasks", "Add task", "Mark task as completed"])

    if choice == "View tasks":
        view_tasks(tasks)
    elif choice == "Add task":
        new_task = st.text_input("Enter the new task:")
        if st.button("Add Task"):
            add_task(tasks, new_task)
    elif choice == "Mark task as completed":
        task_index = st.number_input("Enter the task index to mark as completed:", min_value=1, max_value=len(tasks))
        if st.button("Mark as Completed"):
            mark_completed(tasks, int(task_index) if task_index else None)

    st.session_state.tasks = tasks

if __name__ == "__main__":
    main()
