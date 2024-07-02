import psycopg2  # type: ignore
import data

def main():
    conn = psycopg2.connect("postgresql://tvdi_1bpv_user:fx1DSgq1dFkZ1A9xWfFbnuqYLJuHFjDs@dpg-cpscs9g8fa8c739532vg-a.singapore-postgres.render.com/tvdi_1bpv")
    with conn:  # with conn會自動commit(),手動close
        with conn.cursor() as cursor:  # 自動close()
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

        all_data: list[dict] = data.load_data()

        with conn.cursor() as cursor:
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

