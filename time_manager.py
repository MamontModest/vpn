import sqlite3
import time
from telethon.sync import TelegramClient
from clients import data_limit,times
import datetime
from telethon.tl.functions.messages import StartBotRequest
con = sqlite3.connect("vpn.db")
cur = con.cursor()
api_id = '29413118'
api_hash = 'e80eddcc8322873af477a85223fe5d57'
username = 'dsafdafth'
phone=77073292462
client = TelegramClient(username, int(api_id), api_hash)
print(times(datetime.datetime.today()),datetime.datetime.today())
while True:
    con = sqlite3.connect("vpn.db")
    cur = con.cursor()
    cur.execute('select * from all_info')
    con.commit()
    s = cur.fetchall()
    con.close()
    x=times(datetime.datetime.today())
    for i in s:
        time.sleep(2)
        if i[3]-65==0:
            client.start(phone=str(phone))
            client.send_message('god_vpn_bot',str(i[0]))
            client.disconnect()
        if i[3]-65<0:
            data_limit(i[2],0)
            print('done')
    time.sleep(60*60*23.9)