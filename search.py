import sqlite3
import tkinter as tk
from tkinter import messagebox

def first_name_search():
    window1.destroy()

    def search_data(first_name):
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM details WHERE first_name = ?', (first_name,))
        data = cursor.fetchall()
        connection.close()
        return data

    def on_search_button_press():
        search_term = search_entry.get()
        if search_term:
            result = search_data(search_term)
            display_results(result)
        else:
            messagebox.showinfo("Error", "Please enter a search term.")

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

    # Main Tkinter window
    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (screen_width, screen_height))
    window.title("Search Data")

    head_label = tk.Label(window, text="Write the data that needs \n to be searched:",
                          font=("Comic Sans MS", 52, 'bold'), fg="#000000")
    head_label.pack(pady=10)

    search_label = tk.Label(window, text="Search:", font=("Comic Sans MS", 20))
    search_label.pack(pady=10)
    search_entry = tk.Entry(window, font=20)
    search_entry.pack(pady=10)

    search_button = tk.Button(window, text="Search", font=("Comic Sans MS", 15), command=on_search_button_press)
    search_button.pack(pady=8)

    result_text = tk.Text(window, height=15, width=50)
    result_text.pack(pady=10)

    window.mainloop()


def last_name_search():
    window1.destroy()
    def search_data(last_name):
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM details WHERE last_name = ?', (last_name,))
        data = cursor.fetchall()
        connection.close()
        return data

    def on_search_button_press():
        search_term = search_entry.get()
        if search_term:
            result = search_data(search_term)
            display_results(result)
        else:
            messagebox.showinfo("Error", "Please enter a search term.")

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

    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (screen_width, screen_height))
    window.title("Search Data")

    head_label = tk.Label(window, text="Write the data that needs \n to be searched:",
                          font=("Comic Sans MS", 52, 'bold'), fg="#000000")
    head_label.pack(pady=10)

    search_label = tk.Label(window, text="Search:", font=("Comic Sans MS", 20))
    search_label.pack(pady=10)
    search_entry = tk.Entry(window, font=20)
    search_entry.pack(pady=10)

    search_button = tk.Button(window, text="Search", font=("Comic Sans MS", 15), command=on_search_button_press)
    search_button.pack(pady=8)

    result_text = tk.Text(window, height=15, width=50)
    result_text.pack(pady=10)

    window.mainloop()


def age_search():
    window1.destroy()
    def search_data(age):
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM details WHERE age = ?', (age,))
        data = cursor.fetchall()
        connection.close()
        return data

    def on_search_button_press():
        search_term = search_entry.get()
        if search_term:
            result = search_data(search_term)
            display_results(result)
        else:
            messagebox.showinfo("Error", "Please enter a search term.")

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

    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (screen_width, screen_height))
    window.title("Search Data")

    head_label = tk.Label(window, text="Write the data that needs \n to be searched:",
                          font=("Comic Sans MS", 52, 'bold'), fg="#000000")
    head_label.pack(pady=10)

    search_label = tk.Label(window, text="Search:", font=("Comic Sans MS", 20))
    search_label.pack(pady=10)
    search_entry = tk.Entry(window, font=20)
    search_entry.pack(pady=10)

    search_button = tk.Button(window, text="Search", font=("Comic Sans MS", 15), command=on_search_button_press)
    search_button.pack(pady=8)

    result_text = tk.Text(window, height=15, width=50)
    result_text.pack(pady=10)

    window.mainloop()


def gender_search():
    window1.destroy()
    def search_data(gender):
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM details WHERE gender = ?', (gender,))
        data = cursor.fetchall()
        connection.close()
        return data

    def on_search_button_press():
        search_term = search_entry.get()
        if search_term:
            result = search_data(search_term)
            display_results(result)
        else:
            messagebox.showinfo("Error", "Please enter a search term.")

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

    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (screen_width, screen_height))
    window.title("Search Data")

    head_label = tk.Label(window, text="Write the data that needs \n to be searched:",
                          font=("Comic Sans MS", 52, 'bold'), fg="#000000")
    head_label.pack(pady=10)

    search_label = tk.Label(window, text="Search:", font=("Comic Sans MS", 20))
    search_label.pack(pady=10)
    search_entry = tk.Entry(window, font=20)
    search_entry.pack(pady=10)

    search_button = tk.Button(window, text="Search", font=("Comic Sans MS", 15), command=on_search_button_press)
    search_button.pack(pady=8)

    result_text = tk.Text(window, height=15, width=50)
    result_text.pack(pady=10)

    window.mainloop()


def graduation_search():
    window1.destroy()
    def search_data(graduation):
        connection = sqlite3.connect("userdata.db")
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM details WHERE graduation = ?', (graduation,))
        data = cursor.fetchall()
        connection.close()
        return data

    def on_search_button_press():
        search_term = search_entry.get()
        if search_term:
            result = search_data(search_term)
            display_results(result)
        else:
            messagebox.showinfo("Error", "Please enter a search term.")

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

    window = tk.Tk()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    window.geometry("%dx%d+0+0" % (screen_width, screen_height))
    window.title("Search Data")

    head_label = tk.Label(window, text="Write the data that needs \n to be searched:",
                          font=("Comic Sans MS", 52, 'bold'), fg="#000000")
    head_label.pack(pady=10)

    search_label = tk.Label(window, text="Search:", font=("Comic Sans MS", 20))
    search_label.pack(pady=10)
    search_entry = tk.Entry(window, font=20)
    search_entry.pack(pady=10)

    search_button = tk.Button(window, text="Search", font=("Comic Sans MS", 15), command=on_search_button_press)
    search_button.pack(pady=8)

    result_text = tk.Text(window, height=15, width=50)
    result_text.pack(pady=10)

    window.mainloop()


# Main Tkinter window
window1 = tk.Tk()
screen_width = window1.winfo_screenwidth()
screen_height = window1.winfo_screenheight()
window1.geometry("%dx%d+0+0" % (screen_width, screen_height))
window1.title("Search Data")

head_label = tk.Label(window1, text="Please select the criteria \n on which you want to search:",
                      font=("Comic Sans MS", 52, 'bold'), fg="#000000")
head_label.pack(pady=10)

first_name_search_button = tk.Button(window1, text="Search by First Name", font=("Comic Sans MS", 20), fg="#000000",
                                     command=first_name_search)
first_name_search_button.pack(pady=10)

last_name_search_button = tk.Button(window1, text="Search by Last Name", font=("Comic Sans MS", 20), fg="#000000",
                                    command=last_name_search)
last_name_search_button.pack(pady=10)

age_search_button = tk.Button(window1, text="Search by Age", font=("Comic Sans MS", 20), fg="#000000",
                              command=age_search)
age_search_button.pack(pady=10)

gender_search_button = tk.Button(window1, text="Search by Gender", font=("Comic Sans MS", 20), fg="#000000",
                                 command=gender_search)
gender_search_button.pack(pady=10)

graduation_search_button = tk.Button(window1, text="Search by Graduation Year", font=("Comic Sans MS", 20), fg="#000000",
                                     command=graduation_search)
graduation_search_button.pack(pady=10)

window1.mainloop()
