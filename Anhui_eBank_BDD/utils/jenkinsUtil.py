# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
from utils.dbUtil import SingletonModel
from utils.gitlabUtil import GitLabAPI


def jenkinsBuild(is_sucess=None, git_commit_id=None,project_name=None):
    from config import BASE_CONFIG
    # 获取项目名称
    project_name = project_name if project_name != None else BASE_CONFIG["GITLAB_INFO"]["PROJECT_NAME"]
    from jenkinsapi.jenkins import Jenkins
    jenkins = Jenkins(BASE_CONFIG["JENKINS_INFO"]["URL"], username=BASE_CONFIG["JENKINS_INFO"]["USERNAME"],
                      password=BASE_CONFIG["JENKINS_INFO"]["API_TOKEN"])
    jobName = jenkins.keys()
    is_jobs_exist = False
    for key in jobName:
        if (key == BASE_CONFIG["JENKINS_INFO"]["PROJECT_NAME"]):
            is_jobs_exist = True
    if (is_jobs_exist):
        api = GitLabAPI()
        dbObject = SingletonModel()
        params = BASE_CONFIG["JENKINS_INFO"]["BUILD_PARAM"]
        if is_sucess==False:
            # 回退至上次成功版本
            if git_commit_id == None:
                res = dbObject.fetchone(table='git_success_commit', where="project_name='" + project_name + "'",
                                        order="add_time")
                git_commit_id = res.get("short_token")
            params["fail_checkout_path"] = git_commit_id
            print("jenkins构建参数：", params)
        if is_sucess==True:
            # 将成功版本保存至数据库
            content = api.get_sucess_token(project_name=project_name)
            insert_time = dbObject.timeFormat()
            dbObject.insert(table='git_success_commit',
                                  project_name=project_name,
                                  author_email=content["author_email"],
                                  created_at=insert_time,
                                  author_name=content["author_name"],
                                  token=content["id"],
                                  short_token=content["short_id"],
                                  commit_str=content["title"],
                                  add_time=insert_time)
        job = jenkins[BASE_CONFIG["JENKINS_INFO"]["PROJECT_NAME"]]
        job_instance = job.invoke(build_params=params)
        if job_instance.is_running():
            job_instance.block_until_complete()
    else:
        print(BASE_CONFIG["JENKINS_INFO"]["PROJECT_NAME"], "项目不存在。")




#ss
from requests import post,get
import json


def httprequest(header,url,method,params=None):
    """
        根据不同传入请求类型参数参数分出不同的请求
    """
    if method == 'post':
        html = post(url, data=json.dumps(params), headers=header)
        strss = html.text
        return strss
    elif method == 'get':
        html = get(url, headers=header)
        strss = html.text
        return strss

if __name__=="__main__":
    jenkinsBuild(is_sucess=False)