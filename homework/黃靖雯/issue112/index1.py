import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self, title:str = "Hello!", **kwargs):
        super().__init__(**kwargs)
        self.title(title)
        label:ttk.Label = ttk.Label(self, 
                                    text='Hey Jess!',
                                    font=('Arial', 30, 'bold'),
                                    foreground='#f98')
        label.pack(padx=100,pady=40)
        ttk.Button(self, text='Wave Back!').pack()

if __name__ == '__main__':
    window:Window = Window(title='Greetings')
    window.mainloop()