import requests


r = requests.post("http://127.0.0.1:8000/hello")
print(r)
print(r.text)


r = requests.post("http://127.0.0.1:8000/hello", headers={"USER": "Tom"})
print(r)
print(r.text)
