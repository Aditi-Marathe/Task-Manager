import tkinter as tk
from tkinter import messagebox
from tkinter.simpledialog import askstring

# Task list
tasks = []

# Functions
def add_task():
    task = task_entry.get()
    if task:
        due_date = askstring("📅 Due Date", "Enter due date (YYYY-MM-DD) or leave blank:")
        priority = askstring("🔺 Priority", "Enter priority (High/Medium/Low) or leave blank:")
        category = askstring("📂 Category", "Enter category or leave blank:")
        task_details = {
            "task": task,
            "completed": False,
            "due_date": due_date if due_date else "No due date",
            "priority": priority if priority else "No priority",
            "category": category if category else "No category"
        }
        tasks.append(task_details)
        update_tasks()
        messagebox.showinfo("Success", "Task added successfully! ✅")
    else:
        messagebox.showwarning("⚠ Warning", "Task cannot be empty!")

def delete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks.pop(selected_task_index[0])
        update_tasks()
        messagebox.showinfo("Deleted", "Task deleted successfully! 🗑")
    else:
        messagebox.showwarning("⚠ Warning", "No task selected!")

def complete_task():
    selected_task_index = task_listbox.curselection()
    if selected_task_index:
        tasks[selected_task_index[0]]["completed"] = True
        update_tasks()
        messagebox.showinfo("Completed", "Task marked as completed! ✅")
    else:
        messagebox.showwarning("⚠ Warning", "No task selected!")

def search_tasks():
    keyword = search_entry.get()
    if keyword:
        search_results = [task for task in tasks if keyword.lower() in task["task"].lower()]
        task_listbox.delete(0, tk.END)
        for task in search_results:
            status = "✅" if task["completed"] else "⏳"
            task_listbox.insert(tk.END, f'{status} {task["task"]} - 📅 {task["due_date"]} - 🔺 {task["priority"]} - 📂 {task["category"]}')
    else:
        messagebox.showwarning("⚠ Warning", "Search keyword cannot be empty!")

def update_tasks():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "⏳"
        task_listbox.insert(tk.END, f'{status} {task["task"]} - 📅 {task["due_date"]} - 🔺 {task["priority"]} - 📂 {task["category"]}')

def clear_all_tasks():
    if messagebox.askyesno("Confirmation", "Are you sure you want to clear all tasks? 🚮"):
        tasks.clear()
        update_tasks()
        messagebox.showinfo("Cleared", "All tasks cleared! 🗑")

# Create the main window
root = tk.Tk()
root.title("📌 Task Manager")
root.geometry("500x600")
root.configure(bg="#e6f7ff")

# Widgets with emojis
task_label = tk.Label(root, text="📝 Enter a task:", bg="#e6f7ff", font=("Arial", 12, "bold"))
task_label.pack(pady=5)

task_entry = tk.Entry(root, width=60, font=("Arial", 12))
task_entry.pack(pady=5)

add_button = tk.Button(root, text="➕ Add Task", command=add_task, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
add_button.pack(pady=5)

delete_button = tk.Button(root, text="🗑 Delete Task", command=delete_task, bg="#FF5733", fg="white", font=("Arial", 12, "bold"))
delete_button.pack(pady=5)

complete_button = tk.Button(root, text="✅ Complete Task", command=complete_task, bg="#008CBA", fg="white", font=("Arial", 12, "bold"))
complete_button.pack(pady=5)

search_label = tk.Label(root, text="🔍 Search tasks:", bg="#e6f7ff", font=("Arial", 12, "bold"))
search_label.pack(pady=5)

search_entry = tk.Entry(root, width=60, font=("Arial", 12))
search_entry.pack(pady=5)

search_button = tk.Button(root, text="🔎 Search", command=search_tasks, bg="#FFC107", fg="black", font=("Arial", 12, "bold"))
search_button.pack(pady=5)

clear_button = tk.Button(root, text="🚮 Clear All Tasks", command=clear_all_tasks, bg="#D9534F", fg="white", font=("Arial", 12, "bold"))
clear_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=60, height=15, font=("Arial", 12))
task_listbox.pack(pady=10)

# Start the main loop
root.mainloop()
