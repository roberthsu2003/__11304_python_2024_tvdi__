import os
os.system('clear')
import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("按鈕位置和字體顏色")
        self.resizable(False,False)
        self.geometry('600x500')
        
        box = ttk.Frame()
        box.pack(fill='both', expand = 1)
        tk.Button(box, text = "NW", foreground="#CE0000").pack(side='left', fill='x', expand = 1,anchor='nw')
        tk.Button(box, text = "Top Center", foreground="#FF79BC").pack(side='left', fill='x', expand = 1, anchor='center')
        tk.Button(box, text = "SE", foreground="#8600FF").pack(side='left', fill='x', expand = 1,anchor='se')
        # 下部分
        box1 = ttk.Frame()
        box1.pack(fill='both', expand = 1)
        tk.Button(box1, text = "SW", foreground="#00AEAE").pack(side='bottom', fill='y', expand = 1, anchor='sw')
        tk.Button(box1, text = "Bottom Center", foreground="#FF8F59").pack(side='bottom', fill='y', expand = 1, anchor='center')
        tk.Button(box1, text = "NE", foreground="#0072E3").pack(side='bottom', fill='y', expand = 1, anchor='ne')

if __name__ == "__main__":
     window:Window = Window()
     window.mainloop()