# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""


import requests

from config_template import BASE_CONFIG

class GitLabAPI(object):
    def __init__(self, headers={'PRIVATE-TOKEN': BASE_CONFIG["GITLAB_INFO"]["PRIVATE_TOKEN"]}, *args, **kwargs):
        self.headers = headers


    def get_user_id(self, username):
        """
        返回用户id
        :param username:
        :return:
        """
        user_id = None
        res = requests.get(BASE_CONFIG["GITLAB_INFO"]["URL"]+"/api/v3/users?username=%s"%username, headers=self.headers, verify=False)
        status_code = res.status_code
        if status_code != 200:
            raise Exception("访问错误!", res)
        content = res.json()
        if content:
            user_id = content[0].get('id')
        return user_id


    def get_user_projects(self):
        """
        返回项目id
        :return:
        """
        res = requests.get(BASE_CONFIG["GITLAB_INFO"]["URL"]+"/api/v3/projects", headers=self.headers, verify=False)
        status_code = res.status_code
        if status_code != 200:
            raise Exception("访问错误!", res)
        content = res.json()
        return content


    def get_user_project_id(self, name):
        """
        :param name: 项目名称
        :return:
        """
        project_id = None
        projects = self.get_user_projects()
        if projects:
            for item in projects:
                if item.get('name') == name:
                    project_id = item.get('id')
        return project_id


    def get_project_branchs(self, project_id):
        """
        返回项目分支
        :param project_id:
        :return:
        """
        branchs = []
        res = requests.get(BASE_CONFIG["GITLAB_INFO"]["URL"]+"/api/v3/projects/%s/repository/branches"%project_id, headers=self.headers, verify=False)
        status_code = res.status_code
        if status_code != 200:
            raise Exception("访问错误!", res)
        content = res.json()
        if content:
            for item in content:
                branchs.append(item.get("name"))
        return branchs


    def get_project_commits(self, project_id):
        """
        返回项目提交
        :param project_id:
        :return:
        """
        tags = []
        res = requests.get(BASE_CONFIG["GITLAB_INFO"]["URL"]+"/api/v3/projects/%s/repository/commits"%project_id, headers=self.headers, verify=False)
        status_code = res.status_code
        if status_code != 200:
            raise Exception("访问错误!", res)
        content = res.json()
        return content

    def get_sucess_token(self, project_name= None):
        project_id = self.get_user_project_id(project_name if project_name != None else BASE_CONFIG["GITLAB_INFO"]["PROJECT_NAME"])
        commits = self.get_project_commits(project_id)
        # return(commits[0]['short_id'])
        return commits[0]

if __name__ == "__main__":
    api = GitLabAPI()
    api.get_sucess_token(project_name="Fingertip_Bank")

    # user_id = api.get_user_id('git6636865')
    # print("user_id:", user_id)
    #
    # project_id = api.get_user_project_id('qa_assistant_front')
    # print("project:", project_id)
    #
    # branchs = api.get_project_branchs(project_id)
    # print("project branchs:", branchs)
    #
    # commits = api.get_project_commits(project_id)
    # print("project tags:", commits)









