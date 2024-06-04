from pprint import pprint
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk
import tools

class Window(ThemedTk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("AQI顯示")
        ttk.Button(self, text="Quit", command=self.destroy).pack()


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
    window = Window(theme="blue")
    window.mainloop()
    

if __name__ == '__main__':
    main()