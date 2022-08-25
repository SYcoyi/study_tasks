import datetime
import os
import shutil
import threading
import time

import requests
from datetime import timezone, timedelta, datetime


class Result:
    """
    该类封装了业务方法的返回值（如Operation中方法），目的是让业务方法具有标准的返回值，方便判断调用是否成功。
    缺点：方法中会增加很多if else判断
    """
    def __init__(self, info=""):
        self.success = True
        self.info = info

    def __repr__(self):
        return f"success= {self.success}, {self.info}"


def clear_log():
    shutil.rmtree("logs", True)
    os.mkdir("logs")


# def log(func):   # 装饰器@log
#     def inner(*args, **kwargs):
#         r = func(*args, **kwargs)
#         logger.info(f"{func.__name__} ——> {r}")
#         return r
#
#     return inner


class Operation:
    def __getattribute__(self, item):  # 通过修改该方法来取代装饰器@log，这样就不用在每个方法上面加@log的装饰器了。
        func = super().__getattribute__(item)
        if type(func) == type(logger.info):  # type(func): <class 'method'>  当logger.info的对象类型也是method时才成立。即只用其中的方法。
            # print(f"type(func): {type(func)}")   # type(func): <class 'method'>
            # print(f"type(logger.info): {type(logger.info)}")   # type(logger.info): <class 'method'>
            def log(*args, **kwargs):
                r = func(*args, **kwargs)
                # print(f"func: {func}") # func: <bound method JenkinsJobAPI.list_jobs of <__main__.Jenkins object at 0x0327CBD0>>
                # print(f"r:{r}")   #  r:200  ResponseBody = {'_class': 'hudson.model.Hudson', 'jobs': []}
                if not isinstance(r, Response):
                    logger.info(f"{func.__name__} ———> {r}")
                return r

            return log
        else:
            return func


class MyLog:
    """
    打印并导出Info级别及Debug级别的log日志文件
    """
    def __init__(self, log_level="INFO"):
        self.INFO = 1
        self.DEBUG = 2
        log_dict = {"INFO": self.INFO, "DEBUG": self.DEBUG}
        self.log_level = log_dict[log_level]  # 根据传入值来来取INFO、DEBUG

    def info(self, msg):  # 简略日志打印
        msg = msg.replace(u'\xa0', u' ')  # 解决编码问题，python的gbk和utf-8编码不兼容，gbk中没有\xa0, 用空格代替
        timezone_offset = 8.0  # 时间戳设置为东八区
        tzinfo = timezone(timedelta(hours=timezone_offset))
        timestamp = datetime.now(tzinfo)
        try:
            scenario_name = threading.current_thread().scenario_name
        except:
            scenario_name = "Scenario1"
        if self.log_level >= self.INFO:  # 传入值为INFO时，只print info
            print(f"[{scenario_name}][{timestamp}]{msg}")
        with open(f"logs//logs_{scenario_name}.txt", "a") as f:
            f.write(f"[{timestamp}]{msg}\n")

    def debug(self, msg):  # 详细日志打印
        timezone_offset = 8.0
        tzinfo = timezone(timedelta(hours=timezone_offset))
        timestamp = datetime.now(tzinfo)
        try:
            scenario_name = threading.current_thread().scenario_name
        except:
            scenario_name = "Scenario1_Debug"
        if self.log_level >= self.DEBUG:  # 传入值为DEBUG时，info & debug都会print
            print(f"[{scenario_name}][{timestamp}]{msg}")
        with open(f"logs//logs_{scenario_name}.txt", "a") as f:
            f.write(f"[{timestamp}]{msg}\n")


class Response:
    """
    处理响应的数据结构的类，属于“数据结构类”
    """

    def __init__(self, code, body, raw_response):
        self.code = code
        self.body = body
        self.raw_response = raw_response
        self.print_raw_request(raw_response)

    def __repr__(self):
        # 默认情况下，__repr__() 会返回和调用者有关的 “类名+object at+内存地址”信息。如：<__main__.Response object at 0x000001A7275221D0>
        # 当然，我们还可以通过在类中重写这个方法，从而实现当输出实例化对象时，输出我们想要的信息。
        return f"{self.code}  ResponseBody = {self.body}"  # 格式化这个类的对象，返回格式后的字符串

    def print_raw_request(self, response):  # 自动打印所有通过rest_client发送的请求的原始请求和原始响应。
        format_headers = lambda d: '\n'.join(f'{k}: {v}' for k, v in d.items())
        # logger.info("{req.method} {req.url}   RequestBody: {req.body}".format(req=response.request))
        # logger.info("{res.status_code}   ResponseText: {res.text}".format(res=response)) # info日志，会导致打印过多可读性下降，注释掉
        req = response.request
        res = response
        reqhdrs = format_headers(response.request.headers)
        reshdrs = format_headers(response.headers)
        logger.debug(f"""
_____________________request_____________________
{req.method} {req.url}
{reqhdrs}
        
RequestBody:  {req.body}

____________________response_____________________
{res.status_code} {res.reason}  {res.url}
{reshdrs}
        
ResponseText:  {res.text}
        
______________________end_______________________

""")


