import sqlite3
import tkinter as tk
from tkinter import messagebox

def view_all_data():
    connection = sqlite3.connect("userdata.db")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM details")
    data = cursor.fetchall()
    connection.close()
    return data

def display_results(result):
    result_text.delete(1.0, tk.END)
    if not result:
        result_text.insert(tk.END, "No matching data found.")
    else:
        for row in result:
            result_text.insert(tk.END, f"ID: {row[0]}\n")
            result_text.insert(tk.END, f"First Name: {row[1]}\n")
            result_text.insert(tk.END, f"Last Name: {row[2]}\n")
            result_text.insert(tk.END, f"Age: {row[3]}\n")
            result_text.insert(tk.END, f"Mobile Number: {row[4]}\n")
            result_text.insert(tk.END, f"Email ID: {row[5]}\n")
            result_text.insert(tk.END, f"Gender: {row[6]}\n")
            result_text.insert(tk.END, f"Graduation: {row[7]}\n")
            result_text.insert(tk.END, "\n")

def on_view_all_button_press():
    result = view_all_data()
    display_results(result)

# Main Tkinter window
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (screen_width, screen_height))
window.title("View Data")

head_label = tk.Label(window,text="VIEWING WHOLE DATA", font=("Comic Sans MS", 52, 'bold'),  fg="#000000")
head_label.pack(pady=10)

view_all_button = tk.Button(window, text="View All", font=("Comic Sans MS", 15), command=on_view_all_button_press)
view_all_button.pack(pady=10)

result_text = tk.Text(window, height=45, width=100, font=("Comic Sans MS", 12))
result_text.pack()

window.mainloop()