

import requests
import json



date_1 = {'mobile_phone':15926546346,'pwd':'123456788'}
# print(type(date_1))
d = json.dumps(date_1)
print(type(d))
res = requests.sessions.session()
headers = {"X-Lemonban-Media-Type":"lemonban.v2","Content-Type":"application/json"}
r = res.request(method="POST",url='http://api.lemonban.com/futureloan/member/login',data=d,headers=headers)
print(r.json()['msg'])
# print(r.text)
# date_dice = json.loads(r.text)
# print(date_dice["msg"])
# print(type(r.text))
# print(r.text)

# print(res_login.text)