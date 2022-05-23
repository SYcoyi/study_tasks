# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
# 域名
import requests

from utils.dbUtil import SingletonModel
from utils.generatorTools import StringBar, RandomBar

gb = RandomBar()
Domain = "https://test3.ubank365.com"
host = "test3.ubank365.com"

# BANK
# 法人信息
faren = "sheldonfaren"
faren_pwd = "96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e"

# 省联社信息
sls = "public001"
sls_pwd = "96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e"

# ENV 数据库信息
host = "10.43.2.7"
port = 3306
user = "root"
pwd = "root"
db = "froad_cbank_test_anhui"

# 商户端
merchant = "sheldonttt"
merchant_pwd = "062e058bab4712217e0afdc987457430"



h = {
    'Referer': Domain + '/anhui/admin/bank/index.html',
    'Content-Type': 'application/json',
}


class Context(object):
    pass


def preToken():
    result = requests.post(Domain + '/api/bank/login/gic', json={}, headers=h)
    preToken = StringBar.LRFindString(result.text, '"token":"', '","codeUrl')
    dbObject = SingletonModel(host=host, port=port, user=user, passwd=pwd, db=db)
    data = dbObject.sqlFetchone(
        "SELECT `code`FROM `cb_sms_log` WHERE mobile is null ORDER BY `create_time` DESC LIMIT 1")
    return preToken[0], data[0]['code']


def login(username, password, code, token):
    body = {
        "userName": username,
        "password": password,
        "code": code,
        "loginFailureCount": 0,
        "token": token,
    }
    result = requests.post(Domain + '/api/bank/login/ve', json=body, headers=h)
    return StringBar.LRFindString(result.text, '"userId":', ',"code"')[0], \
           StringBar.LRFindString(result.text, '"token":"',
                                  '","tag"')[0]


def createMerchant():
    pass


def run():
    context = Context()
    token, code = preToken()
    userId, token = login(faren, faren_pwd, code, token)
    context.userId = userId
    context.token = token
    print(context.userId, context.token)


if __name__ == '__main__':
    run()
