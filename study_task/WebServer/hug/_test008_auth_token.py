import requests

url = 'http://localhost:8000/token_generation'
payload = {
    "user": "User2",
    "password": "Mypassword"
}
r = requests.post(url, data=payload)
print(r)
print(r.text)
print()


url = "http://localhost:8000/token_authenticated"
r = requests.get(url, headers={"Authorization": r.json()['token']})  # 这里header里面的"Authorization"是http协议要求的，并由hug底层实现
print(r.request.headers)
print(r)
print(r.text)

