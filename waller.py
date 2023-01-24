from PyEasyQiwi import QiwiConnection
api_key = "eyJ2ZXJzaW9uIjoiUDJQIiwiZGF0YSI6eyJwYXlpbl9tZXJjaGFudF9zaXRlX3VpZCI6IjJ0dDUyaS0wMCIsInVzZXJfaWQiOiI3OTgxMDE3ODcwNiIsInNlY3JldCI6ImY0Mzc4MDBhZDdlM2E3ZGUwYTcxNmEwN2QyY2JlZGFlYzE3NzIwMmFhYTU5NjI1NGM3MjQwZWVjN2Y5MThiMjQifX0="

conn = QiwiConnection(api_key)
pay_url, bill_id, response = conn.create_bill(value=76.00, description="User1",theme_code='Egor-ChYZVzq4Ixq')
status, response = conn.check_bill(bill_id)
print(pay_url,bill_id,response)
print(status)

