from tkinter.simpledialog import Dialog
from tkinter import Misc

class CustomMessagebox(Dialog):    
    def __init__(self, parent:Misc, title:str,name:str,bmi:float,status:str,advice:str):
        super().__init__(parent=parent, title=title)
        result_message = f"{name}您好:\n   bmi:{bmi:.2f}\n   體重:{status}\n   建議:{advice}"
        print(result_message)