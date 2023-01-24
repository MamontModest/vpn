import sqlite3

con = sqlite3.connect("vpn.db")
cur = con.cursor()
def first_time(uid):
    cur.execute(f'SELECT balance FROM info WHERE uid = {uid}')
    if len(cur.fetchall())==0:
        return True
    return False
def create_user(uid):
    cur.execute(f'insert  into info  values({uid},0)')
    con.commit()
def creat_link(uid,pay_url, bill_id, response):
    cur.execute(f'insert  into payments  values({uid},{pay_url},{bill_id},{response})')
    con.commit()
#доделать несколько оплат
def chek_oplacheno(uid):
    cur.execute(f'select  * from payments  where (id={uid}) and (status=PAID)')
    if len(cur.fetchall()) == 0:
        return False
    cur.execute(f'delete * from payments where id={uid}')
    con.commit()
    return True

def select(uid):
    cur.execute(f'SELECT balance FROM info WHERE uid = {uid}')
    balance=cur.fetchone()
    return balance[0]