import requests


class Jenkins:
    def __init__(self, base_url):
        self.base_url = base_url
        self.s = requests.Session()

    def list_jobs(self, attribute_to_show="name"):
        endpoint = f"{self.base_url}/api/json?tree=jobs[{attribute_to_show}]"
        print(f"endpoint={endpoint}")
        r = self.s.get(endpoint)
        return r

    def get_user(self, username):
        endpoint = f"{self.base_url}/user/{username}/api/json"
        print(f"endpoint={endpoint}")
        r = self.s.get(endpoint)
        return r




if __name__=="__main__":
    anonymous=Jenkins(base_url="http://localhost:8080")
    r = anonymous.list_jobs()
    print(r.request.url)
    # r1 = r.json()
    # print(r1["jobs"][0]["name"])
    # print(f"r={r}")
    print(r.json()["jobs"])   # 是一个列表，列表内有三组字典，每组字典的key和value名称是相同的，值不同。
    # list1 = []
    # for i in r.json()['jobs']:
    #     print(i['name'])       # 打印出了三个值
    #     print(type(i['name']))   # str
    #     list1.append(i['name'])
    # print(f"list1 = {list1}")      # 此处打印出的值同下行代码

    jobs = [_['name'] for _ in r.json()['jobs']]   # 此处的_只是一个变量，可以换成任意一个字母作为变量的。
    print(f"jobs={jobs}")
    print("")


    r = anonymous.get_user('admin')
    print(f"response code={r.status_code}")
    print(f"response body={r.json()}")
    print("")
    r = anonymous.get_user("testusera")
    print(f"response code={r.status_code}")