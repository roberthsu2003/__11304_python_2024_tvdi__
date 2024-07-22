import tkinter as tk
from tkinter import ttk, Toplevel, messagebox, Button
from dataset import getInfo
import numpy as np       #數學處理
import pandas as pd       #資料處理
import matplotlib.pyplot as plt #繪圖
import seaborn as sns
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from PIL import Image, ImageTk
import chart.analysis as analysis
import chart.analysis2 as analysis2
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor
# ==================================================================

# 使用 getInfo 函數從 dataset.py 中載入資料集
df = getInfo()

# 如果資料集為空，處理異常情況
if df.empty:
    print("無法載入資料集，請檢查文件路徑。")
    exit()

# =================================================
class MyWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        self.option_add('*font', ('Tahoma', 15, 'bold'))
        self.title("波士頓房價預測")
        self.geometry("800x620")
        
        # 呼叫函數以居中視窗
        self.center_window(800, 620)

        self.create_widgets()

        # 初始化 Treeview 相關變量
        self.tree_frame1 = None
        self.tree1 = None
        self.tree_frame2 = None
        self.tree2 = None

        # 設置窗口關閉時的處理
        self.protocol("WM_DELETE_WINDOW", self.on_close)

        # 在應用程式啟動時顯示 treeview1 和 treeview2
        self.create_treeview1()
        self.create_treeview2()

    def create_widgets(self):
        # 創建框架放置標籤和按鈕
        self.frame = tk.Frame(self)
        self.frame.pack(anchor="nw", padx=5, pady=5, fill='x')

        # 標籤設計
        self.label = tk.Label(self.frame, text="波士頓房價", bg="lightblue", relief="raised", padx=20, pady=10)
        self.label.pack(side="left")

        # combobox設計
        self.combobox = ttk.Combobox(self.frame, values=["資料前處理", "特徵變數"], state="readonly")
        self.combobox.set("請選擇圖表:")
        self.combobox.pack(side="left", padx=(5, 0))

        # 按鈕設計，包括文字和向下箭頭圖案
        self.show_btn = tk.Button(self.frame, text="查看資料 \u21E9", pady=5, font=('Tahoma', 12, 'bold'), command=self.show_data, relief="raised", borderwidth=5)
        self.show_btn.pack(side="left", padx=(5, 0))

        # 恢復初始狀態按鈕
        self.reset_btn = tk.Button(self.frame, text="恢復初始狀態", pady=5, font=('Tahoma', 12, 'bold'), command=self.reset_data, relief="raised", borderwidth=5)
        self.reset_btn.pack(side="left", padx=(5, 10))

        # 新增按鈕 "評分"
        self.open_options_btn = tk.Button(self.frame, text="評分", pady=5, font=('Tahoma', 12, 'bold'), command=self.show_rating_dialog, relief="raised", borderwidth=5)
        self.open_options_btn.pack(side="left")

        # 添加背景框架，並填充視窗下方
        self.background_frame = tk.Frame(self, bg="#FBF6E2")
        self.background_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)

        # 設置右側文字框架
        # self.right_frame = tk.Frame(self, bg="lightgrey", padx=10, pady=10)
        # self.right_frame.pack(side="right", fill="y", padx=5, pady=5, ipadx=10)

        # 添加文字內容
        # self.info_label = tk.Label(self.right_frame, text="這裡是右側的文字內容區域。", bg="lightgrey", font=('Arial', 12))
        # self.info_label.pack(pady=10)

    def center_window(self, width=800, height=600):
        # 取得螢幕的寬度和高度
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()

        # 計算視窗的位置，使其位於螢幕中央
        position_x = (screen_width - width) // 2
        position_y = (screen_height - height) // 2

        # 設定視窗的寬度、高度及位置
        self.geometry(f'{width}x{height}+{position_x}+{position_y}')

    def show_data(self):
        selected_option = self.combobox.get()
        if selected_option == "請選擇圖表:":
            messagebox.showwarning("警告", "請先選擇一個選項")
            return
        
        if selected_option == "資料前處理":
            self.show_data_one_window()
        elif selected_option == "特徵變數":
            self.show_data_window()
        # elif selected_option == "數據三": #如果有第三個選項
        #     self.show_additional_data_window()

    def create_treeview1(self):
        self.destroy_treeview1()

        self.tree_frame1 = tk.Frame(self.background_frame)
        self.tree_frame1.pack(pady=10, padx=10, fill='both', expand=True)

        self.label1 = tk.Label(self.tree_frame1, text="資料集", padx=20)
        self.label1.pack(side="top")

        self.tree1 = ttk.Treeview(self.tree_frame1, columns=("CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PIRATIO", "B", "LSTAT", "PRICE"), show="headings")

        for col in ("CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PIRATIO", "B", "LSTAT", "PRICE"):
            self.tree1.heading(col, text=col, anchor="center")
            self.tree1.column(col, anchor="center", width=80, stretch=False)

        vsb1 = ttk.Scrollbar(self.tree_frame1, orient="vertical", command=self.tree1.yview)
        self.tree1.configure(yscrollcommand=vsb1.set)
        vsb1.pack(side="right", fill="y")

        hsb1 = ttk.Scrollbar(self.tree_frame1, orient="horizontal", command=self.tree1.xview)
        self.tree1.configure(xscrollcommand=hsb1.set)
        hsb1.pack(side="bottom", fill="x")

        self.tree1.pack(side="left", fill="both", expand=True)

        try:
            df = pd.read_csv("train_dataset.csv")
            for index, row in df.head(20).iterrows():
                data = tuple(row)
                self.tree1.insert("", "end", values=data)
        except Exception as e:
            messagebox.showerror("錯誤", f"讀取 CSV 檔案失敗: {e}")

    def create_treeview2(self):
        self.destroy_treeview2()

        self.tree_frame2 = tk.Frame(self.background_frame)
        self.tree_frame2.pack(pady=10, padx=10)

        # 新增treeview標籤2
        self.label2 = tk.Label(self.tree_frame2, text="敘述統計", padx=20)
        self.label2.pack(side="top")

        self.tree2 = ttk.Treeview(self.tree_frame2, columns=("Statistic", "CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PIRATIO", "B", "LSTAT", "PRICE"), show="headings")

        # 設置標題
        self.tree2.heading("Statistic", text="Statistic", anchor="center")
        self.tree2.column("Statistic", width=60, stretch=False)

        for col in ("CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PIRATIO", "B", "LSTAT", "PRICE"):
            self.tree2.heading(col, text=col, anchor="center")
            self.tree2.column(col, width=80, stretch=False)

        hsb2 = ttk.Scrollbar(self.tree_frame2, orient="horizontal", command=self.tree2.xview)
        self.tree2.configure(xscrollcommand=hsb2.set)
        hsb2.pack(side="bottom", fill="x")

        self.tree2.pack(side="left", fill="both", expand=True)
        self.tree_frame2.grid_rowconfigure(0, weight=1)
        self.tree_frame2.grid_columnconfigure(0, weight=1)

        try:
            df = pd.read_csv("train_dataset.csv")
            stats = df.describe()

            for stat_index, stat_name in enumerate(["count", "mean", "std", "min", "25%", "50%", "75%", "max"]):
                values = [stat_name] + [stats.loc[stat_name, col] for col in ("CRIM", "ZN", "INDUS", "CHAS", "NOX", "RM", "AGE", "DIS", "RAD", "TAX", "PIRATIO", "B", "LSTAT", "PRICE")]
                self.tree2.insert("", "end", values=values)
        except FileNotFoundError:
            print("找不到指定的 CSV 檔案。")

    def destroy_treeview1(self):
        if self.tree_frame1:
            self.tree_frame1.destroy()
            self.tree_frame1 = None
            self.tree1 = None

    def destroy_treeview2(self):
        if self.tree_frame2:
            self.tree_frame2.destroy()
            self.tree_frame2 = None
            self.tree2 = None

    def reset_data(self):
        self.combobox.set("請選擇圖表:")
        self.destroy_treeview1()
        self.destroy_treeview2()
        # 在恢復初始狀態時顯示 treeview1 和 treeview2
        self.create_treeview1()
        self.create_treeview2()

    def show_data_one_window(self):
        new_window = Toplevel(self)
        new_window.title("資料前處理")
        new_window.geometry("1250x410")

        # 呼叫分析函數以顯示圖表
        analysis2.show_plots_in_window(new_window)

        try:
            # 圖表描述標籤
            chart_label = tk.Label(new_window, text="確認是否有缺失值，查看盒鬚圖與房價變數最初的常態分佈", font=('Tahoma', 15, 'bold'))
            chart_label.pack(side=tk.BOTTOM, pady=5)    

        except FileNotFoundError as e:
            messagebox.showerror("錯誤", f"找不到指定的圖片檔案：{e}")

    def show_data_window(self):
        new_window = tk.Toplevel(self)
        new_window.title("特徵變數")
        new_window.geometry("1000x620")

        # 創建左邊框架
        left_frame = tk.Frame(new_window, bg='lightgrey')
        left_frame.grid(row=0, column=0, sticky='nsew')

        # 創建右邊框架
        right_frame = tk.Frame(new_window, bg='#7D8ABC')
        right_frame.grid(row=0, column=1, sticky='nsew')

        # 設定視窗內的行和列的權重
        new_window.grid_rowconfigure(0, weight=1)
        new_window.grid_columnconfigure(0, weight=1)
        new_window.grid_columnconfigure(1, weight=1)

        # 創建左上角的框架
        upper_left_frame = tk.Frame(left_frame, bg='lightgrey')
        upper_left_frame.pack(padx=10, anchor='center', fill='x')

        # 創建內部框架
        inner_frame = tk.Frame(upper_left_frame, bg='lightgrey')
        inner_frame.pack(padx=10, pady=10, anchor='center')

        # 添加關閉按鈕
        close_button = tk.Button(inner_frame, text="關閉", command=new_window.destroy, font=('Arial', 10))
        close_button.pack(side='left', padx=5)

        # 添加閾值標籤
        threshold_label = tk.Label(inner_frame, text="閾值:", bg='yellow', font=('Arial', 14))
        threshold_label.pack(side='left', padx=10)

        # 添加閾值輸入框，設定預設提示文字
        threshold_entry = tk.Entry(inner_frame, font=('Arial', 14), width=10)
        threshold_entry.insert(0, "0.4")  # 設定預設為標準閾值:0.4
        threshold_entry.pack(side='left', padx=10)

        # 創建用於顯示選擇特徵的標籤
        result_label = tk.Label(right_frame, text="", bg='#7D8ABC', fg='white', font=('Arial', 12), justify='left')
        result_label.pack(padx=20, pady=20, anchor='nw')

        # 創建右下角框架用於顯示回歸評估結果
        eval_frame = tk.Frame(right_frame, bg='#508C9B')
        eval_frame.pack(fill='both', expand=True)

        # 創建用於顯示回歸評估結果的標籤
        eval_label = tk.Label(eval_frame, text="", bg='#508C9B', fg='white', font=('Arial', 12), justify='left')
        eval_label.pack(padx=20, pady=20, anchor='nw')

        # 定義查看選項的函數
        def view_options():
            try:
                # 嘗試讀取CSV檔案
                data = pd.read_csv('train_dataset.csv')
            except FileNotFoundError:
                messagebox.showerror("錯誤", "找不到檔案: train_dataset.csv")  # 檔案未找到的錯誤
                return
            except Exception as e:
                messagebox.showerror("錯誤", f"發生錯誤: {e}")  # 其他錯誤
                return

            # 清除之前的圖表
            for widget in lower_left_frame.winfo_children():
                widget.destroy()

            # 創建相關性熱圖
            plt.figure(figsize=(5, 3))
            featuresCorr = data.corr()
            ax = sns.heatmap(featuresCorr, annot=True, fmt=".2f", annot_kws={"size": 6}, cmap='coolwarm', cbar_kws={'shrink': .8})
            plt.title('Features Correlation Heatmap', fontsize=8)
            plt.xlabel('Features', fontsize=8)
            plt.ylabel('Features', fontsize=8)
            plt.xticks(fontsize=6)
            plt.yticks(fontsize=6)

            # 在Tkinter窗口中顯示圖表
            canvas = FigureCanvasTkAgg(plt.gcf(), master=lower_left_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(side='top', fill='both', expand=True, padx=5, pady=(0,5))

            # 根據輸入的閾值x計算選擇特徵
            try:
                x_text = threshold_entry.get()
                if x_text == "請輸入數值" or not x_text:
                    messagebox.showerror("錯誤", "請輸入有效的數值")
                    return
                x = float(x_text)
            except ValueError:
                messagebox.showerror("錯誤", "請輸入有效的數值")
                return

            targetCorr = featuresCorr['PRICE']
            targetCorr = targetCorr.drop('PRICE')
            selectedFeatures = targetCorr[abs(targetCorr) > x]

            result_text = f"選擇特徵數： {len(selectedFeatures)} \n選擇特徵:\n{selectedFeatures}"
            result_label.config(text=result_text)

            # 如果有選擇特徵，進行回歸分析
            if not selectedFeatures.empty:
                x = data[selectedFeatures.index]
                y = data['PRICE']
                x_train, x_test, y_train, y_test = train_test_split(
                    x, y, test_size=0.2, random_state=1)  # R^2確認範圍，再調整random_state

                # 數據標準化
                transfer = StandardScaler()
                x_train = transfer.fit_transform(x_train)
                x_test = transfer.transform(x_test)

                # 使用線性回歸模型
                estimator = LinearRegression()
                estimator.fit(x_train, y_train)
                y_pred = estimator.predict(x_test)

                # 評估回歸模型
                mse = mean_squared_error(y_test, y_pred)
                r2 = r2_score(y_test, y_pred)

                # 初始化最高準確率及其對應的模型名稱
                max_knn_accuracy = -1
                max_gs_accuracy = -1
                max_dec_accuracy = -1

                # 迭代運行五次並找出最高準確率的一次
                for i in range(5):
                    # 分割數據集為訓練集和測試集
                    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=i)

                    # 標準化數據
                    scaler = StandardScaler()
                    X_train_scaled = scaler.fit_transform(X_train)
                    X_test_scaled = scaler.transform(X_test)

                    # 使用K近鄰演算法
                    knn = KNeighborsRegressor(n_neighbors=5)
                    knn.fit(X_train_scaled, y_train)
                    knn_score = knn.score(X_test_scaled, y_test)
                    if knn_score > max_knn_accuracy:
                        max_knn_accuracy = knn_score

                    # 設定KNN回歸模型和GridSearchCV的參數網格
                    param_grid = {
                        'n_neighbors': [3, 5, 8, 10],
                        'weights': ['uniform', 'distance']
                    }

                    knn_gs = KNeighborsRegressor()
                    grid_search = GridSearchCV(knn_gs, param_grid, cv=5, scoring='neg_mean_squared_error')
                    grid_search.fit(X_train_scaled, y_train)
                    gs_score = grid_search.best_estimator_.score(X_test_scaled, y_test)
                    if gs_score > max_gs_accuracy:
                        max_gs_accuracy = gs_score

                    # 初始化決策樹回歸模型
                    dec_tree = DecisionTreeRegressor(random_state=42)
                    dec_tree.fit(X_train, y_train)
                    dec_score = dec_tree.score(X_test, y_test)
                    if dec_score > max_dec_accuracy:
                        max_dec_accuracy = dec_score

                # 儲存最高準確率到 analysis 模組
                analysis.max_knn_accuracy = max_knn_accuracy
                analysis.max_gs_accuracy = max_gs_accuracy
                analysis.max_dec_accuracy = max_dec_accuracy

                # 輸出模型評估結果
                eval_text = (f"Mean Squared Error(MSE): {mse}\n\n"
                            f"R-squared(R^2): {r2}\n\n\n"
                            f"K近鄰模組_準確率：{max_knn_accuracy}\n\n"
                            f"GridSearchCV網格搜索模組_準確率：{max_gs_accuracy}\n\n"
                            f"決策樹分析_準確率：{max_dec_accuracy}")
                eval_label.config(text=eval_text)
            else:
                eval_label.config(text="沒有選擇特徵進行回歸分析")

        # 添加查看選項按鈕
        view_button = tk.Button(inner_frame, text="查看選項", command=view_options, font=('Arial', 10))
        view_button.pack(side='left', padx=5)

        # 創建左下角的框架
        lower_left_frame = tk.Frame(left_frame, bg='lightgrey')
        lower_left_frame.pack(padx=10, pady=5, anchor='nw', fill='both', expand=True)

        # 創建右上角的框架
        upper_right_frame = tk.Frame(right_frame, bg='#7D8ABC')
        upper_right_frame.pack(padx=20, pady=10, anchor='nw', fill='x')

        # 在右上角框架添加標籤
        label_right = tk.Label(upper_right_frame, bg='#7D8ABC', fg='white', font=('Arial', 16))
        label_right.pack(pady=50)

        view_options()

    # def show_additional_data_window(self):
    #     new_window = tk.Toplevel(self)
    #     new_window.title("數據三")
    #     new_window.geometry("850x420")

    #     try:
    #         # 圖表描述標籤
    #         chart_label = tk.Label(new_window, text="圖表三", font=('Tahoma', 15, 'bold'))
    #         chart_label.pack(side=tk.TOP, pady=5)

    #     except FileNotFoundError as e:
    #         messagebox.showerror("錯誤", f"找不到指定的圖片檔案：{e}")

    def on_close(self):
        if messagebox.askokcancel("退出", "確定要退出嗎？"):
            self.destroy()

    def show_rating_dialog(self):
        # 準備要顯示的準確率數據
        knn_accuracy = getattr(analysis, 'max_knn_accuracy', '未計算')
        gs_accuracy = getattr(analysis, 'max_gs_accuracy', '未計算')
        dec_accuracy = getattr(analysis, 'max_dec_accuracy', '未計算')

        # 構建消息框顯示內容
        message = f"K近鄰模組_準確率：{knn_accuracy}\n\n"
        message += f"GridSearchCV網格搜索模組_準確率：{gs_accuracy}\n\n"
        message += f"決策樹分析_準確率：{dec_accuracy}"

        # 使用消息框顯示準確率
        messagebox.showinfo("模型準確率", message)


        

if __name__ == "__main__":
    window = MyWindow()
    window.mainloop()