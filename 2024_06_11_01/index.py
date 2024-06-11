import tkinter as tk
from ttkthemes import ThemedTk

class Window(ThemedTk):
    def __init__(self,theme:str|None,**kwargs):
        super().__init__(**kwargs)


def main():
    window = Window(theme='arc')
    window.mainloop()

if __name__ == '__main__':
    main()