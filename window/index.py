import tkinter as tk

def get_names() -> list[str]:
    with open('names.txt',encoding='utf-8') as file:
        content:str = file.read()
    names:list[str] = content.split()
    return names

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        #多做一些事
        self.title("我的第一個GUI程式")

if __name__ == '__main__':
    names:list[str] = get_names()
    window:Window = Window()    
    window.mainloop()


