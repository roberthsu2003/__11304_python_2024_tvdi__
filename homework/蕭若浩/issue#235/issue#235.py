import MLproject_Solar_Irradiance.weather.data as data
import tkinter as tk
from tkinter import ttk
from ttkthemes import ThemedTk

try:
    ubike_data:list[dict]=data.load_data()
except Exception as error:
    print(error)

ubike=tk.Tk()
ubike.title("全國ubike資料")
# ubike.geometry("1000x400")

#設定column
column=('#1','#2','#3','#4','#5','#6','#7','#8','#9','#10','#11')
tree=ttk.Treeview(ubike,columns=column,show='tree headings')

#設定heading
tree.heading('#0',text='站點編號')
tree.heading('#1',text='站名')
tree.heading('#2',text='區域')
tree.heading('#3',text='地段')
tree.heading('#4',text='經度')
tree.heading('#5',text='緯度')
tree.heading('#6',text='回傳時間')
tree.heading('#7',text='接收時間')
tree.heading('#8',text='啟用狀態')
tree.heading('#9',text='總車位數')
tree.heading('#10',text='可借車輛數')
tree.heading('#11',text='可還車輛數')

contents=[]
for n in range((len(ubike_data))):
    contents.append((ubike_data[n]["sna"],
                    ubike_data[n]["sarea"],
                    ubike_data[n]["ar"],
                    ubike_data[n]["lng"],
                    ubike_data[n]["lat"],
                    ubike_data[n]["mday"],
                    ubike_data[n]["updateTime"],
                    ubike_data[n]["act"],
                    ubike_data[n]["total"],
                    ubike_data[n]["rent_bikes"],
                    ubike_data[n]["return_bikes"]))

i=1
for content in contents:
    tree.insert('',tk.END,text=i, values=content)
    i+=1

tree['height']=20

tree.grid()
ubike.mainloop()