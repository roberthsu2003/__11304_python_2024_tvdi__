from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk

class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)


def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()