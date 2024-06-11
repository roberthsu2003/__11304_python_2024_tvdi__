import os
os.system("cls")
import tools
import tkinter as tk
from tkinter import ttk, Misc, Frame
from ttkthemes import ThemedTk
from tkinter import messagebox
from tkinter.simpledialog import Dialog

class Window(ThemedTk):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.geometry('500x300')
        self.resizable(False,False)
        self.create_widgets()
    
    def create_widgets(self):
        self.iconphoto(True, tk.PhotoImage(file = "./images/BMI_icon.png"))
        self.title("BMI 計算器")
        style = ttk.Style()
        style.configure("TOP.TLabel", font=('Helvetica',25,"bold","italic"))
        title_frame = ttk.Frame(self, borderwidth=2, relief='groove')
        ttk.Label(title_frame, text = "BMI 計算器", style='TOP.TLabel').pack(expand=True, fill="y")
        title_frame.pack(ipadx=100, ipady=30, padx=10, pady=10)
        func_frame =ttk.Frame(self, border=1, relief='groove')
        func_frame.pack()
        
        # name
        name_label = ttk.Label(func_frame, text = "姓名：")
        name_label.grid(row = 0, column=0, sticky=tk.W, padx=5, pady=5)
        self.name_entry = ttk.Entry(func_frame)
        self.name_entry.grid(row = 0, column = 1, sticky=tk.W, padx=5, pady=5)
        self.name_entry.focus()

        # height
        height_label = ttk.Label(func_frame, text = "身高：")
        height_label.grid(row = 1, column=0, sticky=tk.W, padx=5, pady=5)
        self.height_entry = ttk.Entry(func_frame)
        self.height_entry.grid(row = 1, column = 1, sticky=tk.W, padx=5, pady=5)

        # weight
        weight_label = ttk.Label(func_frame, text = "體重：")
        weight_label.grid(row = 2, column=0, sticky=tk.W, padx=5, pady=5)
        self.weight_entry = ttk.Entry(func_frame)
        self.weight_entry.grid(row = 2, column = 1, sticky=tk.W, padx=5, pady=5)

        # calculate
        calculate_button= ttk.Button(func_frame, text = "計算", command =self.click1)
        calculate_button.grid(row = 3, column = 1, padx=5, pady=5, sticky= tk.E)

    def click1(self):
         
        name = self.name_entry.get()
        if name.isspace() is True or len(name) == 0:
            return messagebox.showerror("錯誤","名字不能為空白！")
        elif name.isdigit():
            return messagebox.showerror("錯誤","名字不能為數字")
        try:
            height = int(self.height_entry.get())
            weight = int(self.weight_entry.get())
        except ValueError:
            return messagebox.showerror("錯誤","錯誤，身高體重為數字")
        
        result:list[dict] = tools.dict_info(name, height, weight)
        bmi = result[0]['BMI']

        def bmi_info(value:dict, bmi:float) -> str:
            return f" {value['name']} 您好:\n{'':>8}BMI : {bmi}\n{'':>8}體重:{value['weigh_info']}\n{'':>8}建議:{value['advice']}"
        message_data:list[str] = list(map(lambda value:bmi_info(value, bmi), result))
        message = ''.join(message_data)

        ShowInfo(parent=self, title= "BMI計算結果",message=message, bmi=bmi)

class ShowInfo(Dialog):
    def __init__(self, parent:Misc | None, title: str | None = None, message:str="", bmi:float=0) -> None:
        self.message = message
        self.bmi = bmi
        super().__init__(parent=parent, title=title)

    def body(self, master:Frame) -> Misc | None:
        text = tk.Text(self, height=5, font=('Helvetica', 15), width=45)
        text.pack(padx=10,pady=10)
        text.insert(tk.INSERT, self.message)

        if float(self.bmi) >= 24: 
            # 尋找“體重”文本的起始索引
            start_index = text.search("體重",'1.0',stopindex=tk.END)
            # 找到下一个的索引，作为“體重”文本的结束位置
            end_index = text.search("建議", f"{start_index}", stopindex=tk.END)
            # 應用標籤到“體重”文本, 起始索引, 結束索引
            text.tag_add("體重", start_index, end_index)
            text.tag_config("體重", foreground='red')
        elif float(self.bmi) < 18.5:
            # 尋找“體重”文本的起始索引
            start_index = text.search("體重",'1.0',stopindex=tk.END)
            # 找到下一个的索引，作为“體重”文本的结束位置
            end_index = text.search("建議", f"{start_index}", stopindex=tk.END)
            # 應用標籤到“體重”文本, 起始索引, 結束索引
            text.tag_add("體重", start_index, end_index)
            text.tag_config("體重", foreground='orange')

        text.config(state='disabled')      
        return None
    
    def buttonbox(self) -> None:
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="OK", width=10, command=self.ok)  
        self.ok_button.pack(pady=(20,30), ipady=10)
        box.pack()

    def ok(self):
        print("OK button was clicked!")
        super().ok()  

def main():
   window = Window(theme="arc")
   window.mainloop()

if __name__ == '__main__':
    main()
    
    
    