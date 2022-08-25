import hug

sessions = {}


# 表示服务端保存在内存中的session的集合，是保存的MockSession这个类的实例


class MockSession:
    def __init__(self):
        self.session_id = "5F00832B-DE24-4CAF-9638-C10D1C642C6C"

    def get_session_id(self):
        return self.session_id


"""
MockSession类：
MockSession表示服务端保存在内存中的单个session，有两个方法
__init__方法用来新建session，为了简单所有session都用了同一个session id。正常应该是调用某种算法来计算一个不同的值出来做session id，且该值不应重复
另外真正服务端实现中，session也往往不是用一个字典直接保存在内存中，如Redis等内存型数据库，可以用来保存session。
第二个get_session_id方法用来获取session id
"""


@hug.post("/authenticated")
def cookie_api_call(request, response):   # request & response这两个变量是来源于hug底层的falcon框架。
    session_id = request.cookies.get('session-id')  # 尝试从请求的cookies里面获取session-id
    if sessions.get(session_id):  # 尝试从服务端内存里的sessions字典中查找有没有session-id的这个key值。能找到就鉴权通过
        for k, v in request.cookies.items():  # 鉴权通过后，把请求里带的cookie值全部复制到响应的cookie里。
            response.set_cookie(k, v, domain="127.0.0.1", secure=False)
        return f"Successfully authenticated user = {sessions[session_id].user}"
    else:
        return "Not Authenticated"


# 注意成功后打印出来的user，是根据用户请求的cookie里带的session id，在服务的内存中找到对应的session，然后再读取其中用户信息的用户名部分得到的。


@hug.post("/login")
def login(username, password, response):  # 此处的response是hug服务端给客户端返回的响应对象
    mockusername = "user4"
    mockpassword = 'pwd'
    if mockpassword == password and mockusername == username:
        my_session = MockSession()
        my_session.user = username  # 将用户信息中的用户名称存入内存中的session中
        session_id = my_session.get_session_id()  # 给该用户创建一个session id
        sessions[session_id] = my_session  # 以session_id作为key，把这个session信息存内存中
        response.set_cookie('session-id', session_id, domain='127.0.0.1', secure=False)  # hug底层库falcon中的set_cookie方法
        return {"status": "success"}  # 在cookie-session鉴权中，我们需要把session的信息如session id存进响应的cookie中
    return f'{"status:": "fail", "info: ": f"Invalid username or password for user: {username}"}'


# 通过提取response中的cookie里的session_id来完成了鉴权，即自己把session id放进去了，所以鉴权通过，完成登录。


if __name__ == "__main__":
    hug.API(__name__).http.serve(port=8000)

"""
整个流程：
1. 客户端发起登录请求，请求中携带用户名和密码
2. 服务端校验用户名密码，正确则鉴权通过
3. 服务端在内存中创建session，并保存用户信息进session
4. 服务端通过算法给session生成session id
5. 服务端把session id存进响应的cookie中
6. 服务端返回响应，其中包含含有session id的cookie
7. 客户端得到响应
8. 客户端使用响应中的cookie继续发起新请求
9. 服务端检查请求中的cookie，从中找到session id
10. 服务端在内存中查找session id所对应的session是否存在（因为登出后session id可销毁）
11. 服务端找到session，从中提取到用户信息，并由此得知用户已登录
12. 服务端将响应返回给客户端，响应中携带该用户的信息。
"""