class RestClient:
    """
    该类负责发送和接收http请求
    收到的响应全部用Response类的对象来做返回值
    属于“工具类”：用于实现功能
    """

    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.session()

    def options(self, endpoint, **kwargs):
        r = self.session.options(self.base_url + endpoint, **kwargs)
        return self.process(r)

    def get(self, endpoint):
        endpoint = self.base_url + endpoint
        # print(f"GET {endpoint}")
        r = self.session.get(endpoint)
        return self.process(r)

    def post(self, endpoint, data=None, json=None, **kwargs):
        endpoint = self.base_url + endpoint
        # print(f"POST {endpoint}")
        r = self.session.post(endpoint, data, json, **kwargs)
        return self.process(r)

    @staticmethod
    def process(response):
        code = response.status_code
        try:
            # 尝试解析响应中content的内容为dict
            body = response.json()
        except:
            # 如果解析失败则直接将content转为字符串
            body = str(response.content)
        return Response(code, body, response)


# class JenkinsOperation(Operation):  # 继承Operation类，父类中的__getattribute__方法子类自动继承。
#     """
#     将业务逻辑单独抽离在这个类，达到精简Jenkins类，使其只处理http接口封装而不用处理业务逻辑
#     """
#
#     def __init__(self, jenkins):  # 只接受一个参数jenkins，这个参数jenkins的值就是 self.use_jenkins = JenkinsOperation(self) 中self传给它的
#         self.jenkins = jenkins

#     # @log
#     def delete_all_jobs(self):
#         names = self.get_all_job_names()
#         for name in names:
#             self.jenkins.delete_job(name)
#         return Result(f"{names} all deleted")
#
#     # @log
#     def get_all_job_names(self):
#         r = self.jenkins.list_jobs()
#         # print(r.raw_response.request.headers)
#         jobs = [_['name'] for _ in r.body['jobs']]
#         return jobs
#
#     # @log
#     def get_all_job_names_with_url(self):
#         r = self.jenkins.list_jobs('name,url')
#         jobs = {_['name']: _['url'] for _ in r.body['jobs']}
#         return jobs
#
#     # @log
#     def create_job_with_dsl(self, dsl, job_name):
#         result = Result()
#         r = self.jenkins.get_job(job_name)
#         if r.code == 200:
#             result.success = False
#             result.info = f"{job_name} Already Exist"
#             return result
#         script = f"""def jobDSL=\"\"\"{dsl}\"\"\";
# def flowDefinition = new org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition(jobDSL, true);
# def parent = Jenkins.instance;
# def job = new org.jenkinsci.plugins.workflow.job.WorkflowJob(parent, "{job_name}")
# job.definition = flowDefinition
# job.save();
# Jenkins.instance.reload()"""
#         temp = self.jenkins.run_groovy(script)
#         r = self.jenkins.get_job(job_name)
#         if r.code == 200 and r.body.get("displayName") == job_name:
#             result.success = True
#             result.info = f"Job Created at {r.body.get('url')}"
#             return result
#         else:
#             result.success = False
#             result.info = f"{job_name} Created Failed"
#             return result


class JenkinsJobAPI:
    def __init__(self, jenkins):
        self.jenkins = jenkins
        self.rest_client = jenkins.rest_client

    def list_jobs(self, attribute_to_show="name"):  # http接口的封装方法
        return self.rest_client.get(f"/api/json?tree=jobs[{attribute_to_show}]")

    def get_job(self, job):
        # 检查某个job是否存在
        return self.rest_client.get(f"/job/{job}/api/json")

    def delete_job(self, job_name):
        return self.rest_client.post(f"/job/{job_name}/doDelete", allow_redirects=False)


class JenkinsUserAPI:
    def __init__(self, jenkins):
        self.jenkins = jenkins
        self.rest_client = jenkins.rest_client

    def get_user(self, username):  # http接口的封装方法
        return self.rest_client.get(f"/user/{username}/api/json")

    def asynch_people(self):
        return self.rest_client.post(f"/asynchPeople/api/json")


