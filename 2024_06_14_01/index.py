from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox
import data

class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)
        self.title('台北市YouBike2.0及時資料')
        try:
            self.__data = data.load_data()
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))
        
        self._display_interface()
        
    def _display_interface(self):
        mainFrame = ttk.Frame(borderwidth=1,relief='groove')
        ttk.Label(mainFrame,text="台北市YouBike2.0及時資料",font=('arial',25)).pack()
        tableFrame = ttk.Frame(mainFrame)
        tableFrame.pack(expand=True,fill=tk.BOTH)
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)



    @property
    def data(self)->list[dict]:
        return self.__data


def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()