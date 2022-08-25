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

s = requests.session()
s.headers["Authorization"] = r.json()["token"]
url = 'http://localhost:8000/token_authenticated'
r = s.get(url)
print(r.request.headers['Authorization'])
print(r)
print(r.text)