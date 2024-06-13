#輸出時field_serializer 更改格式
from pydantic import RootModel,BaseModel,field_serializer
#datetime 的使用格式
from datetime import datetime

class Info(BaseModel):
    sna:str
    sarea:str
    mday:datetime
    ar:str
    act:bool
    updateTime:datetime
    total:int
    available_rent_bikes:int
    latitude:float
    longitude:float
    available_return_bikes:int

    @field_serializer("mday","updateTime")
    def serialize_str(self,value:datetime) -> str:
        return value.strftime('%Y-%m-%d %p%I:%M:%S')
    
    @field_serializer("sna")
    def serialize_split(self,value:str) -> str:
        return value.split("_")[-1]
    
    @field_serializer("act")
    def serialize_act(self,value:bool) -> str:
        if bool:
            return "營業中"
        else:
            return "維護中"

class Youbike_Data(RootModel):
    root:list[Info]
    
def GetData(data):
    youbike_data=Youbike_Data.model_validate(data)
    data = youbike_data.model_dump()

    return data