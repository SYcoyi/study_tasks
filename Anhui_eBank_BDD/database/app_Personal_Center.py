
# -- coding=utf-8 --
# coding: unicode_escape
"""
Created on 2019.02.18
安徽社区银行__app端_个人中心
"""

Domain = 'https://test3.ubank365.com'
host = 'test3.ubank365.com'



##银行app端登录Header
Header_App = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '{Cookie}',
    'Host': 'test3.ubank365.com',
    'Upgrade-Insecure-Requests': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': Domain + '/anhui',
    'Content-Type': 'application/json',
    'token': '{token}',
    'memberCode': '{memberCode}'
}

__all__ = ["Header_App_Personal_Center"]


Header_App_Personal_Center=[

    {
        # app_手机个人端登录
        'ModelName': 'Header_App_Personal_Center1',
        'InterfaceName': 'Get_into_Personal_Center',
        'Header': Header_App,
        "URL": Domain + "/api/user/ticket/list?type=1&pageNumber=1&pageSize=10&lastPageNumber=0&firstRecordTime=0&lastRecordTime=0&totalCount=0&pageCount=0",
        "Params": "",
        "Body": {
        },
        "Method": "Get",
        'InterfaceDesc': '手机进入我的券码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"ticketId"',
                    'WarningDesc': '"ticketId"',
                    'isStop': ''
                }
            ]
        }
    },
]
