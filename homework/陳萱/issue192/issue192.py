import requests
from requests import JSONDecodeError
from pydantic import BaseModel, RootModel, Field, field_validator
from pprint import pprint


def download_json() -> list[dict]:
    YouBike_url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"
    try:
        response = requests.get(YouBike_url)
    except Exception:
        raise Exception("Invalid Connection")
    else:
        if response.status_code == 200:
            try:
                all_data:list[dict] = response.json()
                return all_data
            except JSONDecodeError:
                raise Exception("This api_key is for testing and you have exceeded max retries. Try again later.")
        else:
            raise Exception("Download Failed")

try:
    all_data:list[dict] = download_json()
    pprint(all_data)
except Exception as error:
    print(error)


class Site(BaseModel):
    site_name:str = Field(alias='sna')
    site_area:str = Field(alias='sarea')
    mday:str
    address:str = Field(alias='ar')
    act:str
    updateTime:str
    total_bikes:int = Field(alias='total')
    rent_bikes:int = Field(alias='available_rent_bikes')
    latitude:float
    longitude:float
    return_bikes:int = Field(alias='available_return_bikes')


class Bike(RootModel):
    root:list[Site]

bike:Bike = Bike.model_validate(all_data)
data = bike.model_dump()

pprint(data)