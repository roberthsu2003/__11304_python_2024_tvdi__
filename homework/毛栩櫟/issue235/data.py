import requests
from requests import Response
from pydantic import BaseModel, RootModel, Field,field_serializer

def __download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res:Response = requests.get(url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data:dict[any] = res.json()
        return all_data
    

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
    return_bikes:int = Field(alias="available_return_bikes")

    @field_serializer('sna')
    def serialize_split(self,value:str) -> str:
        return value.split("_")[-1] #將資料從"_"處切割，並且只留右邊的資料
    
    @field_serializer("act")
    def serialize_act(self,value:bool) -> str:
        if bool:
            return "營業中"
        else :
            return "維護中"

class Youbike_Data(RootModel):
    root:list[Info]

def load_data()->list[dict]:
    try:
        all_data:dict[any] = __download_json()
    except Exception as error:
        print(error)
        
    youbike_data:Youbike_Data = Youbike_Data.model_validate(all_data)
    data = youbike_data.model_dump()
    return data