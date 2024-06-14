import requests
from requests import JSONDecodeError
from pydantic import BaseModel,RootModel,Field,field_validator
from datetime import datetime