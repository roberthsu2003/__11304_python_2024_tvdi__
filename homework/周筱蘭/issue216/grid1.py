import tkinter as tk
from tkinter import ttk
# login視窗,2個輸入框, 一個按鈕

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry("240x100")
        self.title('Login')
        self.resizable(0, 0)

        # configure the grid
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        # username
        username_label = ttk.Label(self, text="姓名:")
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # password
        height_label = ttk.Label(self, text="身高:")
        height_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        height_entry = ttk.Entry(self,  show="*")
        height_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        weight_label = ttk.Label(self, text="體重:")
        weight_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

        weight_entry = ttk.Entry(self,  show="*")
        weight_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        # login button
        login_button = ttk.Button(self, text="Login")
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)


if __name__ == "__main__":
    app = App()
    app.mainloop()