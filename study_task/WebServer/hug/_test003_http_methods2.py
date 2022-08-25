import requests

payload = {"name": "Coyi", "age": 18}
# r = requests.post("http://localhost:8000/hello_user", data=payload)
# print(r.status_code)
# print(r.text)
#
# r = requests.post("http://localhost:8000/hello_user?name=Coyi&age=20")
# print(r.status_code)
# print(r.text)
#
# r = requests.post("http://localhost:8000/hello_user?name=Coyi111", data=payload)
# print(r.status_code)
# print(r.text)

r = requests.put("http://localhost:8000/hello_put", data=payload)
print(r.status_code)
print(r.text)


"""
如上三种都可以获取到结果，为什么会这样呢？
因为服务端并没有做限制。
在服务端我们只是定义了这个服务需要哪些参数，而这些参数到底是从post请求体里传进来的还是从请求头里传进来的，并没有进行专门的定义。
我们也没有定义这个方法的请求体一定要是json。
所以，结果就是就算不用json传请求，一样可以把请求正确的发给服务器。
这个和服务端代码是用什么框架实现的没有关系，除非服务端程序中专门加上了检查。
"""