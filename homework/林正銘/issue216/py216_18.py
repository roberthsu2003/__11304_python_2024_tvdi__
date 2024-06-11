import tkinter as tk
from tkinter import *
from tkinter import messagebox
import tkinter.messagebox as messagebox
from tkinter import simpledialog, ttk
from ttkthemes import ThemedTk

class CustomMessagebox(tk.Toplevel):
    def __init__(self, parent, title, message, status_color=None):
        super().__init__(parent)
        self.title(title)
        self.message = message
        self.status_color = status_color
        
        self.body()
        self.buttonbox()
        
    def body(self):
        self.message_text = tk.Text(self, font=("Arial", 10), wrap="word", height=5, width=40)
        self.message_text.insert(tk.END, self.message)
        self.message_text.pack(padx=10, pady=10)

        if self.status_color:
            self.message_text.tag_add("status", "2.0", "2.end")
            self.message_text.tag_config("status", foreground=self.status_color)

    def buttonbox(self):
        self.ok_button = ttk.Button(self, text="確定", command=self.destroy)
        self.ok_button.pack(pady=10)

root = Tk()
root.title('BMI專案 歡迎頁面 1 of 3')
#root.iconbitmap('./images/codemy.ico')
root.geometry("350x150")

def show_bmi_result():
    try:
        name = entry_name.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())
        bmi = weight / (height / 100) ** 2
        if bmi < 18.5:
            status = "體重過輕"
            ideal_weight = 18.5 * (height / 100) ** 2
            weight_change = ideal_weight - weight
            status_color = "red"
            advice = f"您需要至少增加 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        elif 18.5 <= bmi <= 24.9:
            status = "正常"
            status_color = "black"
            advice = "您的體重正常，請保持！"
        else:
            status = "體重過重"
            ideal_weight = 24.9 * (height / 100) ** 2
            weight_change = weight - ideal_weight
            status_color = "red"
            advice = f"您需要至少減少 {abs(weight_change):.2f} 公斤才能達到正常體重。"
        
        result_message = f"{name}您好:\n   bmi:{bmi:.2f}\n   體重:{status}\n   建議:{advice}"
        
        # 顯示自定義的msgbox
        if status == "體重過輕" or status == "體重過重":
            dialog = CustomMessagebox(root, title="BMI專案 結果頁面 3 of 3", message=result_message)
        else:
            messagebox.showinfo("BMI結果", result_message)

    except ValueError:
        messagebox.showerror("輸入無效", "請輸入有效的身高和體重數值。")


def clicker():
    global pop
    pop = Toplevel(root)
    pop.title("BMI專案 計算頁面 2 of 3")
    pop.geometry("350x300")
    pop.config(bg="green")
    #global me
    #me = PhotoImage(file="./images/green_1.png")
    global entry_name
    global entry_height
    global entry_weight
    pop_label = Label(pop, text="請輸入姓名/身高/體重",bg="green",fg="white",font=("helvetica", 12))
    pop_label.pack(pady=10)
    
    my_frame = Frame(pop, bg="green")
    my_frame.pack(pady=5)
    
    #my_pic = Label(my_frame, image=me, borderwidth=0)
    #my_pic.grid(row=0,column=0, pady=10)
    
    # 姓名
    label_name = tk.Label(my_frame, text="姓名:", bg="white")
    label_name.grid(row=0, column=0, padx=5, pady=5)

    entry_name = tk.Entry(my_frame)
    entry_name.grid(row=0, column=1, padx=5, pady=5)
    

    # 身高體重
    label_height = tk.Label(my_frame, text="身高 (cm):", bg="white")
    label_height.grid(row=1, column=0, padx=5, pady=5)
  

    entry_height = tk.Entry(my_frame)
    entry_height.grid(row=1, column=1, padx=5, pady=5)
    
    

    label_weight = tk.Label(my_frame, text="體重 (kg):", bg="white")
    label_weight.grid(row=2, column=0, padx=5, pady=5)


    entry_weight = tk.Entry(my_frame)
    entry_weight.grid(row=2, column=1, padx=5, pady=5)
    
        # 計算按鈕設計
    button_calculate = tk.Button(my_frame, text="計算", command=show_bmi_result)
    button_calculate.grid(row=3, columnspan=2, padx=5, pady=5)
    #button_calculate.pack(pady=10)
    '''
    yes = tk.Button(my_frame, text="YES", command=lambda: choice("yes"), bg="orange")
    yes.grid(row=4,column=1)
    
    no = tk.Button(my_frame, text="NO", command=lambda: choice("no"), bg="orange")
    no.grid(row=4,column=2)
    '''
def choice(option):
    global name1
    global height1
    global weight1
    #pop.destroy()
    if option == "yes":
        BMI9 = 25.0
        name1 = entry_name.get()
        height1 = float(entry_height.get())
        weight1 = float(entry_weight.get())
        str1 = "%s您好\n您的身高是%0.1f公分\n體重是%0.1f公斤\nBMI值是%0.1f\n" %(name1, height1, weight1   , BMI9)     
        my_label.config(text=str1)
        '''
        my_frame1 = Frame(pop, bg="yellow")
        my_frame1.pack(pady=5)
        label_height1 = Label(my_frame1, text="XXX您好", bg="white")
        label_height1.grid(row=0, column=0, padx=5, pady=5)
        label_height2 = Label(my_frame1, text="您的體重過重,要注意喔!!!", bg="white")
        label_height2.grid(row=1, column=0, padx=5, pady=5)
        label_height3 = Label(my_frame1, text="需要減重YYY公斤,才會正常喔!!!", bg="white")
        label_height3.grid(row=2, column=0, padx=5, pady=5)
        '''
    else:
        my_label.config(text="You click NO!")
        my_label.config(text="You click NO!")
        my_label.config(text="You click NO!")
        
my_button = Button(root, text="開始進入BMI功能!", command=clicker)
my_button.pack(pady=50)

my_label = Label(root, text="")
my_label.pack(pady=20)

root.mainloop()