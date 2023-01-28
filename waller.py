from PyEasyQiwi import QiwiConnection
from db import delete_platej
from clients import data_limit
import sqlite3
import time
def times(x):
    a=str(x)
    day=int((int(a.split('-')[0]) - 2023) * 365 + int(a.split('-')[1]) * 30 + int(a.split('-')[2]))
    return day
api_key = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjJ0dDUyaS0wMCIsInVzZXJfaWQiOiI3OTgxMDE3ODcwNiIsInNlY3JldCI6ImY0Mzc4MDBhZDdlM2E3ZGUwYTcxNmEwN2QyY2JlZGFlYzE3NzIwMmFhYTU5NjI1NGM3MjQwZWVjN2Y5MThiMjQifX0="
qiwi = QiwiConnection(api_key)
con = sqlite3.connect("vpn.db")
cur = con.cursor()
while True:
    cur.execute('select * from plateji')
    time.sleep(5)
    for i in cur.fetchall():
        try:
            status,responce=qiwi.check_bill(str(i[0])+':'+i[1])
            uid = i[0]
            if status == 'PAID':
                suma = i[2]
                if suma == 149:
                    uid=i[0]
                    cur.execute(f'SELECT * FROM all_info WHERE uid = {uid}')
                    con.commit()
                    all_info=cur.fetchone()
                    key_id=all_info[2]
                    data_limit(key_id,400000000000)
                    cur.execute(f'select periods from all_info  WHERE uid = {uid}')
                    con.commit()
                    day_to = cur.fetchone()[0]
                    cur.execute(f'select id_plateja from plateji  WHERE uid = {uid}')
                    con.commit()
                    now_day = times(cur.fetchone()[0])
                    cur.execute(f'update  all_info set periods=(?)   WHERE uid = {uid}',[max(now_day,day_to)+30])
                    con.commit()
                    delete_platej(uid)
                    con.commit()
                    print('ex')
                elif suma ==349:
                    uid = i[0]
                    cur.execute(f'SELECT * FROM all_info WHERE uid = {uid}')
                    con.commit()
                    all_info = cur.fetchone()
                    key_id = all_info[2]
                    data_limit(key_id, 400000000000)
                    cur.execute(f'select periods from all_info  WHERE uid = {uid}')
                    con.commit()
                    day_to = cur.fetchone()[0]
                    cur.execute(f'select id_plateja from plateji  WHERE uid = {uid}')
                    con.commit()
                    now_day = times(cur.fetchone()[0])
                    cur.execute(f'update  all_info set periods=(?)   WHERE uid = {uid}', [max(now_day, day_to) + 90])
                    print((now_day, day_to))
                    con.commit()
                    delete_platej(uid)
                    con.commit()
                    print('ex')
                elif suma == 999:
                    uid = i[0]
                    cur.execute(f'SELECT * FROM all_info WHERE uid = {uid}')
                    con.commit()
                    all_info = cur.fetchone()
                    key_id = all_info[2]
                    data_limit(key_id, 400000000000)
                    cur.execute(f'select periods from all_info  WHERE uid = {uid}')
                    con.commit()
                    day_to = cur.fetchone()[0]
                    cur.execute(f'select id_plateja from plateji  WHERE uid = {uid}')
                    con.commit()
                    now_day = times(cur.fetchone()[0])
                    cur.execute(f'update  all_info set periods=(?)   WHERE uid = {uid}', [max(now_day, day_to) + 360])
                    print((now_day, day_to))
                    con.commit()
                    delete_platej(uid)
                    con.commit()
                    print('ex')
            if status == 'EXPIRED' or status == 'REJECTED':
                delete_platej(uid)
            elif status == 'WAITING':
                pass
        except:
            print('eror')





