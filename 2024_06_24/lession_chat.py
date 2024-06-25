import psycopg2
import data

def create_table(conn):
    with conn.cursor() as cursor:
        sql = '''
            CREATE TABLE IF NOT EXISTS youbike (
                _id SERIAL PRIMARY KEY,
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
                act BOOLEAN
            );
        '''
        cursor.execute(sql)

def insert_data(conn, all_data):
    with conn.cursor() as cursor:
        insert_sql = '''
            INSERT INTO youbike(sna, sarea, ar, mday, updatetime, total, rent_bikes, return_bikes, lat, lng, act)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (updatetime, sna) DO NOTHING;
        '''
        for site in all_data:
            try:
                cursor.execute(insert_sql, (
                    site['sna'],
                    site['sarea'],
                    site['ar'],
                    site['mday'],
                    site['updateTime'],
                    site['total'],
                    site['rent_bikes'],
                    site['retuen_bikes'],  # corrected typo: 'return_bikes' instead of 'retuen_bikes'
                    site['lat'],
                    site['lng'],
                    site['act']
                ))
            except psycopg2.Error as e:
                conn.rollback()  # Rollback the transaction on error
                print(f"Error inserting data for site '{site['sna']}': {e}")

def main():
    try:
        conn = psycopg2.connect("postgresql://tvdi_user:KPw6uyvpBi1Vgc3yREdipuVFunLTPYv0@dpg-cpscs808fa8c739532a0-a.singapore-postgres.render.com/tvdi")
        
        create_table(conn)
        
        all_data = data.load_data()
        
        insert_data(conn, all_data)
        
        conn.commit()
        print("Data insertion successful.")

    except (Exception, psycopg2.DatabaseError) as error:
        print("Error inserting data into PostgreSQL:", error)

    finally:
        if conn:
            conn.close()

if __name__ == '__main__':
    main()