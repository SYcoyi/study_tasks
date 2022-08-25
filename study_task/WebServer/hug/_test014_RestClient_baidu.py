from WebServer.hug.hug014_RestClient_baidu import RestClient

rest_client = RestClient(client_id="SDF98SDFSD9SADF", client_secret="78SJFSF9SFAFSDFF08S")
# url = "http://localhost:8000/text2audio"
# token = rest_client.token
# print(f"logined already? token= {token}")
# rest_client.logout()
# token = rest_client.token
# print(f"logout already? token= {token}")
# rest_client.login(client_id="SDF98SDFSD9SADF", client_secret="78SJFSF9SFAFSDFF08S")
# token = rest_client.token
# print(f"logined already? token= {token}")

tex = "这是我仿照的百度鉴权方法，来试试看你能用不"
payload = {'tok': "fail", 'tex': tex, 'cuid': "quickstart",
                 'lan': 'zh', 'ctp': 1}

r = rest_client.session.post(rest_client.api_root_url + '/text2audio', data=payload)
print(r)
print(r.text)
print()

payload = {'tok': rest_client.token, 'tex': tex, 'cuid': "quickstart",
                 'lan': 'zh', 'ctp': 1}
r = rest_client.session.post(rest_client.api_root_url + '/text2audio', data=payload)
print(r)
print(r.text)
