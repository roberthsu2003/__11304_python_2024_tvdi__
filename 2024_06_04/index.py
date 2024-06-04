import requests
from  requests import JSONDecodeError
from pprint import pprint
from pydantic import BaseModel,RootModel,Field,field_validator

class Site(BaseModel):
    site_name:str = Field(alias='sitename')
    county:str
    aqi:int
    status:str
    pm25:float = Field(alias='pm2.5')

    @field_validator("pm25",mode='before')
    @classmethod
    def abc(cls, value:str)->str:
        if value=="":
            return "0.0"
        else:
            return value


class Records(RootModel):
    root:list[Site]

def download_json()->dict[any]:
    aqi_url = 'https://data.moenv.gov.tw/api/v2/aqx_p_488?api_key=e8dd42e6-9b8b-43f8-991e-b3dee723a52d&limit=1000&sort=datacreationdate desc&format=JSON'
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
                raise Exception("api_key為測試用,連線已至上限,請稍後再試")
        else:
            raise Exception("下載狀態碼不是200")

def main():
    try:
        all_data:dict[any] = download_json()
    except Exception as error:
        print(error)
    else:
        records:Records = Records.model_validate(all_data['records'])
        data:list[dict] = records.model_dump()
        pprint(data)

if __name__ == '__main__':
    main()