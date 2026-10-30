
import tkinter as tk
from tkinter import ttk, messagebox
import csv

# Save student details
def submit():
    name = name_entry.get()
    div = div_entry.get()
    roll = roll_entry.get()
    email = email_entry.get()
    phone = phone_entry.get()

    if not name or not div or not roll or not email or not phone:
        messagebox.showwarning("Warning", "Fill all fields")
        return

    if "@" not in email or not email.endswith(".com"):
        messagebox.showwarning("Error", "Enter a valid email")
        return

    if not phone.isdigit() or len(phone) != 10:
        messagebox.showwarning("Error", "Enter 10 digit phone number")
        return

    with open("student.txt", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, div, roll, email, phone])

    messagebox.showinfo("Success", "Details saved successfully")


# Display student details in a table
def read():
    try:
        with open("student.txt", "r", newline="") as file:
            records = list(csv.reader(file))
    except FileNotFoundError:
        messagebox.showinfo("Info", "Submit details first")
        return

    window = tk.Toplevel(root)
    window.title("Student Records")

    columns = ("Name", "Division", "Roll No", "Email", "Phone")
    table = ttk.Treeview(window, columns=columns, show="headings")

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=130)

    for record in records:
        if len(record) == 5:
            table.insert("", "end", values=record)

    table.pack(padx=10, pady=10)


# Create main window
root = tk.Tk()
root.title("Student Details")
root.geometry("300x400")

tk.Label(root, text="Student Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Division").pack()
div_entry = tk.Entry(root)
div_entry.pack()

tk.Label(root, text="Roll No").pack()
roll_entry = tk.Entry(root)
roll_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Phone Number").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Button(root, text="Submit", command=submit).pack(pady=10)
tk.Button(root, text="Read", command=read).pack()

root.mainloop()
