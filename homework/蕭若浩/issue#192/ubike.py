import requests
import json
from requests import Response
from pydantic import BaseModel, RootModel, Field

def dw_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url=url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data:dict[any] = res.json()
        return all_data
    
try:
    all_data:dict[any] = dw_json()
except Exception as error:
    print(error)
    
class Site(BaseModel):
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
    return_bikes:int = Field(alias="available_return_bikes")

class Records(RootModel):
    root:list[Site]

records:Records = Records.model_validate(all_data)
data = records.model_dump()

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
    
with open('data.txt', 'w', encoding='utf-8') as fp:
  json.dump(data, fp, ensure_ascii=False)