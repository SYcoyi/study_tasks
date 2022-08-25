import requests

r1 = requests.get("http://localhost:8000/v1/echo?text=%E4%BD%A0%E5%A5%BD")
print(r1.text)
r2 = requests.get("http://localhost:8000/v2/echo?text=%E4%BD%A0%E5%A5%BD")
print(r2.text)
r3 = requests.get("http://localhost:8000/v3/echo?text=%E4%BD%A0%E5%A5%BD")
print(r3.text)
r4 = requests.get("http://localhost:8000/v4/echo?text=%E4%BD%A0%E5%A5%BD")
print(r4.text)
