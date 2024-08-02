from dotenv import load_dotenv
import psycopg2
from psycopg2.errors import UniqueViolation
from werkzeug.security import check_password_hash
import os
load_dotenv()

class InvalidEmailException(Exception):
    pass

def insert_data(values:list[any]=None):
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql='''
            INSERT INTO 使用者(姓名, 性別, 聯絡電話, 電子郵件, isgetemail,出生年月日, 自我介紹, 密碼, 連線密碼) 
            VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s)
            '''
            try:
                cursor.execute(sql,values)
            except UniqueViolation:
                raise InvalidEmailException
            except Exception:
                raise RuntimeError

    conn.close()
    
def validateUser(email:str,password:str) -> tuple[bool,str]:
    conn = psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            sql ='''
            SELECT 密碼,姓名
            FROM 使用者
            WHERE 電子郵件 = %s
            '''
            cursor.execute(sql,[email])
            searchData:tuple[str, str] | None = cursor.fetchone()
            if searchData:
                hash_password = searchData[0]
                username = searchData[1]
                is_ok = check_password_hash(hash_password,password)
                return  is_ok, username
            else:
                return False,""

             
    conn.close()
