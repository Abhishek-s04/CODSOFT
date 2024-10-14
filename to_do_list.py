import tkinter as tk
from tkinter import messagebox

#add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

#delete a task
def delete_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# mark task as completed
def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_task_index)
        task_listbox.delete(selected_task_index)
        task_listbox.insert(tk.END, f"{task} (Completed)")
    except:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("700x500")  


task_entry = tk.Entry(root, width=50)  
task_entry.grid(row=0, column=0, padx=10, pady=10)


add_button = tk.Button(root, text="Add Task", width=15, command=add_task) 
add_button.grid(row=0, column=1)

delete_button = tk.Button(root, text="Delete Task", width=15, command=delete_task)
delete_button.grid(row=1, column=1)

complete_button = tk.Button(root, text="Mark Completed", width=15, command=mark_completed)
complete_button.grid(row=2, column=1)

task_listbox = tk.Listbox(root, height=40, width=80)
task_listbox.grid(row=2, column=0, rowspan=3, padx=10, pady=10)


root.mainloop()

