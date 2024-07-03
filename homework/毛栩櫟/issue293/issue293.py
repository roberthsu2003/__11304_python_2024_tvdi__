import data
import psycopg2
import os
from dotenv import load_dotenv
load_dotenv()
data.load_data()
all_data:list[dict]=data.load_data()
conn=psycopg2.connect(os.environ['POSTGRESQL_TOKEN'])    #建立連線
with conn:
    with conn.cursor() as cursor:
        sql='''
        create table if not exists youbike(
	    _id serial Primary key,
	    sna varchar(50) not null unique,
	    ar varchar(100),
	    sarea varchar(50),
	    mday timestamp,
	    updatetime timestamp,
	    total smallint,
	    rent_bikes smallint,
	    return_bikes smallint,
	    lat real,
	    lng real
        );
        '''
        cursor.execute(sql)
conn.close()    #斷開連線

conn=psycopg2.connect("postgresql://tvdi_09yy_user:XIo11qROxXzCLwzG2n8bsYnIH9aOv2k8@dpg-cpsctgt6l47c73e3hdr0-a.singapore-postgres.render.com/tvdi_09yy")
with conn:
    with conn.cursor() as cursor:
        insert_sql='''
        insert into youbike(sna,sarea,ar,mday,updatetime,total,rent_bikes,return_bikes,lat,lng)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        on conflict (sna) do update 
        set sna=excluded.sna,
            sarea=excluded.sarea,
            ar=excluded.ar,
            mday=excluded.mday,
            updatetime=excluded.updatetime,
            total=excluded.total,
            rent_bikes=excluded.rent_bikes,
            return_bikes=excluded.return_bikes,
            lat=excluded.lat,
            lng=excluded.lng
        where youbike.updatetime != excluded.updatetime;
        '''
        for site in all_data:
            cursor.execute(insert_sql,(site['sna'],
                                    site['sarea'],
                                    site['ar'],
                                    site['mday'],
                                    site['updateTime'],
                                    site['total'],
                                    site['rent_bikes'],
                                    site['return_bikes'],
                                    site['lat'],
                                    site['lng']))
conn.close()