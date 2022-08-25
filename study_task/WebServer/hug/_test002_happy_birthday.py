import requests


def test_happy_birthday():
    r = requests.get("http://localhost:8000/happy_birthday?name=Coyi&age=31")
    print()
    print(r.status_code)
    print()
    print(r.text)

