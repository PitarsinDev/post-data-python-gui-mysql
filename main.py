import tkinter as tk
from tkinter import ttk
import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="add_gui"
)
cursor = db.cursor()

def add_record():
    global entry_name, entry_occupation, entry_salary
    name = entry_name.get()
    occupation = entry_occupation.get()
    salary = entry_salary.get()

    sql = "INSERT INTO employee (name, occupation, salary) VALUES (%s, %s, %s)"
    values = (name, occupation, salary)
    cursor.execute(sql, values)
    db.commit()

    entry_name.delete(0, tk.END)
    entry_occupation.delete(0, tk.END)
    entry_salary.delete(0, tk.END)

def main():
    global entry_name, entry_occupation, entry_salary 
    root = tk.Tk()
    root.title("ระบบบันทึกข้อมูล")

    label_name = ttk.Label(root, text="Name :")
    label_occupation = ttk.Label(root, text="Position :")
    label_salary = ttk.Label(root, text="Money :")

    button_add = ttk.Button(root, text="Add Data", command=lambda: add_record(entry_name, entry_occupation, entry_salary))

    entry_name = ttk.Entry(root)
    entry_occupation = ttk.Entry(root)
    entry_salary = ttk.Entry(root)

    button_add = ttk.Button(root, text="Add Data", command=add_record)

    label_name.grid(row=0, column=0, padx=5, pady=5)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    label_occupation.grid(row=1, column=0, padx=5, pady=5)
    entry_occupation.grid(row=1, column=1, padx=5, pady=5)
    label_salary.grid(row=2, column=0, padx=5, pady=5)
    entry_salary.grid(row=2, column=1, padx=5, pady=5)

    button_add.grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()