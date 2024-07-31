from dotenv import load_dotenv
import psycopg2
import os
load_dotenv()

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
            searchData:tuple[str, str] = cursor.fetchone()
            database_password = searchData[0]
            username = searchData[1]
            return  password == database_password, username 
    conn.close()
