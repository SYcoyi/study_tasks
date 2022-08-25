"""
基础鉴权の客户端实现
"""

import requests
import base64


s = requests.session()
user, password, error_pwd = "user1", "mypassword", "myErrorPassword"

r1 = requests.get("http://localhost:8000/public")
print(r1)
print("r1:", r1.text)

r2 = requests.get("http://localhost:8000/authenticated")
print(r2)
print("r2:", r2.text)

r22 = requests.get(f"http://user1:mypassword@localhost:8000/authenticated")    # 用户名和密码在url中的写法
print(r22)
print("r22: ", r22.text)

r3 = requests.get("http://localhost:8000/authenticated", auth=("user1", "mypassword"))
print(r3)
print("r3:", r3.text)

r4 = requests.get("http://localhost:8000/authenticated", auth=("user2", "mypassword"))  # 直接在get里面加auth(最终还是在header里)
print(r4)
print("r4:", r4.text)

s.auth = user, password
r5 = s.get("http://localhost:8000/authenticated")   # 使用session函数，将auth添加进该函数
print(r5)
print("r5:", r5.text)

s.auth = user, error_pwd
r6 = s.get("http://localhost:8000/authenticated")
print(r6)
print("r6:", r6.text)


s.auth = None
raw = f"{user}:{password}"
print(raw)
encoded = base64.b64encode(raw.encode("utf-8")).decode("utf-8")    # 先对用户名和密码进行编码，再放进header中
print(base64.b64encode(raw.encode("utf-8")))
print(encoded)
s.headers["Authorization"] = f"Basic {encoded}"    # 直接操作header，在header Authorization中使用Basic基本授权的方式进行登录
print(s.headers["Authorization"])
r7 = s.get("http://localhost:8000/authenticated")
print(r7)
print("r7:", r7.text)
