import tkinter as tk
from tkinter import ttk

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("BMI計算")
        self.geometry("500x300")

        weight_label = ttk.Label(self, text="體重:")
        weight_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)
        self.weight_entry = ttk.Entry(self)
        self.weight_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        height_label = ttk.Label(self, text="身高")
        height_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)
        self.height_entry = ttk.Entry(self)
        self.height_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        self.bmi_label_text = tk.StringVar()
        self.bmi_label = ttk.Label(self, textvariable=self.bmi_label_text)
        self.bmi_label.grid(column=0, row=2, columnspan=2, pady=5)

        ttk.Button(self,text="計算",command=self.calculate).grid(column=0, row=3, columnspan=2, pady=5)


    def calculate(self):

        try:
            weight=self.weight_entry.get()
            height=self.height_entry.get()
            bmi = round(int(weight)/(int(height)/100)**2,2)
            self.bmi_label_text.set(f"BMI={bmi}")
        except Exception as e:
            self.bmi_label_text.set(f"輸入錯誤: {e}")

if __name__ =="__main__":
    window=Window()
    window.mainloop()
