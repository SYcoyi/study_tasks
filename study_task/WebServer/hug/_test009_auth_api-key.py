import requests


r = requests.get("http://localhost:8000/key_authenticated")
print(r)
print(r.text)

r = requests.get("http://localhost:8000/key_authenticated", headers={"X-Api-Key": "5F00832B-DE24-4CAF-9638-C10D1C642C6C"})
print(r)
print(r.text)
