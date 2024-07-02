import psycopg2
import data
data.load_data()
all_data:list[dict]=data.load_data()

conn=psycopg2.connect("postgresql://tvdi_09yy_user:XIo11qROxXzCLwzG2n8bsYnIH9aOv2k8@dpg-cpsctgt6l47c73e3hdr0-a.singapore-postgres.render.com/tvdi_09yy")    #建立連線
with conn:
    with conn.cursor() as cursor:
        sql='''
        create table if not exists youbike(
	    _id serial Primary key,
	    sna varchar(50) not null,
	    ar varchar(100),
	    sarea varchar(50),
	    mday timestamp,
	    updatetime timestamp,
	    total smallint,
	    rent_bikes smallint,
	    return_bikes smallint,
	    lat real,
	    lng real,
        act bool,
        unique(sna,updatetime)
        ) ;
        '''
        cursor.execute(sql)
    with conn.cursor() as cursor:
        insert_sql='''
        insert into youbike(sna,sarea,ar,mday,updatetime,total,rent_bikes,return_bikes,lat,lng)
        values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) 
        on conflict (sna,updatetime) do nothing;
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
conn.close()    #斷開連線