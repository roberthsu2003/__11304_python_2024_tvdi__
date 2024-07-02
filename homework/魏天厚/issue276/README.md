# 下載youbike的資料,進入postgreSQL的youbike的table，updatetime + sna的2個欄位的值不可以重覆

## [Data.py](./data.py)
```python

import requests
from requests import Response
from pydantic import BaseModel, RootModel, Field, field_validator, ConfigDict, field_serializer
from datetime import datetime

def _download_json():
    url = "https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json"

    try:
        res: Response = requests.get(url)
    except Exception:
        raise Exception("連線失敗")
    else:
        all_data: dict[any] = res.json()
        return all_data
    

class _Info(BaseModel):
    sna: str
    sarea: str
    mday: datetime
    ar: str
    act: str
    updateTime: datetime
    total: int
    rent_bikes: int = Field(alias="available_rent_bikes")
    lat: float = Field(alias="latitude")
    lng: float = Field(alias="longitude")
    retuen_bikes: int = Field(alias="available_return_bikes")

    model_config = ConfigDict(
        populate_by_name=True,
    )

    @field_validator("sna", mode='before')
    @classmethod
    def flex_string(cls, value: str) -> str:
        return value.split(sep="_")[-1]
    
    @field_serializer("mday", "updateTime")
    def datetime_to_str(self, value: datetime) -> str:
        return value.strftime('%Y-%m-%d %H:%M:%S')
    

class _Youbike_Data(RootModel):
    root: list[_Info]

def load_data() -> list[dict]:
    all_data: dict[any] = _download_json()
    youbike_data: _Youbike_Data = _Youbike_Data.model_validate(all_data)
    data = youbike_data.model_dump()
    return data

class FilterData(object):
    @staticmethod
    def get_selected_coordinate(sna: str, data: list[dict]) -> _Info:    
        right_list: list[dict] = list(filter(lambda item: item['sna'] == sna, data))
        data: dict = right_list[0]
        return _Info.model_validate(data)

__all__ = ['load_data', 'FilterData']

```

## [main.py](./main.py)

> ### CONSTRAINT unique_sna_updatetime UNIQUE (sna, updateTime) 

> ### ON CONFLICT (sna, updatetime) DO NOTHING;

```python

import psycopg2
import data

def main():
    
    conn = psycopg2.connect("postgresql://tvdi_et5g_user:rO4f8W7mB0kylH1UvACmrEKJSrznix20@dpg-cpscs956l47c73e3h0bg-a.singapore-postgres.render.com/tvdi_et5g")
    with conn:  # with conn會自動commit(),手動close
        with conn.cursor() as cursor:  # 自動close()
            sql = '''
                CREATE TABLE IF NOT EXISTS youbike(
                _id Serial Primary Key,
                sna VARCHAR(50) NOT NULL,
                sarea VARCHAR(50),
                ar VARCHAR(100),
                mday timestamp,
                updateTime timestamp,
                total SMALLINT,
                rent_bikes SMALLINT,
                return_bikes SMALLINT,
                lat REAL,
                lng REAL,
                act boolean,
                CONSTRAINT unique_sna_updatetime UNIQUE (sna, updateTime)  
            );
            '''
            ## CONSTRAINT unique_sna_updatetime UNIQUE (sna, updateTime) 

            cursor.execute(sql)

        all_data: list[dict] = data.load_data()

        with conn.cursor() as cursor:
            insert_sql = '''
            INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes, return_bikes, lat, lng, act)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (sna, updatetime) DO NOTHING;
            '''

            ## ON CONFLICT (sna, updatetime) DO NOTHING;

            for site in all_data:
                cursor.execute(insert_sql, (
                    site['sna'],
                    site['sarea'],
                    site['ar'],
                    site['mday'],
                    site['updateTime'],
                    site['total'],
                    site['rent_bikes'],
                    site['retuen_bikes'],
                    site['lat'],
                    site['lng'],
                    site['act']
                ))
    conn.close()

if __name__ == '__main__':
    main()
```