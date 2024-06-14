from tkinter.simpledialog import Dialog
from tkinter import ttk
from tkinter import Misc
import tkinter as tk
from data import Info

class CustomMessagebox(Dialog):    
    def __init__(self, parent:Misc, title:str,site:Info):        
        print(site)
        super().__init__(parent=parent, title=title)

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        contain_frame = ttk.Frame(master,style='Input.TFrame')         

        contain_frame.pack(pady=10,padx=30)

    def apply(self):
        # 當用戶按下確定時處理數據
        pass

    def buttonbox(self):
        # Add custom buttons (overriding the default buttonbox)
        box = ttk.Frame(self)
        self.ok_button = tk.Button(box, text="確定", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        box.pack()

    def ok(self):
        # Override the ok method
        super().ok()


    