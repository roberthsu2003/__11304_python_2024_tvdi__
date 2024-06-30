import psycopg2  
import ubikedata

def main():
    # 建立連線
    conn = psycopg2.connect("postgresql://tvdi_2ddg_user:Fya25QbuhhKZxhnj53WkHm3vsIsDVd35@dpg-cpsct1t6l47c73e3h8e0-a.singapore-postgres.render.com/tvdi_2ddg")

    with conn: #with conn會自動commit()
        # 建立cursor, CREATE TABLE
        with conn.cursor() as cursor: # as cursor自動close()
    
            sql = '''
                CREATE TABLE IF NOT EXISTS youbike (
                    _id Serial Primary Key,
                    sna VARCHAR(50) NOT NULL,
                    sarea VARCHAR(50),
                    ar VARCHAR(100),
                    mday TIMESTAMP,
                    updatetime TIMESTAMP,
                    total SMALLINT,
                    rent_bikes SMALLINT,
                    return_bikes SMALLINT,
                    lat REAL,
                    lng REAL,
                    act BOOLEAN,
                    UNIQUE (sna, updatetime)
                );
            '''
            cursor.execute(sql)
            
        all_data:list[dict] = ubikedata.load_data()
        with conn.cursor() as cursor:  # as cursor自動close()
            # 建立cursor, 寫入資料
            insert_sql = '''
                INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes, return_bikes, lat, lng, act)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)  
                
            '''
            
            for site in all_data:
                
                cursor.execute(insert_sql , (
                    site['sna'],
                    site['sarea'],
                    site['ar'],
                    site['mday'],
                    site['updateTime'],
                    site['total'],
                    site['rent_bikes'],
                    site['return_bikes'],
                    site['lat'],
                    site['lng'],
                    site['act']
                ))
                
    conn.close()

if __name__ == "__main__":
    main()