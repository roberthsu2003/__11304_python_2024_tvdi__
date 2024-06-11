import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,theme:str|None,**kwargs):
        super().__init__(**kwargs)
        self.title("BMI計算器")
        #self.configure(bg="#D3D3D3")
        #self.geometry("350x350+100+50")
        self.resizable(False,False)
        style = ttk.Style()
        #print(style.theme_names())

        mainFrame = ttk.Frame(self)
        title_label = ttk.Label(self, text="BMI計算器", font=("Arial", 20))
        title_label.pack(pady=10)
        mainFrame.pack(padx=100,pady=50)



def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()