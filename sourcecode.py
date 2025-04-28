import tkinter as tk
from tkinter import messagebox
import pymysql as py 
mycon = py.connect(host = "localhost" ,database = "mep")
mycur = mycon.cursor()


#function for login
def login():
    c = 0
    userid = entry_username.get()
    password = entry_password.get()
    
    mycur.execute("select Name, userid from central;")
    data = mycur.fetchall()
    for a in data:
        x,y = a 
        if x == userid and y == password:
            messagebox.showinfo(title = "Logged in", message = "sucesfully logged in.")
            c = 1
            break
        else:
            pass
    if c == 0:
        messagebox.showerror(title="Invalid Login", message = "Unable to log in")

#making the window and its variious attributes
window = tk.Tk()
window.configure(bg = "#fbc4ab")
window.title("the 2ND program")
window.geometry("700x700")

#frame
frame = tk.Frame(window, bg = "#fbc4ab")

#making the widgets
label = tk.Label(frame, text = "Login" ,fg = "#000000",bg = "#fbc4ab", font = ("Times New Roman", 40))
label_username = tk.Label(frame, text = "Username", fg = "#000000", bg = "#fbc4ab", font = ("Times New Roman", 15))
label_password = tk.Label(frame, text = "Password", fg = "#000000", bg = "#fbc4ab", font = ("Times New Roman", 15))
entry_username = tk.Entry(frame)
entry_password = tk.Entry(frame, show = "*")
login_button = tk.Button(frame, text = "Login", bg = "#000000", fg ="#000000", font = ("Times New Roman", 15),command = login)

#confgiure of diff widgets
###############entry of the entry
entry_password.configure(borderwidth = 0, highlightbackground = "#fbc4ab")
entry_username.configure(borderwidth = 0, highlightbackground = "#fbc4ab")
login_button.configure(highlightbackground = "#fbc4ab")


#placing the widgets
label.grid(row = 0,column = 0, columnspan = 2,pady = 5)
label_username.grid(row = 1,column = 0,pady = 10)
entry_username.grid(row = 1,column = 1)
label_password.grid(row = 2,column = 0, pady = 10)
entry_password.grid(row = 2, column = 1)
login_button.grid(row = 3, column = 0, columnspan = 2, pady = 10)
frame.pack()


window.mainloop()
