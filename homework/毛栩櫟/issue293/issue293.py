import data
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
data.load_data()
all_data:list[dict]=data.load_data()

def main():
    conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])
    with conn:
        with conn.cursor() as cursor:
            insert_sql='''
            UPDATE youbike
            set sarea=%s,
                ar=%s,
                mday=%s,
                updatetime=%s,
                total=%s,
                rent_bikes=%s,
                return_bikes=%s,
                lat=%s,
                lng=%s
            WHERE youbike.sna = %s AND youbike.updatetime != %s;
            '''
            for site in all_data:
                cursor.execute(insert_sql,(site['sarea'],
                                        site['ar'],
                                        site['mday'],
                                        site['updateTime'],
                                        site['total'],
                                        site['rent_bikes'],
                                        site['return_bikes'],
                                        site['lat'],
                                        site['lng'],
                                        site['sna'],
                                        site['updateTime']
                                        ))
    conn.close()

if __name__=='__main__':
    main()