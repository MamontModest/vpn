import sqlite3
con = sqlite3.connect("vpn.db")
cur = con.cursor()
cur.execute("create table info(uid,balance)")
con.commit()