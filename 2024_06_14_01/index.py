from ttkthemes import ThemedTk
import tkinter as tk
from tkinter import ttk, messagebox
import data

class Window(ThemedTk):
    def __init__(self,theme:str='arc',**kwargs):
        super().__init__(theme=theme,**kwargs)
        self.title('台北市YouBike2.0及時資料')
        try:
            #self.__data = data.load_data()
            pass
        except Exception as e:
            messagebox.showwarning(title='警告',message=str(e))
        
        self._display_interface()
        
    def _display_interface(self):
        mainFrame = ttk.Frame(borderwidth=1,relief='groove')
        ttk.Label(mainFrame,text="台北市YouBike2.0及時資料",font=('arial',25)).pack()
        tableFrame = ttk.Frame(mainFrame)
        columns = ('first_name', 'last_name', 'email')
        tree = ttk.Treeview(tableFrame, columns=columns, show='headings')
        # define headings
        tree.heading('first_name', text='First Name')
        tree.heading('last_name', text='Last Name')
        tree.heading('email', text='Email')

        # generate sample data
        contacts = []
        for n in range(1, 100):
            contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))
        
        # add data to the treeview
        for contact in contacts:
            tree.insert('', tk.END, values=contact)
        
        tree.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(tableFrame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='ns')


        tableFrame.pack(expand=True,fill=tk.BOTH)
        mainFrame.pack(expand=True,fill=tk.BOTH,padx=10,pady=10)



    @property
    def data(self)->list[dict]:
        pass
        #return self.__data


def main():
    window = Window(theme='breeze')
    window.mainloop()

if __name__ == '__main__':
    main()