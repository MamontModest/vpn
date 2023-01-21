import sqlite3

con = sqlite3.connect("vpn.db")
cur = con.cursor()
def first_time(uid):
    cur.execute(f'SELECT balance FROM info WHERE uid = {uid}')
    if len(cur.fetchall())==0:
        return False
    return True
def select(uid):
    cur.execute(f'SELECT balance FROM info WHERE uid = {uid}')
    balance=cur.fetchone()
    return balance[0]