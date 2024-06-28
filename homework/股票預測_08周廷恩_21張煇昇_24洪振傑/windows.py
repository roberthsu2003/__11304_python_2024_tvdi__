#自定義 套件
import data_loading as rdata
import datas
from datas import Data
import features
from features.feature import Feature

#python 套件
import tkinter 
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pandas as pd
from numpy import random    #亂數產生
import numpy as np       #數學處理
import matplotlib.pyplot as plt #繪圖
import seaborn as sns

class Window(tkinter.Tk):
    def __init__(self):
        self._stock_id:int=0
        self._stock_data:pd.DataFrame=None
        self._stock_features:list=[]

        super().__init__()
        self.title("stock window")
        self.geometry("800x600")

        style = ttk.Style()
        style.configure("LeftTop.TFrame", background="lightblue")
        style.configure("LeftBottom.TFrame", background="lightgreen")
        style.configure("Right.TFrame", background="lightcoral")

        main_frame=ttk.Frame(self)
        #main_frame的設定 
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=1)
        main_frame.grid_rowconfigure(0, weight=1)
        #左-------------------------------------------------------------------------------------------
        left_frame=ttk.Frame(main_frame)
        #left_frame的設定
        left_frame.grid_rowconfigure(0, weight=1)
        left_frame.grid_rowconfigure(1, weight=1)
        left_frame.grid_columnconfigure(0, weight=1)

        left_top_frame = ttk.Frame(left_frame, style="LeftTop.TFrame")

        self.stock_id_var = tkinter.StringVar()
        ttk.Label(left_top_frame, text="stock_id").grid(row=0,column=0,padx=(10,10),pady=(10,10))
        ttk.Entry(left_top_frame, textvariable=self.stock_id_var).grid(row=0,column=1,padx=(10,10),pady=(10,10))
        ttk.Button(left_top_frame,text="送出",command=self.update_stock_id).grid(row=1,column=1,sticky="se")

        left_top_frame.grid(row=0, column=0, sticky="nsew")

        self.left_bottom_frame = ttk.Frame(left_frame, style="LeftBottom.TFrame")

        self.left_bottom_frame.grid(row=1, column=0, sticky="nsew")

        left_frame.grid(row=0,column=0,sticky="nsew")
        #左-------------------------------------------------------------------------------------------

        #右-------------------------------------------------------------------------------------------
        self.right_frame = ttk.Frame(main_frame, style="Right.TFrame")
        self.right_frame.grid_rowconfigure(0, weight=1)
        self.right_frame.grid_columnconfigure(0, weight=1)

        canvas = tkinter.Canvas(self.right_frame)
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbarx = ttk.Scrollbar(self.right_frame, orient="horizontal", command=canvas.xview)
        scrollbary = ttk.Scrollbar(self.right_frame, orient="vertical", command=canvas.yview)
        scrollbarx.grid(row=1, column=0, sticky="ew")
        scrollbary.grid(row=0, column=1, sticky="ns")
        canvas.configure(xscrollcommand=scrollbarx.set,yscrollcommand=scrollbary.set)

        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        
        self.right_frame.grid(row=0, column=1, sticky="nsew")
        #右-------------------------------------------------------------------------------------------
        main_frame.pack(fill="both", expand=True)
    
    @property
    def stock_id(self):
        return self._stock_id

    def update_stock_id(self):
        try:
            self._stock_id = int(self.stock_id_var.get())
            self.main()

        except ValueError:
            print("Invalid stock ID input")

    def main(self):
        month_num=6
        stock_id=self.stock_id
        file_path='data.csv'

        month_datas=pd.DataFrame()
        original_datas=pd.DataFrame()
        #檢查是否檔案下載了
        if rdata.Check_Data_Csv():
            print("csv 已經存在")
            month_datas = pd.read_csv(file_path)
        else:
            print("下載檔案")
            original_datas:pd.DataFrame=rdata.Get_N_Month_Data(month_num=month_num,stock_id=stock_id)
            

            #將該網站的日期從str -> datetime
            # month_datas['日期'] = month_datas['日期'].apply(datas.parse_custom_date)

            #特徵值使用
            window=20
            sma:pd.DataFrame = Feature().Calculate_Moving_Average(data=original_datas, window=window)
            original_datas=sma

            rsi:pd.DataFrame= Feature().Calculate_Rsi(data=original_datas,window=window)
            original_datas=rsi

            num_std=2
            original_datas:pd.DataFrame=Feature().Calculate_Bollinger_Bands(data=original_datas,window=window,num_std=num_std)
            
            
            month_datas=original_datas.drop(columns=['Date'])
            # 將 month_datas 寫入 data.csv
            month_datas.to_csv('data.csv', index=False)
        
        self._stock_data=month_datas

        self.create_checkbuttons()
        self.boxplot_features()
        self.distplot_features()

    def create_checkbuttons(self):
        for widget in self.left_bottom_frame.winfo_children():
            widget.destroy()

        check_vars = []
        features = self._stock_data.keys()
        for i, feature in enumerate(features):
            var = tkinter.BooleanVar()
            checkbutton = ttk.Checkbutton(self.left_bottom_frame, text=feature, variable=var)
            checkbutton.grid(row=i, column=0, sticky="w")
            check_vars.append((feature,var))

        ttk.Button(self.left_bottom_frame,text="確認",command=self.choosen_features).grid(row=len(features), column=0, sticky="w")

        self._stock_features=check_vars

    def choosen_features(self):
        self.boxplot_features()
        self.distplot_features()

    def get_selected_features(self):
        return [feature for feature, var in self._stock_features if var.get()]

    #畫盒鬚圖
    def boxplot_features(self):
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()
        selected_features = self.get_selected_features()
        for i, fea in enumerate(selected_features):
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.boxplot(self._stock_data[fea], showmeans=True)
            ax.set_title(fea)

            canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=0, column=i, sticky="nsew")
            self.scrollable_frame.grid_columnconfigure(i, weight=1)

    #畫常態圖
    def distplot_features(self):
        selected_features = self.get_selected_features()
        for i, fea in enumerate(selected_features):
            fig, ax = plt.subplots(figsize=(6, 4))
            sns.distplot(self._stock_data[fea], ax=ax, hist=True, kde=True, rug=False, bins=20,
                         hist_kws={'edgecolor': 'black'}, kde_kws={'linewidth': 2})
            ax.set_title(fea)

            canvas = FigureCanvasTkAgg(fig, master=self.scrollable_frame)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=i, sticky="nsew")
            self.scrollable_frame.grid_rowconfigure(i, weight=1)


        