# issue164

> [issue164連結](./issue164.ipynb)

> ### 讀檔
```
with open("data.json",mode="r",encoding="utf-8") as file:
    data:str=file.read()
```

> ### 資料結構
```
class Project(BaseModel):
    name:str
    status:str

class Address(BaseModel):
    street:str
    city:str
    zipcode:str

class Root(BaseModel):
    name:str
    age:int
    address:Address
    projects:list[Project]
```

> ### 轉檔
```
try:
    r1:Root=Root.model_validate_json(data)
except ValidationError as e:
    print(e)
else:
    print(r1.model_dump())
```