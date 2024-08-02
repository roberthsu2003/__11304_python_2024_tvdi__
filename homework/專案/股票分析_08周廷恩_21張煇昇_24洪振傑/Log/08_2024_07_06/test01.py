import tkinter as tk 
from tkinter import ttk
from ttkthemes import ThemedTk
import tkinter.messagebox as msgbox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sklearn.feature_selection import SelectKBest,f_regression
import seaborn as sns
import numpy as np
import features
from features.feature import Feature
import pandas as pd
import matplotlib.ticker as  mticker


class Window(tk.Tk):
    def __init__(self,theme:str=None,**kwargs):
        super().__init__(**kwargs)
        self.title("Test")

        #定義style的名稱
        style = ttk.Style()
        style.configure('Top.TFrame')
        style.configure('Top.TLabel',font=('Helvetica',25,'bold'))

        title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=2,relief='groove')
        ttk.Label(title_frame,text='Stock Forecast',style='Top.TLabel').pack(expand=True,fill='y')
        title_frame.pack(ipadx=100,ipady=10,padx=10,pady=10)

        center_frame  = ttk.Frame(borderwidth=2,relief='groove')
        ttk.Label(center_frame,text='請選擇技術圖',font=('Arial',20,'bold'),foreground='#000').pack(expand=True,fill='y')
        center_frame.pack(fill=tk.BOTH,expand=1,padx=100,pady=50)

        ttk.Button(self,text="Quit",command=self.destroy).pack(side='bottom')
        
      

#按鈕
        func_frame = title_frame = ttk.Frame(self,style='Top.TFrame',borderwidth=1)
        ttk.Label(func_frame,text="請選擇技術圖",font=('Arial',20,'bold'),foreground='#ADD').pack(expand=True,fill='y')
        ttk.Button(center_frame,text='5MA',command=self.click1).pack(side='left',expand=True)
        center_frame.pack(pady=10)
        ttk.Button(center_frame,text='20MA',command=self.click2).pack(side='left',expand=True)
        center_frame.pack(pady=10)
        ttk.Button(center_frame,text='60MA',command=self.click3).pack(side='left',expand=True)
        center_frame.pack(pady=10)

        self.func_frame2  = ttk.Frame(self,borderwidth=1,relief='groove')
        self.func_frame2.pack(pady=10)

        

    def click1(self):
    
        sol=['sma']

        window=5
        original_datas=pd.DataFrame()

        original_datas = pd.read_csv("data.csv")
        original_datas = Feature().Calculate_Moving_Average(data=original_datas, window=window)
        
        self._stock_data=original_datas

        self.distplot_features(0, sol)



    def click2(self):

        sol=['sma']

        window=20
        original_datas=pd.DataFrame()

        original_datas = pd.read_csv("data.csv")
        original_datas = Feature().Calculate_Moving_Average(data=original_datas, window=window)

        self._stock_data=original_datas

        self.distplot_features(0, sol)

        

    def click3(self):
        sol=['sma']

        window=60
        original_datas=pd.DataFrame()

        original_datas = pd.read_csv("data.csv")
        original_datas = Feature().Calculate_Moving_Average(data=original_datas, window=window)

        self._stock_data=original_datas

        self.distplot_features(0, sol)

        

     # 定義自訂圖形函式
    def get_selected_features(self):

            alpha=float(self.alpha_combobox.get())

            data_x = self._stock_data.iloc[:, :-1]
            data_y = self._stock_data.iloc[:, -1]
            n = 16
            chi = SelectKBest(f_regression, k=n)
            arrchi = chi.fit_transform(data_x, data_y)
            score = np.round(chi.scores_,4)
            selected_scores = score[np.abs(score) > alpha]
            scoresort = np.argsort(selected_scores)
            scoresort = np.flipud(scoresort)
            col = self._stock_data.columns

            return col[scoresort]
    
    def clean_right(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

    
    #畫常態圖
    def distplot_features(self,index,selected_features):

        for i, fea in enumerate(selected_features):
            fig, ax = plt.subplots(figsize=(6, 4))
            #     # Assuming ax is your subplot axis
            # ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # 设置日期格式
            # ax.xaxis.set_major_locator(mdates.AutoDateLocator())  # 自动设置日期刻度间隔
            ax.plot(self._stock_data['Date'], self._stock_data['sma'], label='SMA')  # Plot SMA data
            ax.set_xlabel('Date')
            ax.set_ylabel('SMA')
            ax.set_title(fea)
            #x軸處理
            # tick_spacing = ax.set_xlabel['Date'].size/12
            # ax.xaxis.set_major_locator(mticker.MultipleLocator(tick_spacing))

            # canvas = FigureCanvasTkAgg(fig, master=self.func_frame2)
            # canvas.draw()
            # canvas.get_tk_widget().grid(row=index, column=i, sticky="nsew")

             # 調整 X 軸刻度間距
            ax.xaxis.set_major_locator(mticker.AutoLocator())  # 自動設置刻度間距

            canvas = FigureCanvasTkAgg(fig, master=self.func_frame2)
            canvas.draw()
            canvas.get_tk_widget().grid(row=index, column=i, sticky="nsew")
            
         



def main():
    def on_closing():
        window.destroy()
        window.quit()

    window = Window(theme='arc')
    window.protocol("WM_DELETE_WINDOW",on_closing)
    window.mainloop()

if __name__=="__main__":
    main()