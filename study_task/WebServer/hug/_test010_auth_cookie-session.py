import requests


s = requests.Session()

# 未登录调用鉴权接口
r = s.post("http://127.0.0.1:8000/authenticated")
print(r)
print(r.text)
print(r.cookies.get('session-id'))
print(s.cookies.get('session-id'))


payload = {
    "username": "user4",
    "password": "pwd"
}
r = s.post("http://127.0.0.1:8000/login", data=payload)
print(r)
print(r.text)
print(r.cookies.get('session-id'))
print(s.cookies.get('session-id'))


r = s.post("http://127.0.0.1:8000/authenticated", data=payload)
print(r)
print(r.text)   # "Successfully authenticated user = user4"
print(r.cookies.get('session-id'))
print(s.cookies.get('session-id'))