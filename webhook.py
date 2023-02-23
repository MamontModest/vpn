from flask import Flask,request
import sqlite3
from clients import data_limit
from datetime import datetime,timedelta
app = Flask(__name__)

@app.route('/',methods=['POST'])
def hello_world():
    if request.remote_addr in ['127.0.0.1','185.71.76.0','185.71.76.27','185.71.77.27','185.71.77.0','77.75.153.25','77.75.153.0','77.75.156.11','77.75.156.35','77.75.154.25','77.75.154.128','2a02:5180::/32']:
        if request.json['event']=='payment.succeeded':
            listik = request.json['object']['description'].split('-')
            uid = int(listik[0])
            for_month=listik[1]
            print(uid,for_month)
            value=int(float(request.json['object']['amount']['value']))


            if for_month == '1month':
                con = sqlite3.connect("vpn.db")
                cur = con.cursor()
                cur.execute(f'SELECT * FROM users WHERE uid = {uid}')
                con.commit()
                all_info = cur.fetchone()
                key_id = all_info[2]
                data_limit(key_id, 400000000000)
                day_to = all_info[3]
                now_day = datetime.today().strftime("%Y-%m-%d")
                new_day = (max(datetime.strptime(now_day, "%Y-%m-%d"),
                               datetime.strptime(day_to, "%Y-%m-%d")) + timedelta(days=30)).strftime("%Y-%m-%d")
                cur.execute(f'update  users set for_date=(?)   WHERE uid = {uid}', [new_day])
                con.commit()
                cur.execute('insert into History_payments values(?,?,?,?)', [uid, value, 'OK', now_day])
                con.commit()
                con.close()

            elif for_month == '3month':
                con = sqlite3.connect("vpn.db")
                cur = con.cursor()
                cur.execute(f'SELECT * FROM users WHERE uid = {uid}')
                con.commit()
                all_info = cur.fetchone()
                key_id = all_info[2]
                data_limit(key_id, 400000000000)
                day_to = all_info[3]
                now_day = datetime.today().strftime("%Y-%m-%d")
                new_day = (max(datetime.strptime(now_day, "%Y-%m-%d"),
                               datetime.strptime(day_to, "%Y-%m-%d")) + timedelta(days=90)).strftime("%Y-%m-%d")
                cur.execute(f'update  users set for_date=(?)   WHERE uid = {uid}', [new_day])
                con.commit()
                cur.execute('insert into History_payments values(?,?,?,?)', [uid, value, 'OK', now_day])
                con.commit()
                con.close()



            elif for_month == '12month':
                con = sqlite3.connect("vpn.db")
                cur = con.cursor()
                cur.execute(f'SELECT * FROM users WHERE uid = {uid}')
                con.commit()
                all_info = cur.fetchone()
                key_id = all_info[2]
                data_limit(key_id, 400000000000)
                day_to = all_info[3]
                now_day = datetime.today().strftime("%Y-%m-%d")
                new_day = (max(datetime.strptime(now_day, "%Y-%m-%d"),
                               datetime.strptime(day_to, "%Y-%m-%d")) + timedelta(days=365)).strftime("%Y-%m-%d")
                cur.execute(f'update  users set for_date=(?)   WHERE uid = {uid}', [new_day])
                con.commit()
                cur.execute('insert into History_payments values(?,?,?,?)', [uid, value, 'OK', now_day])
                con.commit()
                con.close()

            return 'succeeded',200
        return  'a',200
    else:
        return 'lol',400

if __name__ == '__main__':
    app.run()