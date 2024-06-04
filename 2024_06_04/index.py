from pprint import pprint
import tkinter as tk
from tkinter import ttk
import tools

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("AQI顯示")


def main():
    '''
    try:
        all_data:dict[any] = tools.download_json()
    except Exception as error:
        print(error)
    else:        
        data:list[dict] = tools.get_data(all_data)
        pprint(data)
    '''
    window = Window()
    window.mainloop()
    

if __name__ == '__main__':
    main()