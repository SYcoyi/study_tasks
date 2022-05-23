import json
import requests
# url = 'https://baidu.com/s?ie=utf-8&wd=豆瓣250top电影'
# r = requests.get(url)
# print(r)
# print(r.content)
# print("**************************************")
# print(r.text)

# test1
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

# #用fixture实现测试方法级别的setup和teardown的例子
# #conftest.py的内容
# import pytest
# @pytest.fixture(scope="function",autouse=True)
# def foo():
#     print("function setup")
#     yield 100
#     print("function teardown")


# test_1540.py内容
# import pytest
#
#
# def inc(X):
#     return x + 1
#
#
# def test_answer_1():
#     assert inc(3) == 5
#
#
# def test_answer_2(foo):
#     print(foo)
#     assert inc(98) == foo
#
#
# if __name__ == '__main__':
#     pytest.main()

# 在Python中使用单引号或双引号是没有区别的
