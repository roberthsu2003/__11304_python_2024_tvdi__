from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox
import data

class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)
        try:
            self.__data = data.load_data()
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))


    @property
    def data(self)->list[dict]:
        return self.__data


def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()