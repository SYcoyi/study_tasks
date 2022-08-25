import requests


url = "http://127.0.0.1:8000/hello"
r = requests.post(url)
print(r)
print(r.text)
print(r.headers)


r = requests.post(url, headers={'USER': 'Tom'})
print(r)
print(r.text)
print(r.headers)
