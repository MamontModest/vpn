import sqlite3
con = sqlite3.connect("vpn.db")
cur = con.cursor()
cur.execute("select * from free")
for i in cur.fetchall():
    print(i)

cur.execute("create table payments(uid,pay_url, bill_id, response)")
con.commit()
cur.execute("create table free(link,status)")
con.commit()
cur.execute("create table info(uid,balance)")
con.commit()
