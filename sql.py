import sqlite3
con = sqlite3.connect("vpn.db")
cur = con.cursor()
cur.execute("create table all_referals(referal_nickname varchar(50),percent_referal integer,kolichestvo_platejei integer , user_percent)")
con.commit()
cur.execute('create table referal (uid integer,referal_nickname varchar(50),percent_referal integer,kolichestvo_platejei integer , user_percent)')
con.commit()
cur.execute('create table users(uid integer,keys varchar(50),key_id integer,for_date varchar(50))')
con.commit()
cur.execute('create table History_payments (uid integer,referal_nickname varchar(50),payment integer,status integer ,date_of_payment)')
con.commit()
cur.execute("create table active_payments(uid integer,id_plateja varchar(50),for_month varchar(50))")
con.commit()







