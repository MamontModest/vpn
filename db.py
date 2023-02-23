import sqlite3


#Работа с таблицей юзерс
def select_key(uid):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute(f'SELECT keys FROM users WHERE uid = {uid}')
    object=cur.fetchone()[0]
    con.commit()
    con.close()
    return 'ss:'+str(object)+':5046/?outline=1'

def select_day(uid):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute(f'SELECT for_date FROM users WHERE uid = {uid}')
    con.commit()
    date=cur.fetchone()[0].split('-')
    con.close()
    return date[2]+" / "+date[1]+' / '+date[0]

def first_time(uid):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute(f'SELECT * FROM users WHERE uid = {uid}')
    con.commit()
    if len(cur.fetchall())==0:
        con.close()
        return True
    con.close()
    return False



def create_user(uid,keys,key_id,period):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute('insert  into  users values (?,?,?,?)',[uid,keys,key_id,period])
    con.commit()
    con.close()


#Работа с рефералами
def select_referal(referal_nickname):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute(f'SELECT * FROM all_referals WHERE referal_nickname = (?)',[referal_nickname])
    object=cur.fetchall()
    con.commit()
    con.close()
    if len(object) == 1:
        return True,object[0]
    return False,False

def create_user_ref(uid,referal_nickname,percent_referal,kolichestvo_platejei,user_percent):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute('insert  into  referal values (?,?,?,?,?)', [uid,referal_nickname,percent_referal,kolichestvo_platejei,user_percent])
    con.commit()
    con.close()


def create_referal(referal_nickname,percent_referal,kolichestvo_platejei,user_percent):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute('insert  into  all_referals values (?,?,?,?)', [referal_nickname,percent_referal,kolichestvo_platejei,user_percent])
    con.commit()
    con.close()


def cupon_payment(uid):
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute(f'SELECT user_percent,kolichestvo_platejei FROM referal WHERE uid = {uid}')
    con.commit()
    object=cur.fetchall()
    con.commit()
    if len(object)==0:
        con.close()
        return False
    else:
        cur.execute(f'SELECT * FROM History_payments WHERE uid = {uid}')
        if len(cur.fetchall())<object[0][1]:
            con.close()
            return object[0][0]
        con.close()
        return False






