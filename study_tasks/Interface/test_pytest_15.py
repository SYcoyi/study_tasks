import json
import requests
import pytest

# 在Python中使用单引号或双引号是没有区别的
# url = 'https://baidu.com/s?ie=utf-8&wd=豆瓣250top电影'
# r = requests.get(url)
# print(r)
# print(r.content)
# print("**************************************")
# print(r.text)

# r = requests.get('https://api.github.com/events')
# print(r.content)
# r = requests.post('http://httpbin.org/post',data = {'key':'value'})
# print(r.content)
# r = requests.put('http://httpbin.org/put',data={'key':'value'})
# print(r.content)

# r = requests.delete('http://httpbin.org/delete')
# print(r.content)

# r = requests.head('http://httpbin.org/get')
# print(r.content)

# r = requests.options('http://httpbin.org/get')
# print(r.content)

# payload = {'key1':'value1','key2':'value2'}
# r = requests.get('http://httpbin.org/get',params=payload)
# print(r.url)


# import json
# dict_a = {'k1':'v1','k2':'v2'}
# #把字典转为json字符串
# x = json.dumps(dict_a)
# print(x)   #{"k1": "v1", "k2": "v2"}
# print(type(x))  #<class 'str'>
# #把json字符串转为字典
# y = json.loads(x)
# print(y)
# print(type(y))


# r = requests.get('https://api.github.com/events')
# print(r.content)
# dict_json = json.loads(r.content)
# print(dict_json)

# 进阶写法
# r = requests.get('https://api.github.com/events')
# print(r.json())   # requests库自带的json解析器。 r.json == json.loads(r.content)

# 14.090 requests中的会话  进阶写法
# r = requests.get('https://www.baidu.com')
# print(r.cookies)   # <RequestsCookieJar[<Cookie BDORZ=27315 for .baidu.com/>]>
# print(vars(r.cookies))   # vars() 函数返回对象object的属性和属性值的字典对象    {'_policy': <http.cookiejar.DefaultCoo....

# 进阶写法
# cookies = dict(cookies_are='working')
# print(cookies)
# r = requests.get('http://httpbin.org/cookies', cookies=cookies)
# print(r.text)

# 改变RequestsCookieJar()的值  增加值
# jar = requests.cookies.RequestsCookieJar()
# print(jar)  # <RequestsCookieJar[]>
# jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# print(jar)
# jar.set('gross_cookie', 'blech', domain='httpbin.org', path='elsewhere')
# r = requests.get('http://httpbin.org/cookies', cookies=jar)
# print(r.text)

# s = requests.session()
# a = s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')  # 创建了一个requests会话，这个get请求使服务端创建了一个服务端的session
# # 对象，并且这个网址的作用是把服务端的session内容返回给用户。
# print(a.text)
# r = s.get('http://httpbin.org/cookies')
# print(r.text)

# session = requests.session()
# r = session.get('https://api.github.com/orgs/TestUpCommunity')
# print(r.json()['name'])
# print(r.json()['html_url'])
# print(r.json()['created_at'])
# print(r.json()['updated_at'])
# print(type(r.json()))


# name html_url created_at updated_at


# r = requests.get('http://www.qq.com')
# print(r.headers)
# print(type(r.headers))

# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent':'my-app/0.0.1'}
# r = requests.get(url,headers=headers)
# print(r.content)
# print("**************************************")
# print(r.headers)


# url = 'https://api.github.com/events'
# headers = {'user-agent':'PostmanRuntime/7.28.4'}
# r = requests.get(url,headers=headers)
# # print(r.headers)    #这里打印的headers是上面的请求的响应给的header，而不是发送的header。
# print(r.request.headers)


# r = requests.get('https://api.github.com/events')
# print(r.content)

# 15.040  pytest 执行演示
# import pytest
#
#
# def inc(x):
#     return x + 1
#
#
# def test_answer():
#     assert inc(4) == 5

# fixture作为setup的官网例子
# content of conftest.py
# import pytest
# import smtplib
#
#
# @pytest.fixture(scope='module')
# def smtp_connection():
#     return smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
#
#
# # content of test_module.py
# def test_ehlo(smtp_connection):
#     response, msg = smtp_connection.ehlo()
#     assert response == 250
#     assert b'smtp.gmail.com' in msg
#     assert 0  # for demo purpose
#
#
# def test_noop(smtp_connection):
#     response, msg = smtp_connection.noop()
#     assert response == 250
#     assert 0  # for demo purpose
#

"""
如上例子执行顺序：
1、先找到所有test_开头的文件，称为：测试脚本文件
2、在测试脚本文件同一级目录下寻找conftest.py,称为测试配置文件
3、按照随机顺序执行测试脚本文件中的测试方法
4、执行第一个测试方法，发现有一个传入参数smtp_connection,在测试配置文件中寻找名为smtp_connection的fixture
5、执行测试配置文件中的smtp_connection方法，保存返回值
6、把上一步的返回值代入第4步的测试方法传入参数中，执行第一个测试方法
7、执行第二个测试方法，发现有一个传入参数smtp_connection,在测试配置文件中寻找名为smtp_connection的fixture
8、发现这个fixture的范围是module，无需重复执行，使用第5步的返回值继续执行第7步的第二个测试方法
所以其实fixture就相当于这个module的setup方法，并且更加灵活。
通过修改fixture的scope（值可以为function,class,module,package和session）我们可以给相应的定制不同的fixture。
同样fixture也可以定义teardown方法。
如下第4行的return改成了yield,那第五行内容会在测试方法执行结束后运行了，相当于实现了teardown。
"""


# # 例3 在官网例子上增加teardown
# @pytest.fixture(scope='module')
# def smtp_connection():
#     yield smtplib.SMTP('smtp.gmail.com', 587, timeout=5)
#     print("我是teardown，我在测试方法结束后运行")

# yield的问题
# def foo():
#     print("starting...")
#     while True:
#         res = yield 4
#         print("res:", res)
#
#
# g = foo()
# print(next(g))
# print("*" * 20)
# print(next(g))

# 用fixture实现测试方法级别的setup和teardown的例子
# conftest.py的内容
# @pytest.fixture(scope="function", autouse=True)
# def foo():
#     print("function setup")
#     yield 100
#     print("function teardown")


# #test_1540.py内容
# def inc(x):
#     return x + 1
#
#
# def test_answer_1():   # 因为fixture的autouse=True，所以在测试方法的传入参数里可以省略这个fixture的方法名。省略后不可以剩余该fixture的返回值
#     assert inc(3) == 5
#
#
# def test_answer_2(foo):
#     print('\nfoo的值是：', foo)
#     print("我是来打印的")
#     assert inc(10) == foo
#
#
# # if __name__ == '__main__':   # 可省略
# #     pytest.main()


# 执行及报告输出
# @pytest.mark.webtest  # 给test_send_http这个方法单独打上了标签，这样在执行时就可以用标签来执行。命令为： pytest -v -m webtest
# def test_send_http():
#     pass
#
#
# def test_something_quick():  # 其他非标签的也可以一起执行 命令为：pytest -v -m "not webtest"
#     pass
#
#
# def test_another():
#     pass
#
#
# class TestClass(object):
#     def test_method(self):
#         pass
#
#     def test_method2(self):
#         pass
#
# # 生成html报告的命令：pytest --html=report\report1.html