class JenkinsJobOperation(Operation, JenkinsJobAPI):
    # @log
    def get_all_job_names(self):
        r = self.list_jobs()
        # print(r.raw_response.request.headers)
        jobs = [_['name'] for _ in r.body['jobs']]
        return jobs

    # @log
    def get_all_job_names_with_url(self):
        r = self.list_jobs('name,url')
        jobs = {_['name']: _['url'] for _ in r.body['jobs']}
        return jobs

    # @log
    def delete_all_jobs(self):
        names = self.get_all_job_names()
        for name in names:
            self.delete_job(name)
        return Result(f"{names} all deleted")

    # @log
    def create_job_with_dsl(self, dsl, job_name):
        result = Result()
        r = self.get_job(job_name)
        if r.code == 200:
            result.success = False
            result.info = f"{job_name} Already Exist"
            return result
        script = f"""def jobDSL=\"\"\"{dsl}\"\"\";
    def flowDefinition = new org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition(jobDSL, true);
    def parent = Jenkins.instance;
    def job = new org.jenkinsci.plugins.workflow.job.WorkflowJob(parent, "{job_name}")
    job.definition = flowDefinition
    job.save();
    Jenkins.instance.reload()"""
        temp = self.run_groovy(script)
        r = self.get_job(job_name)
        if r.code == 200 and r.body.get("displayName") == job_name:
            result.success = True
            result.info = f"Job Created at {r.body.get('url')}"
            return result
        else:
            result.success = False
            result.info = f"{job_name} Created Failed"
            return result


class JenkinsUserOperation(Operation, JenkinsUserAPI):
    def get_all_usernames(self):
        r = self.asynch_people()
        users = r.body.get("users")
        absolute_urls = [_['user']['absoluteUrl'] for _ in users]
        all_usernames = [_.split("/")[-1] for _ in absolute_urls]
        return all_usernames


class Jenkins(JenkinsJobOperation, JenkinsUserOperation):
    """
    负责封装http接口，该类内组装进一个RestClient类的实例作为它的成员变量。这是组装模式(非继承模式)
    属于“业务类”：主要用于封装业务逻辑
    """

    def __init__(self, base_url, username=None, password=None):
        self.base_url = base_url
        self.rest_client = RestClient(base_url)
        # self.use_jenkins = JenkinsOperation(self)  # 在Jenkins类的初始化方法中，把self作为参数传递给JenkinsOperation
        # # 的初始化方法，传递过去的其实就是Jenkins类的实例。
        # self.job_api = JenkinsJobAPI(self)    # 当项目过大方法名容易重复时，可以在根节点成员里加上叶子节点的实例。（虽然不加实例也是可以直接调用的）
        # self.user_api = JenkinsUserAPI(self)  # 同上
        self.crumb_field_name = None
        self.crumb_field_value = None
        if username and password:
            self.login(username, password)

    def login(self, username, password):
        """
        Jenkins登录鉴权需要兼备基础鉴权信息+CSRF token
        调用requests.session.auth来设置基础鉴权信息
        然后再获取token并将该token放入session的header中
        """
        logger.info(f"login username={username}")
        self.rest_client.session.auth = username, password  # 先做登录，直接利用requests的auth机制，把用户名和密码保存在auth
        # 这样requests就会自动把当前session下发送的所有请求都带上鉴权信息。
        r = self.get_crumber_issuer()
        self.crumb_field_name = r.body['crumbRequestField']
        self.crumb_field_value = r.body['crumb']
        # print(f"crumb_field_name']  {r.body['crumbRequestField']}")
        # print(f"crumb_field_value  {r.body['crumb']}")
        # 在session中设置crumb的字段名和值
        self.rest_client.session.headers[self.crumb_field_name] = self.crumb_field_value
        # print(self.rest_client.session.headers)
        # return self

    def logout(self):
        del self.rest_client.session.headers[self.crumb_field_name]
        self.rest_client.auth = None
        self.crumb_field_name = None
        self.crumb_field_value = None
        # print(self.rest_client.session.headers)

    def get_crumber_issuer(self):
        return self.rest_client.get('/crumbIssuer/api/json')

    def run_groovy(self, script):
        payload = {'script': script}
        return self.rest_client.post(f"/scriptText", data=payload)


