import sqlite3
con = sqlite3.connect("vpn.db")
cur = con.cursor()
cur.execute('select * from all_info')
print(len(cur.fetchall()))
cur.execute('select * from plateji')
print(len(cur.fetchall()))
cur.execute("create table plateji(uid,id_plateja,summa)")
con.commit()
cur.execute("create table all_info(uid,keys,key_id,periods)")
con.commit()
cur.execute('select * from all_info')
print(cur.fetchall())








