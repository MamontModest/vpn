import sqlite3
con = sqlite3.connect("vpn.db")
cur = con.cursor()
cur.execute('create table referal (uid,ref)')
con.commit()
cur.execute('select * from referal')
print(cur.fetchall())
con.commit()
cur.execute('select * from all_info')
print(cur.fetchall())
cur.execute('select * from plateji')
print(cur.fetchall())
cur.execute("create table plateji(uid,id_plateja,summa)")
con.commit()
cur.execute("create table all_info(uid,keys,key_id,periods)")
con.commit()
cur.execute('select * from all_info')
print(cur.fetchall())








