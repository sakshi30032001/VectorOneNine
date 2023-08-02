import sqlite3
import tkinter as tk
from tkinter import messagebox

def create_table():
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS details (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            age INTEGER NOT NULL,
            mobile TEXT NOT NULL,
            email TEXT NOT NULL,
            gender TEXT NOT NULL,
            graduation TEXT NOT NULL
        )"""
    )
    connection.commit()
    connection.close()

def insert_data(first_name, last_name, age, mobile, email, gender, graduation):
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()
    cursor.execute(
        "INSERT INTO details (first_name, last_name, age, mobile, email, gender, graduation) VALUES (?, ?, ?, ?, ?, ?, ?)",(first_name, last_name, age, mobile, email, gender, graduation))
    connection.commit()
    connection.close()

def on_submit_button_press():
    first_name = first_name_entry.get()
    last_name = last_name_entry.get()
    age = age_entry.get()
    mobile = mobile_entry.get()
    email = email_entry.get()
    gender = gender_entry.get()
    graduation = graduation_entry.get()

    if first_name and last_name and age and mobile and email and gender and graduation:
        try:
            age = int(age)
            insert_data(first_name, last_name, age, mobile, email, gender, graduation)
            messagebox.showinfo("Success", "Data inserted successfully.")
        except ValueError:
            messagebox.showerror("Error", "Age must be a valid integer.")
    else:
        messagebox.showinfo("Error", "Please fill in all fields.")

def clear_form():
    first_name_entry.delete(0, tk.END)
    last_name_entry.delete(0, tk.END)
    age_entry.delete(0, tk.END)
    mobile_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    gender_entry.delete(0, tk.END)
    graduation_entry.delete(0, tk.END)

# Main Tkinter window
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (screen_width, screen_height))
window.title("Insert Data")

create_table()

head_label = tk.Label(window,text="Please Enter the details:", font=("Comic Sans MS", 52, 'bold'),  fg="#000000")
head_label.pack(pady=10)

first_name_label = tk.Label(window, text="FIRST NAME:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000")
first_name_label.pack()
first_name_entry = tk.Entry(window, width=40, font=8)
first_name_entry.pack()

last_name_label = tk.Label(window, text="LAST NAME:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000", )
last_name_label.pack()
last_name_entry = tk.Entry(window, width=40, font=8)
last_name_entry.pack()

age_label = tk.Label(window, text="AGE:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000")
age_label.pack()
age_entry = tk.Entry(window, width=40, font=8)
age_entry.pack()

mobile_label = tk.Label(window, text="MOBILE NUMBER:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000")
mobile_label.pack()
mobile_entry = tk.Entry(window, width=40, font=8)
mobile_entry.pack()

email_label = tk.Label(window, text="EMAIL-ID:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000")
email_label.pack()
email_entry = tk.Entry(window, width=40, font=8)
email_entry.pack()

gender_label = tk.Label(window, text="GENDER:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000")
gender_label.pack()
gender_entry = tk.Entry(window, width=40, font=8)
gender_entry.pack()

graduation_label = tk.Label(window, text="GRADUATION YEAR:", font=("Comic Sans MS", 15, 'bold'),  fg="#000000")
graduation_label.pack()
graduation_entry = tk.Entry(window, width=40, font=8)
graduation_entry.pack()

submit_button = tk.Button(window, text="SUBMIT", font=("Comic Sans MS", 10),  fg="#000000", command=on_submit_button_press)
submit_button.pack(pady=10)

clear_button = tk.Button(window, text="CLEAR", font=("Comic Sans MS", 10),  fg="#000000", command=clear_form)
clear_button.pack(pady=10)

window.mainloop()
