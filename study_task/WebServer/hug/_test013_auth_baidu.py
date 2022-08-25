# -*- coding:gbk -*-
import requests

#
# # "client_id"错误
# payload = {
#     "client_id": "SDF98SDFSD9SADF_false",
#     "client_secret": "78SJFSF9SFAFSDFF08S",
#     "grant_type": "client_credentials"
# }
#
# r = requests.get(url_token, data=payload)
# print(r)
# print(r.text)
#
# # "client_secret"错误
# payload = {
#     "client_id": "SDF98SDFSD9SADF",
#     "client_secret": "78SJFSF9SFAFSDFF08S_false",
#     "grant_type": "client_credentials"
# }
#
# r = requests.post(url_token, data=payload)
# print(r)
# print(r.text)


url_token = "http://localhost:8000/oauth/2.0/token"
url_audio = "http://localhost:8000/text2audio"
payload_token = {"client_id": "SDF98SDFSD9SADF", "client_secret": "78SJFSF9SFAFSDFF08S",
                 "grant_type": "client_credentials"}
tex = "这是我仿照的百度鉴权方法，来试试看你能用不"


# 生成token
r = requests.get(url_token, data=payload_token)
print(r)
print(r.text)
token = r.json()['access_token']
print(token)
print()

# 用错误的token调用audio接口
payload_audio = {'tok': "fail", 'tex': tex, 'cuid': "quickstart",
                 'lan': 'zh', 'ctp': 1}
r = requests.post(url_audio, data=payload_audio)
print(r)
print(r.text)
print()

# 用正确的token调用audio接口
payload_audio = {'tok': token, 'tex': tex, 'cuid': "quickstart",
                 'lan': 'zh', 'ctp': 1}
r = requests.post(url_audio, data=payload_audio)
print(r)
print(r.text)
print()

# 用错误的参数来校验
payload_audio = {'tok': token, 'tex': tex, 'cuid': "quickstart",
                 'lan': 'zh1', 'ctp': 1}
r = requests.post(url_audio, data=payload_audio)
print(r)
print(r.text)







