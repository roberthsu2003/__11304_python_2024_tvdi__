# data.py
import requests
from requests import Response
from pydantic import BaseModel, Field, RootModel

# 資料加載函數
def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    try:
        res: Response = requests.get(url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data: list = res.json()
        return all_data

class Info(BaseModel):
    sna: str  # 站點名稱
    sarea: str  # 行政區
    mday: str  # 資料更新時間
    ar: str  # 地址
    act: str  # 營運狀態
    updateTime: str  # 資料更新時間
    total: int  # 總車位數
    rent_bikes: int = Field(alias="available_rent_bikes")  # 可租借車輛數
    lat: float = Field(alias="latitude")  # 緯度
    lng: float = Field(alias="longitude")  # 經度
    return_bikes: int = Field(alias="available_return_bikes")  # 可歸還車輛數

class Youbike_Data(RootModel):
    root: list[Info]

def load_data() -> list[dict]:
    all_data: list = __download_json()
    youbike_data: Youbike_Data = Youbike_Data.model_validate(all_data)
    return youbike_data.root
