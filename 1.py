import tkinter as tk
import tkinterwidgets as tkw

window = tk.Tk()

window.title("WELCOME PAGE !")

screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.geometry("%dx%d+0+0" % (screen_width, screen_height))

window.configure(bg="#AA90F1")

window.resizable(False, False)

welcome_label = tkw.Label(window,text="WELCOME ! \n WHAT DO YOU WANT TO DO ???", font=("Comic Sans MS", 52, 'bold'),  fg="#000000", opacity=0.7)
welcome_label.pack(pady=10)


def insert_button_click():
    window.destroy()
    import insertdata


def search_button_click():
    window.destroy()
    import search


def view_button_click():
    window.destroy()
    import view

insert_button = tk.Button(window,text="1] Insert Data in Database", font=("Comic Sans MS", 35, 'bold'),  fg="#000000", command=insert_button_click)
insert_button.pack(pady=10)

search_button = tk.Button(window,text="2] Search Data in Database", font=("Comic Sans MS", 35, 'bold'),  fg="#000000", command=search_button_click)
search_button.pack(pady=10)

view_button = tk.Button(window,text="3] View Data of Database", font=("Comic Sans MS", 35, 'bold'),  fg="#000000", command=view_button_click)
view_button.pack(pady=10)

window.mainloop()