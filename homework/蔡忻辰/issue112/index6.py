import os
os.system("cls")
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("問卷調查")
        self.iconphoto(False, tk.PhotoImage(file = "./images/coolcat.png"))
        self.geometry('300x400')
        self.resizable(False, False)
        box = ttk.Frame()
        box.pack(fill = 'x', padx = 10, pady = 10)
        ttk.Label(box, text="姓名:", font = ("Arial", 13, "bold")).pack(fill='x')
        name = ttk.Entry(box, font= (13))
        name.pack(side='left', pady = 3)
        name.focus()
        box2 = ttk.Frame()
        box2.pack(fill = 'x', padx = 10)
        ttk.Label(box2, text = "性別:", font = ("Arial", 13, "bold")).pack(fill='x')
        checkone = tk.Checkbutton(box2, text = "男", font =(13) )
        checkone.pack(side='left')
        checkone.deselect()
        checktwo = tk.Checkbutton(box2, text = "女", font = (13))
        checktwo.pack(side='left')
        checktwo.deselect()
        checkthree = tk.Checkbutton(box2, text = "多元性", font = (13))
        checkthree.pack(side='left')
        checkthree.deselect()
        box3 = ttk.Frame()
        box3.pack(fill = 'x', padx = 10, pady = 5)
        ttk.Label(box3, text="是否有養貓:", font = ("Arial",13, "bold")).pack(fill='x')
        combobox:ttk.Combobox=ttk.Combobox(box3, values=['請選擇', '是', '否'])
        combobox.pack(side='left')
        combobox.current(0)
        boxbutt = ttk.Frame()
        boxbutt.pack(fill = 'x', padx = 10, pady = 5)
        boxbutt.place(relx = 0.6, rely= 0.45)
        ttk.Button(boxbutt, text = "Submit").pack(ipadx = 5,ipady = 5)

if __name__ == '__main__':
   window:Window = Window()
   window.mainloop()