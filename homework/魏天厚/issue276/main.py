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
