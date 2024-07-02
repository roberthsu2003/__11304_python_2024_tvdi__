# import psycopg2
# import data

# def main():
    
#     conn = psycopg2.connect("postgresql://tvdi_ecbm_user:83RAfDagPTvAhdxU5DSz4jtYS94zr4Lt@dpg-cpscsaaj1k6c738l6hhg-a.singapore-postgres.render.com/tvdi_ecbm")
#     with conn: #with conn會自動commit(),手動close
#         with conn.cursor() as cursor: #自動close()
#             sql = '''
#                 CREATE TABLE IF NOT EXISTS youbike(
#                 _id Serial Primary Key,
#                 sna VARCHAR(50) NOT NULL,
#                 sarea VARCHAR(50),
#                 ar VARCHAR(100),
#                 mday timestamp,
#                 updateTime timestamp,
#                 total SMALLINT,
#                 rent_bikes SMALLINT,
#                 return_bikes SMALLINT,
#                 lat REAL,
#                 lng REAL,
#                 act boolean
#             );
#             '''
#             cursor.execute(sql)

#         all_data:list[dict] = data.load_data()

#         with conn.cursor() as cursor:            
#             insert_sql = '''
#             INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes,return_bikes,lat,lng,act)
#             VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);
#             '''
#             for site in all_data:
#                 cursor.execute(insert_sql,(site['sna'],
#                                 site['sarea'],
#                                 site['ar'],
#                                 site['mday'],
#                                 site['updateTime'],
#                                 site['total'],
#                                 site['rent_bikes'],
#                                 site['return_bikes'],
#                                 site['lat'],
#                                 site['lng'],
#                                 site['act']
#                                 ))
#     conn.close()
        
    

# if __name__ == '__main__':
#     main()

##使用 UNIQUE + ON CONFLICT on youbike table
import psycopg2
import data

def main():
    
    conn = psycopg2.connect("postgresql://tvdi_ecbm_user:83RAfDagPTvAhdxU5DSz4jtYS94zr4Lt@dpg-cpscsaaj1k6c738l6hhg-a.singapore-postgres.render.com/tvdi_ecbm")

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
                    updateTime TIMESTAMP,
                    total SMALLINT,
                    rent_bikes SMALLINT,
                    return_bikes SMALLINT,
                    lat REAL,
                    lng REAL,
                    act BOOLEAN,
                    UNIQUE(sna, updateTime) 
                );
            '''
            cursor.execute(sql)
            
        all_data:list[dict] = data.load_data()
        with conn.cursor() as cursor:  # as cursor自動close()
            # 建立cursor, 寫入資料
            insert_sql = '''
                INSERT INTO youbike(sna, sarea, ar, mday, updateTime, total, rent_bikes, return_bikes, lat, lng, act)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (sna, updateTime) DO NOTHING; 
            '''
            for site in all_data:
                cursor.execute(insert_sql, (site['sna'],
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