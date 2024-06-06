## 0604 作業 issue#192

[HW_issue192 連結](https://github.com/NoktoX/__11304_python_2024_tvdi__/blob/main/homework/%E9%99%B3%E8%90%B1/issue192/issue192.ipynb)

### 讀取檔案
```python
from pprint import pprint 

def download_json()->dict[any]:
    aqi_url = "	https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    try:
        response = requests.get(aqi_url)
    except Exception:
        raise Exception("連線失敗") 
        
    else:
        if response.status_code == 200:
            try:
                all_data:dict[any] = response.json()  
                return all_data

            except JSONDecodeError:
                raise Exception("api_key為測試用,連線已至上限,稍後在試")
        else:
            raise Exception("下載狀態碼不是200")
```

### 執行
```python
try:
    all_data: dict = download_json()
    pprint(all_data[0])
    
except Exception as error:
    print(error)
```

```python
from pydantic import BaseModel, RootModel, Field

class Info(BaseModel):
    sna:str
    sarea:str
    mday:str
    ar:str
    act:str
    updateTime:str
    total:int
    rent_bikes:int = Field(alias="available_rent_bikes")
    lat:float = Field(alias="latitude")
    lng:float = Field(alias="longitude")
    retuen_bikes:int = Field(alias="available_return_bikes")

class Youbike_Data(RootModel):
    root:list[Info]
youbike_data:Youbike_Data = Youbike_Data.model_validate(all_data)
data = youbike_data.model_dump()
```
### 顯示資料
```python
data
```