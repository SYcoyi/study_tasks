#!/usr/bin/env python
# -- coding=utf-8 --

'''
配置模板文件
各人需要根据config_template.py建立自己的config.py文件
'''

import os

current_path = os.path.dirname(os.path.realpath(__file__))

BASE_CONFIG = {
    # 基本的URL
    "BASE_URL": "http://www.weather.com.cn/data/sk/",
    # 日志管理
    "LOG": {
        "LOG_LEVEL": "info",
        "LOG_FILE_NAME": "g2p_test.log",
    },
    # 报告目录
    "REPORT_FOLDER": os.path.join(current_path, "report"),
    # allure报告目录
    "ALLURE_REPORT_FOLDER": os.path.join(current_path, "allure_report"),
    # 临时文件目录
    "TEMP_FOLDER": os.path.join(current_path, "temp"),
    # Jenkins 配置
    "JENKINS_INFO": {
        "URL": "http://10.24.248.205:8080/",
        "USERNAME": "jenkins6636865",
        "API_TOKEN": "112bc10b8333d68db4f40e43590fb005fd",
        "PROJECT_NAME": "sub_front_qa_all",
        "BUILD_PARAM": {'env': 'UAT', 'branch': 'master'}
    },
    # GitLab 配置
    "GITLAB_INFO": {
        "URL": "http://gitlab.f-road.com.cn",
        "PRIVATE_TOKEN": "TYWR1yN15H88P1ysAErd",
        "PROJECT_NAME": "qa_assistant_front"
    },
    # Mysql 配置
    "MYSQL_INFO": {
        "HOST": "10.24.248.205",
        "PORT": 3306,
        "USERNAME": "root",
        "PASSWORD": "froad123!@#",
        "DATABASE": "jenkins_dve",
        "TABLE": "git_success_commit",
        "CHARSET": "utf8"
    }
}