if __name__ == "__main__":
    clear_log()
    logger = MyLog()
    admin = Jenkins("http://localhost:8080", "admin", "admin")
    job_dsl = """properties([parameters([string(name: 'Run', defaultValue:'Yes', description:'a parameter')])])node {
    stage("test"){echo 'Hello World'}}"""

    # 可以直接调用各个模块里封装的api
    # 调用JenkinsJobAPI里封装的方法
    r = admin.list_jobs()
    print(r)

    # 调用JenkinsUserAPI里封装的方法
    r = admin.get_user("admin")
    print(r)

    # 可以直接使用各种Operations里面的方法，并且依旧自动打印日志
    # 调用JenkinsUserOperation里的方法
    admin.get_all_usernames()

    # 调用JenkinsJobOperation里的方法
    admin.get_all_job_names()
    admin.delete_all_jobs()
    admin.create_job_with_dsl(job_dsl, "testJob001")
    admin.create_job_with_dsl(job_dsl, "testJob002")
    admin.delete_all_jobs()
    admin.get_all_usernames()

    # r = admin.use_jenkins.delete_all_jobs()
    # # print(f"我是r:{r}")
    # r1 = admin.use_jenkins.create_job_with_dsl(job_dsl, "testJob001")
    # # print(f"我是r1:{r1}")
    # r2 = admin.use_jenkins.create_job_with_dsl(job_dsl, "testJob002")
    # # print(f"我是r2:{r2}")
    # r3 = admin.use_jenkins.delete_all_jobs()
    # # print(f"我是r:{r}")

    # admin.run_groovy("print('Hello Groovy')")
    # logger.info("************************************")
    # logger = MyLog(log_level="DEBUG")
    # admin = Jenkins("http://localhost:8080", "admin", "admin")
    # admin.run_groovy("print('Hello Groovy')")

    # clear_log()
    # logger = MyLog()
    # logger.info("something")

    # anonymous = Jenkins(base_url="http://localhost:8080")
    # r = anonymous.list_jobs()
    # print(f"r.code = {r.code}")
    # print(f"r.body = {r.body}")
    # jobs = [_['name'] for _ in r.body['jobs']]
    # print(f"listJobs.json={jobs}")
    # print('')
    #
    # r = anonymous.get_user('admin')
    # print(f"getUser response content = {r.body}")
    # r = anonymous.get_user('testusera')
    # print(f"getUser response code = {r.code}")
    # print(r)

    # r = anonymous.list_jobs('name,url')
    # print('')
    # print(r.body)
    # print('')
    #
    # r = anonymous.get_all_job_names()
    # print(r)
    #
    # r = anonymous.get_all_job_names_with_url()
    # print(r)

    # r = anonymous.use_jenkins.get_all_job_names()
    # print(r)
    # r = anonymous.use_jenkins.get_all_job_names_with_url()
    # print(r)

    # admin = Jenkins(base_url="http://localhost:8080").login('admin', "admin")
    # r = admin.use_jenkins.get_all_job_names()

    # admin = Jenkins(base_url="http://localhost:8080", username="admin", password="admin")
    # r = admin.run_groovy("print('Hello world groovy!')")
    # print(r)
    # admin.logout()

    # 类型为str 使用的DSL语言。job_dsl描述了一个带参数的pipeline job
    # job_dsl = """properties([
    #                        parameters([
    #                            string(name: 'Run',
    #                                   defaultValue: 'Yes',
    #                                   description: 'a parameter')
    #                                   ])
    #                   ])
    #    node {
    #      stage("test"){
    #       echo 'Hello World'
    #      }
    #    }"""

    # # 类型同为str，是groovy语言写的脚本，用来创建job_dsl所描述的job
    # script = f"""def jobDSL=\"\"\"{job_dsl}\"\"\";
    #
    #        def flowDefinition = new org.jenkinsci.plugins.workflow.cps.CpsFlowDefinition(jobDSL, true);
    #        def parent = Jenkins.instance;
    #        def job = new org.jenkinsci.plugins.workflow.job.WorkflowJob(parent, "job_created_by_http_method")
    #        job.definition = flowDefinition
    #        job.save();
    #        Jenkins.instance.reload()"""

    # admin = Jenkins(base_url="http://localhost:8080", username="admin", password="admin")
    # # r = admin.get_job('job_created_by_http_method')
    # # print(r)
    # # r = admin.run_groovy(script)
    # # print(r)
    # # r = admin.get_job('job_created_by_http_method')   # 分步骤获取某事件前后状态，对比前后来判断某事件是否如预期执行或发生。可称为：分布对比法
    # # print(r)                                # 因为无法保证测试代码本身是否是正确的，所以最好是对比下，或者是日志打印下。
    # r = admin.use_jenkins.create_job_with_dsl(job_dsl, "job_created_by_operation")
    # print(r)
