import os
os.system("cls")
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.iconphoto(True, tk.PhotoImage(file = "./images/user.png"))
        self.title("使用者登入畫面")
        self.geometry('500x300')
        self.resizable(False, False)
        box = ttk.Frame()
        box.pack(fill = 'x', padx = 10, pady = 10)
        acount:ttk.Label = ttk.Label(box, text = "帳號:", font=("Arial", 13, "bold"))
        acount.pack(fill = 'x')
        acounttxt:ttk.Entry = ttk.Entry(box)
        acounttxt.pack(fill = 'x', pady = 10)
        acounttxt.focus()

        password:ttk.Label = ttk.Label(box, text = "密碼:", font=("Arial", 13, "bold"))
        password.pack(fill = 'x')
        passwordtxt:ttk.Entry = ttk.Entry(box, show = "*")
        passwordtxt.pack(fill = 'x', pady = 10)
        ttk.Button(text = "Log in").pack(ipadx = 5, ipady = 5, expand=1)
        
if __name__ == '__main__':
    window:Window = Window()
    window.mainloop()