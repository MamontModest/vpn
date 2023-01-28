import sqlite3
con = sqlite3.connect("vpn.db")
cur = con.cursor()

def select_key(uid):
    cur.execute(f'SELECT keys FROM all_info WHERE uid = {uid}')
    con.commit()
    return 'ss:'+str(cur.fetchone()[0])+':5046/?outline=1'
def select_day(uid):
    cur.execute(f'SELECT periods FROM all_info WHERE uid = {uid}')
    con.commit()
    return str(cur.fetchone()[0])
def first_time(uid):
    cur.execute(f'SELECT * FROM all_info WHERE uid = {uid}')
    con.commit()
    if len(cur.fetchall())==0:
        return True
    return False
def create_user(uid,keys,key_id,period):
    cur.execute('insert  into  all_info values (?,?,?,?)',[uid,keys,key_id,period])
    con.commit()
def delete_platej(uid):
    cur.execute(f'SELECT * FROM plateji WHERE uid = {uid}')
    object=cur.fetchone()
    cur.execute('delete  from  plateji where uid=(?)', [uid])
    con.commit()
    return str(object[0])+':'+object[1]
def create_platej(uid,id_plateja,summa):
    cur.execute('insert  into  plateji values (?,?,?)', [uid,id_plateja,summa])
    con.commit()
def chek_platej(uid):
    cur.execute(f'SELECT * FROM plateji WHERE uid = {uid}')
    con.commit()
    if len(cur.fetchall()) == 0:
        return True
    return False
#доделать несколько оплат


