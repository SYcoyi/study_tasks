#!/usr/bin/env python
# -- coding=utf-8 --
# coding: unicode_escape
"""
Created on 2019.02.18
安徽社区银行__银行管理平台自动化case
"""

# 接口对象注入在类的__all__函数中，
from database.__global_params import Bank_ENV, ENV

__all__ = ['INTERFACE_PARAMS_Bank']
Domain = Bank_ENV["Domain"]

INTERFACE_PARAMS_Bank = [
    {
        ##银行端登录_获取图片验证码
        'ModelName': 'AnhuiBank_Login',
        'InterfaceName': 'AnhuiBank_Login_getGic',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/index.html',
                'Content-Type': 'application/json',
            },
        'URL': Domain + '/api/bank/login/gic',
        'Params': '',
        'Body': '',
        'Method': 'Post',
        'InterfaceDesc': '获取图片验证码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'token',
                    'WarningDesc': '银行管理平台登录页面获取图片验证码错误',
                    'IsStop': ''
                },
            ]
        }
    },

    {
        ##银行端法人行登录
        'ModelName': 'AnhuiBank_Login',
        'InterfaceName': 'AnhuiBank_Login_FaRen',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/index.html',
                'Content-Type': 'application/json',
            },
        'URL': Domain + '/api/bank/login/ve',
        'Params': '',
        'Body': {
            "userName": Bank_ENV["farenName"],
            "password": Bank_ENV["farenPwd"],
            "code": "{code}",
            "loginFailureCount": 0,
            "token": "{token}",
        },
        'Method': 'Post',
        'InterfaceDesc': '银行端法人登陆',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"code":"0000"',
                    'WarningDesc': '银行管理平台登录失败',
                    'IsStop': ''
                },
            ]
        }
    },

    {
        ##银行端法人行登录
        'ModelName': 'AnhuiBank_Login',
        'InterfaceName': 'AnhuiBank_Login_FaRen',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/index.html',
                'Content-Type': 'application/json',
            },
        'URL': Domain + '/api/bank/login/ve',
        'Params': '',
        'Body': {
            "userName": Bank_ENV["farenName"],
            "password": Bank_ENV["farenPwd"],
            "code": "{code}",
            "loginFailureCount": 0,
            "token": "{token}",
        },
        'Method': 'Post',
        'InterfaceDesc': '银行端法人登陆',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"code":"0000"',
                    'WarningDesc': '银行管理平台登录失败',
                    'IsStop': ''
                },
            ]
        }
    },

    {
        ##银行端省联社登录
        'ModelName': 'AnhuiBank_Login',
        'InterfaceName': 'AnhuiBank_Login_ShengLianShe',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/index.html',
                'Content-Type': 'application/json',
            },
        'URL': Domain + '/api/bank/login/ve',
        'Params': '',
        'Body': {
            "userName": Bank_ENV["slsName"],
            "password": Bank_ENV["slsPwd"],
            "code": "{code}",
            "loginFailureCount": 0,
            "token": "{token}",
        },
        'Method': 'Post',
        'InterfaceDesc': '银行端省联社登录',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"code":"0000"',
                    'WarningDesc': '银行管理平台登录失败',
                    'IsStop': ''
                },
            ]
        }
    },

    {
        ##银行管理平台_新增名优特惠商品
        'ModelName': 'AnhuiBank_AddProduct',
        'InterfaceName': 'AnhuiBank_AddProduct_MingYou',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/add_fam.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialProduct/ad',
        'Params': '',
        'Body':
            {
                "merchantId": "67FB69428000",  ##商户编号
                "orgCode": "340101",  ###新增该名优特惠的机构编号，即登录的机构编号
                "buyMethod": "0",  ##购买方式，0为不限制，1为仅限杜鹃信用卡购买
                "productName": "{productName}",  ##商品简称
                "productFullName": "{productFullName}",  ##商品全称
                "marketPrice": "200",  ##市场价
                "salePrice": "180",  ###销售价
                "postage": 0,  ##运费
                "storeNum": "1000",  ##商品原始库存
                "limitNum": "100",  ##商品购买数量限制
                "startDate": '{startDate}',  ##销售开始时间
                "endDate": '{endDate}',  ##销售结束时间
                "description": "名优特惠商品副标题",  ##商品副标题
                "files": [
                    {
                        "source": "1010_2cb01f51-4a86-49ab-ae67-2901c79dfb22",
                        "large": "1010_2cb01f51-4a86-49ab-ae67-2901c79dfb22",
                        "medium": "1010_2cb01f51-4a86-49ab-ae67-2901c79dfb22",
                        "thumbnail": "1010_2cb01f51-4a86-49ab-ae67-2901c79dfb22"
                    }
                ],
                "productKnow": "名优特惠商品购买须知",  ##购买须知
                "brandId": "100000120",  ##商户所关联的品牌
                "productDetails": "名优特惠商品商品详情"  ##商品详情
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_AddProduct_MingYou',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"code":"0000"',
                        'WarningDesc': '银行管理平台新增名优特惠异常',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        ##银行管理平台_新增精品预售商品
        'ModelName': 'AnhuiBank_AddProduct',
        'InterfaceName': 'AnhuiBank_AddProduct_YuShou',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/add_fam.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/ad',
        'Params': '',
        'Body':
            {
                "orgCode": "340101",  ##新增该预售商品的机构，即登录账户的机构编号
                "buyMethod": "0",  ##购买方式，0为不限制 1为仅支持杜鹃信用卡
                "pratenOrgCodeList": [
                    340101
                ],  ###  该商品配送或者自提可以选择的法人行
                "orgCodeList": [  ##若选择配送方式中包含自提，则以下为选择的该商品的可提货网点
                    "073B8D02000A",
                    "073B8D7200C6",
                    "073B8D02000B",
                    "073B8D02000D",
                    "073B8D02000E",
                    "073B8D020010",
                    "073B8D020014",
                ],
                "productName": "{productName}",  ##商品名称
                "productFullName": "{productFullName}",  ##商品全称
                "marketPrice": "99.99",  ##市场价
                "salePrice": "88.88",  ##销售价
                "storeNum": "{storeNum}",  ##商品原始库存
                "postage": "15",  ##运费
                "memberlimitNum": "{memberlimitNum}",  ##限购数量
                "startDate": "{startDate}",  ##预售开始时间
                "endDate": "{endDate}",  ##预售结束时间
                "takeStartDate": "{takeStartDate}",  ##提货开始时间
                "takeEndDate": "{takeEndDate}",  ##提货结束时间， 四个时间均以毫秒级别的时间戳
                "description": "精品预售副标题",  ##副标题
                "distributionType": "2",  ##distributionType
                "files": [
                    {
                        "source": "1010_ba138b49-f385-4065-9db0-3ec4c7b134e6",
                        "large": "1010_ba138b49-f385-4065-9db0-3ec4c7b134e6",
                        "medium": "1010_ba138b49-f385-4065-9db0-3ec4c7b134e6",
                        "thumbnail": "1010_ba138b49-f385-4065-9db0-3ec4c7b134e6"
                    }
                ],
                "productKnow": "精品预售购买须知",  ##购买须知
                "productDetails": "精品预售商品详情"  ##商品详情
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_AddProduct_YuShou',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"code":"0000"',
                        'WarningDesc': '银行管理平台新增精品预售异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        # 待审核名优特惠详情
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_MingYou_Detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/audit_famous_detail.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/specialDetail',
        'Params': {
            "productId": "{productId}",
            "typeDetail": "{typeDetail}",  ##审核类型 0为新增，1为更新
            "auditNumber": "{auditNumber}"  ##审核流水号
        },
        'Body': "",
        'Method': 'Get',
        'InterfaceDesc': '待审核名优特惠详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'taskOverview',
                        'WarningDesc': '银行管理平台获取待审核名优特惠详情异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##银行管理平台待审核_名优特惠审核
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_MingYou_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/audit_famous_detail.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body':
            {
                "productId": "{productId}",
                "remark": "自动审核通过",  ##审核时的审核评语
                "auditState": "{auditState}",  ###审核状态，1为审核通过
                "taskId": "{taskId}",  ##任务编号
                "instanceId": "{instanceId}"  ##审核流水号，值同auditNumber
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_PendAudit_MingYou_Audit',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"code":"0000"',
                        'WarningDesc': '银行管理名优特惠审核异常',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        ##银行管理平台审核_待审核精品预售列表
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_YuShou_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/famous_yushou.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/presell',
        'Params': '',
        'Body':
            {
                "pageSize": 10,
                "pageNumber": 1,
                "myOrgCode": "{myOrgCode}",
                "orgCode": "{orgCode}",
                "startTime": "",
                "endTime": "",
                "productName": "",
                "merchantName": "",
                "lastPageNumber": 0,
                "firstRecordTime": 0,
                "lastRecordTime": 0
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_PendAudit_YuShou_List',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'presellList',
                        'WarningDesc': '银行管理平台获取待审核精品预售列表异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        # 待审核精品预售详情
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_YuShou_Detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/famous_yushou_detail.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/presellDetail',
        'Params': {
            "productId": "{productId}",
            "typeDetail": "{typeDetail}",  ##审核类型 0为新增，1为更新
            "auditNumber": "{auditNumber}"  ##审核流水号
        },
        'Body': "",
        'Method': 'Get',
        'InterfaceDesc': '待审核精品预售详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'taskOverview',
                        'WarningDesc': '银行管理平台获取待审核精品预售详情异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##银行管理平台待审核_精品预售审核
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_YuShou_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/famous_yushou_detail.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body':
            {
                "productId": "{productId}",
                "remark": "自动审核通过",  ##审核是的审核评语
                "auditState": "{auditState}",  ###审核状态，1为审核通过
                "taskId": "{taskId}",  ##任务编号
                "instanceId": "{instanceId}"  ##审核流水号，值同auditNumber
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_PendAudit_YuShou_Audit',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"code":"0000"',
                        'WarningDesc': '银行管理精品预售审核异常',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        ##银行管理平台审核_待审核团购列表
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_TuanGou_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/famous_group.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/auditLt',
        'Params': '',
        'Body':
            {
                "pageSize": 10,
                "pageNumber": 1,
                "orgCode": "{orgCode}",
                "startDate": "",
                "endDate": "",
                "productName": "{productName}",
                "merchantName": "",
                "productCategory": "",
                "lastPageNumber": 0,
                "firstRecordTime": 0,
                "lastRecordTime": 0
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_PendAudit_TuanGou_List',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productList',
                        'WarningDesc': '银行管理平台获取待审核团购列表异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##待审核团购详情
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_TuanGou_Detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/group_detail.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/addl',
        'Params': {
            "productId": "{productId}",
            "auditNumber": "{auditNumber}"  ##审核流水号
        },
        'Body': "",
        'Method': 'Get',
        'InterfaceDesc': '待审核团购详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'auditNumber',
                        'WarningDesc': '银行管理平台获取待审核团购详情异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##银行管理平台待审核_团购审核
        'ModelName': 'AnhuiBank_PendAudit',
        'InterfaceName': 'AnhuiBank_PendAudit_TuanGou_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/group_detail.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body':
            {
                "productId": "{productId}",
                "remark": "自动审核通过",  ##审核是的审核评语
                "auditState": "{auditState}",  ###审核状态，1为审核通过
                "taskId": "{taskId}",  ##任务编号
                "instanceId": "{instanceId}"  ##审核流水号，值同auditNumber
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiBank_PendAudit_TuanGou_Audit',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"code":"0000"',
                        'WarningDesc': '银行管理团购审核异常',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行管理退出登录
        'ModelName': 'AnhuiBank_Logout',
        'InterfaceName': 'AnhuiBank_Logout',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/login/olt',
        'Params': '',
        'Body':
            {
                "token": "{token}",
            },
        'Method': 'Post',
        'InterfaceDesc': '银行端退出登录',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"code":"0000"',
                        'WarningDesc': '银行管理平台退出登录异常',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核商户列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Approvallt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/approvallt',
        'Params': '',
        'Body':
            {
                "category": "",
                "endDate": "",
                "firstRecordTime": 0,
                "lastPageNumber": 0,
                "lastRecordTime": 0,
                "merchantName": "",
                "myOrgCode": Bank_ENV['myOrgCode'],
                "pageNumber": 1,
                "pageSize": 10,
                "startDate": "",
                "type": ""
            },
        'Method': 'Post',
        'InterfaceDesc': '待审核商户列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'totalCount',
                        'WarningDesc': '待审核商户列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核品牌列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_brand',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/brand',
        'Params': '',
        'Body':
            {
                "brandName": "",
                "endTime": "",
                "firstRecordTime": 0,
                "lastPageNumber": 0,
                "lastRecordTime": 0,
                "myOrgCode": Bank_ENV['myOrgCode'],
                "orgCode": Bank_ENV['myOrgCode'],
                "pageNumber": 1,
                "pageSize": 10,
                "startTime": ""
            },
        'Method': 'Post',
        'InterfaceDesc': '待审核品牌列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'brand',
                        'WarningDesc': '待审核品牌列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核品牌列表-名称查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_brand_check',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/brand',
        'Params': '',
        'Body':
            {
                "brandName": "{brandName}",
                "endTime": "",
                "firstRecordTime": 0,
                "lastPageNumber": 0,
                "lastRecordTime": 0,
                "myOrgCode": Bank_ENV['myOrgCode'],
                "orgCode": Bank_ENV['myOrgCode'],
                "pageNumber": 1,
                "pageSize": 10,
                "startTime": ""
            },
        'Method': 'Post',
        'InterfaceDesc': '待审核品牌列表-名称查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'brand',
                        'WarningDesc': '待审核品牌列表-名称查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核品牌列表-名称查询-省联社查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_brand_check_sls',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/brand',
        'Params': '',
        'Body':
            {
                "brandName": "{brandName}",
                "endTime": "",
                "firstRecordTime": 0,
                "lastPageNumber": 0,
                "lastRecordTime": 0,
                "myOrgCode": Bank_ENV['slsOrgCode'],
                "orgCode": Bank_ENV['slsOrgCode'],
                "pageNumber": 1,
                "pageSize": 10,
                "startTime": ""
            },
        'Method': 'Post',
        'InterfaceDesc': '待审核品牌列表-名称查询-省联社查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'brand',
                        'WarningDesc': '待审核品牌列表-名称查询-省联社查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户分类
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Gmc',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/gmc',
        'Params': '',
        'Body': {},
        'Method': 'Post',
        'InterfaceDesc': '商户分类',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'categoryId',
                        'WarningDesc': '商户分类查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核团购列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_AuditLt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/auditLt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV['myOrgCode'], "startDate": "", "endDate": "",
                 "productName": "{productName}", "merchantName": "", "productCategory": "", "lastPageNumber": 1,
                 "firstRecordTime": 1559633120678, "lastRecordTime": 1559631646252},
        'Method': 'Post',
        'InterfaceDesc': '待审核团购列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productList',
                        'WarningDesc': '待审核团购列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核线下礼品列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Offline',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/offline',
        'Params': '',
        'Body': {
            "endPrice": "",
            "firstRecordTime": 0,
            "lastPageNumber": 0,
            "lastRecordTime": 0,
            "myOrgCode": Bank_ENV['myOrgCode'],
            "orgCode": Bank_ENV['myOrgCode'],
            "pageNumber": 1,
            "pageSize": 10,
            "startPrice": ""
        },
        'Method': 'Post',
        'InterfaceDesc': '待审核线下礼品列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '测试审核礼品',
                        'WarningDesc': '待审核线下礼品列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品审核详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PendAuit_OfflineDetail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/offlineDetail',
        'Params': {
            "productId": "{productId}",
            "typeDetail": 0,
            "auditNumber": "{auditNumber}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分礼品审核详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'taskOverview',
                        'WarningDesc': '积分礼品审核详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_Audit_jf',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body': {"productId": "{productId}", "remark": "123123", "auditState": "1", "taskId": "{taskId}",
                 "instanceId": "{instanceId}"},
        'Method': 'Post',
        'InterfaceDesc': '积分礼品审核',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '积分礼品审核失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品下架
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_LineProduct_IT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/lineProduct/it',
        'Params': '',
        'Body': {"productIdList": ["{productIdList}"], "isMarketable": 2},
        'Method': 'Post',
        'InterfaceDesc': '积分礼品下架',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '积分礼品下架失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品上架
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_LineProduct_IT_up',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/lineProduct/it',
        'Params': '',
        'Body': {"productIdList": ["{productIdList}"], "isMarketable": 1},
        'Method': 'Post',
        'InterfaceDesc': '积分礼品上架',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '积分礼品上架失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品删除
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_LineProduct_DE',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/lineProduct/de',
        'Params': '',
        'Body': {"productIdList": ["{productIdList}"]},
        'Method': 'Delete',
        'InterfaceDesc': '积分礼品删除',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '积分礼品删除失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核名优特惠列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Special',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/special',
        'Params': '',
        'Body': {
            "pageSize": 10,
            "pageNumber": 1,
            "myOrgCode": Bank_ENV['myOrgCode'],
            "orgCode": Bank_ENV['myOrgCode'],
            "startTime": "",
            "endTime": "",
            "productName": "{productName}",
            "merchantName": "",
            "lastPageNumber": 0,
            "firstRecordTime": 0,
            "lastRecordTime": 0
        },
        'Method': 'Post',
        'InterfaceDesc': '待审核名优特惠列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '接口测试商品',
                        'WarningDesc': '待审核名优特惠列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 团购列表详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Order_Godl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/godl',
        'Params': {
            "type": 1,
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '团购列表详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'address',
                        'WarningDesc': '团购列表详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        # 待审核预售列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Presell',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/presell',
        'Params': '',
        'Body': {
            "pageSize": 10,
            "pageNumber": 1,
            "myOrgCode": Bank_ENV['myOrgCode'],
            "orgCode": Bank_ENV['myOrgCode'],
            "startTime": "",
            "endTime": "",
            "productName": "{productName}",
            "merchantName": "",
            "lastPageNumber": 0,
            "firstRecordTime": 0,
            "lastRecordTime": 0
        },
        'Method': 'Post',
        'InterfaceDesc': '待审核预售列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '测试商品名称',
                        'WarningDesc': '待审核预售列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核限时特价活动列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_AC_Approvallt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/saleActivity/approvallt',
        'Params': '',
        'Body': {
            "activityName": "",
            "activityId": "",
            "firstRecordTime": 0,
            "lastPageNumber": 0,
            "lastRecordTime": 0,
            "orgCode": Bank_ENV['slsOrgCode'],
            "pageNumber": 1,
            "pageSize": 10,
        },
        'Method': 'Post',
        'InterfaceDesc': '待审核限时特价活动列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '待审批测试活动',
                        'WarningDesc': '待审核限时特价活动列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 审核监控列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/auditMonitor/lt',
        'Params': '',
        'Body': {
            "auditId": "",
            "businessNo": "",
            "businessType": "5",
            "endTime": "2019-06-17 23:59:59",
            "firstRecordTime": 1560743742418,
            "lastPageNumber": 1,
            "lastRecordTime": 1560699238645,
            "myOrgCode": Bank_ENV['myOrgCode'],
            "name": "",
            "operator": Bank_ENV["farenName"],
            "orgCode": Bank_ENV['myOrgCode'],
            "pageNumber": 1,
            "pageSize": 10,
            "startTime": "2019-06-16 00:00:00"
        },
        'Method': 'Post',
        'InterfaceDesc': '审核监控列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchantTaskVo',
                        'WarningDesc': '审核监控列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 审核监控详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PendAuit_SpecialDetail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/specialDetail',
        'Params': {"productId": "{productId}", "typeDetail": "0", "auditNumber": "{auditNumber}"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '审核监控详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'taskOverview',
                        'WarningDesc': '审核监控列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 综合查询列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Composite',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/auditMonitor/composite',
        'Params': '',
        'Body': {"pigeonholeStartTime": "2019-06-17 00:00:00", "pigeonholeEndTime": "2019-06-17 23:59:59", "hist": "0",
                 "myOrgCode": Bank_ENV['myOrgCode'], "operator": Bank_ENV["farenName"], "pageSize": 10, "pageNumber": 1,
                 "isPigeonhole": "2", "orgCode": Bank_ENV['myOrgCode'], "auditId": "", "startTime": "", "endTime": "",
                 "businessType": "1", "name": "", "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0,
                 "auditState": "", "businessNo": ""},
        'Method': 'Post',
        'InterfaceDesc': '综合查询列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageNumber',
                        'WarningDesc': '综合查询列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 综合查询详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Editdl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/editdl',
        'Params': {
            "merchantId": "{merchantId}",
            "auditId": "{auditId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '综合查询详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchantTaskList',
                        'WarningDesc': '综合查询详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PLT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/lineProduct/plt',
        'Params': '',
        'Body': {
            "auditEndTime": "",
            "auditStartTime": "",
            "auditState": "",
            "firstRecordTime": 0,
            "isMarketable": "",
            "lastPageNumber": 0,
            "lastRecordTime": 0,
            "orgCode": Bank_ENV["myOrgCode"],
            "pageNumber": 1,
            "pageSize": 10,
            "priceEnd": "",
            "priceStart": "",
            "productName": ""
        },
        'Method': 'Post',
        'InterfaceDesc': '积分礼品列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'message',
                        'WarningDesc': '积分礼品列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_LineProduct_DL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/lineProduct/dl',
        'Params': {
            "productId": "{productId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分礼品详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productId',
                        'WarningDesc': '积分礼品详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品图片上传探测
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_IMG_token',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/img/token',
        'Params': {"fsizeLimitMax": "0", "fsizeLimitMin": "0", "heightLimitMax": "0", "heightLimitMin": "0",
                   "mimeLimit": "image%2F*", "num": "0.9695756489469662", "widthLimitMax": "0", "widthLimitMin": "0"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分礼品图片上传探测',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '积分礼品图片上传探测失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分礼品新增
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_LineProduct_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/lineProduct/ad',
        'Params': '',
        'Body': {"orgCode": Bank_ENV["myOrgCode"], "pratenOrgCodeList": [Bank_ENV["myOrgCodeNum"]],
                 "orgCodeList": ["54B3BA240000"],
                 "productName": "{productName}", "productFullName": "测试礼品全称112233", "marketPrice": "520", "point": "50",
                 "storeNum": "99999", "memberlimitNum": "0", "startDate": "{startDate}", "endDate": "{endDate}",
                 "description": "测试副标题", "distributionType": "1", "files": [
                {"source": "1010_58b04c37-0ee7-4d10-a97f-0fef1af1fae6",
                 "large": "1010_58b04c37-0ee7-4d10-a97f-0fef1af1fae6",
                 "medium": "1010_58b04c37-0ee7-4d10-a97f-0fef1af1fae6",
                 "thumbnail": "1010_58b04c37-0ee7-4d10-a97f-0fef1af1fae6"}], "productKnow": "测试兑换须知",
                 "productDetails": "测试礼品详情"},
        'Method': 'Post',
        'InterfaceDesc': '积分礼品新增',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '积分礼品新增失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 团购订单列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Golt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/golt',
        'Params': '',
        'Body': {
            "endDate": "2019-06-11 23:59:59",
            "firstRecordTime": 1559723490971,
            "hist": "0",
            "lastPageNumber": 1,
            "lastRecordTime": 1559716043258,
            "merchantName": "",
            "orderStatus": "",
            "orgCode": Bank_ENV["myOrgCode"],
            "pageNumber": 1,
            "pageSize": 10,
            "startDate": "2019-03-13 00:00:00",
            "subOrderId": "",
            "type": 1
        },
        'Method': 'Post',
        'InterfaceDesc': '团购订单列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '团购订单列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 预售订单列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Polt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/polt',
        'Params': '',
        'Body': {
            "cashCouponId": "",
            "deliveryOption": "",
            "endDate": "2019-06-04 23:59:59",
            "firstRecordTime": 1559723490971,
            "hist": "0",
            "lastPageNumber": 1,
            "lastRecordTime": 1559716043258,
            "merchantName": "",
            "myOrgCode": Bank_ENV["myOrgCode"],
            "orderStatus": "",
            "orgCode": Bank_ENV["myOrgCode"],
            "pageNumber": 1,
            "pageSize": 10,
            "startDate": "2019-03-06 00:00:00",
            "subOrderId": "",
            "type": 2,
        },
        'Method': 'Post',
        'InterfaceDesc': '预售订单列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '预售订单列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 预售订单详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Order_Podl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/podl',
        'Params': {
            "type": 2,
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '预售订单详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'address',
                        'WarningDesc': '预售订单详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 预售订单限时特价详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Order_Sdl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/saleProduct/sdl',
        'Params': {
            "type": 2,
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '预售订单限时特价详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '预售订单限时特价详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 面对面订单列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Colt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/colt',
        'Params': '',
        'Body': {
            "cashCouponId": "",
            "endDate": "2019-06-11 23:59:59",
            "firstRecordTime": 1559723490971,
            "hist": "0",
            "lastPageNumber": 1,
            "lastRecordTime": 1559716043258,
            "merchantName": "",
            "orderId": "",
            "orderStatus": "",
            "orderType": "",
            "orgCode": Bank_ENV["myOrgCode"],
            "pageNumber": 1,
            "pageSize": 10,
            "startDate": "2019-03-13 00:00:00",
            "type": 0
        },
        'Method': 'Post',
        'InterfaceDesc': '面对面订单列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '面对面订单列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 面对面订单详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Codl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/codl',
        'Params': {
            "type": 0,
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '面对面订单详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'cashCouponId',
                        'WarningDesc': '面对面订单详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠订单列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Fpolt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/fpolt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "subOrderId": "", "type": 3, "orgCode": Bank_ENV["myOrgCode"],
                 "cashCouponId": "",
                 "startDate": "2019-03-13 00:00:00", "endDate": "2019-06-11 23:59:59", "orderStatus": "",
                 "merchantName": "", "lastPageNumber": 1, "firstRecordTime": 1559723499994,
                 "lastRecordTime": 1559720986922, "hist": "0"},
        'Method': 'Post',
        'InterfaceDesc': '名优特惠订单列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '名优特惠订单列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠订单详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Order_Fpdl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/fpdl',
        'Params': {
            "type": 3,
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '名优特惠订单详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'address',
                        'WarningDesc': '名优特惠订单详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠订单限时特价详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_SaleProduct_SDL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/saleProduct/sdl',
        'Params': {
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '名优特惠订单限时特价详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '名优特惠订单限时特价详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分兑换订单列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Ceolt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/ceolt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orderId": "", "type": "4,5", "orgCode": Bank_ENV["myOrgCode"],
                 "startDate": "2019-03-13 00:00:00", "endDate": "2019-06-11 23:59:59", "orderStatus": "",
                 "merchantName": "", "lastPageNumber": 1, "firstRecordTime": 1560149238196,
                 "lastRecordTime": 1559731697269, "hist": "0"},
        'Method': 'Post',
        'InterfaceDesc': '积分兑换订单列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '积分兑换订单列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分兑换订单详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Order_Cedl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/cedl',
        'Params': {
            "type": "4,5",
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分兑换订单详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'address',
                        'WarningDesc': '积分兑换订单详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分报表中购物订单明细
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Point_ShoppingTotal',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/point/shoppingTotal',
        'Params': {"startDate": "1552953600000", "endDate": "1560729600000", "hist": "0", "pageNumber": "1",
                   "pageSize": "20", "lastPageNumber": "0", "firstRecordTime": "0", "lastRecordTime": "0"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分报表中购物订单明细',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'orderList',
                        'WarningDesc': '积分报表中购物订单明细查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分报表银行积分总计
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Point_FtfTotal',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/point/ftfTotal',
        'Params': {"startDate": "1552953600000", "endDate": "1560729600000", "hist": "0", "pageNumber": "1",
                   "pageSize": "20", "lastPageNumber": "0", "firstRecordTime": "0", "lastRecordTime": "0"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分报表银行积分总计',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'orderList',
                        'WarningDesc': '积分报表银行积分总计查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分报表商户总和
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Point_MerchantTotal',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/point/merchantTotal',
        'Params': {"startDate": "1552953600000", "endDate": "1560729600000", "hist": "0", "pageNumber": "1",
                   "pageSize": "20", "lastPageNumber": "0", "firstRecordTime": "0", "lastRecordTime": "0"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分报表商户总和',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchantList',
                        'WarningDesc': '积分报表商户总和查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品商城订单列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Bsol',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/bsol',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "subOrderId": "", "startDate": "2019-03-13", "endDate": "2019-06-11",
                 "orderStatus": "", "providerName": "", "lastPageNumber": 1, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '精品商城订单列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '精品商城订单列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 积分报表列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Total',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/point/total',
        'Params': {
            "startDate": 1552435200000,
            "endDate": 1560211200000,
            "hist": 0
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '积分报表列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '操作成功',
                        'WarningDesc': '积分报表列表',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 异常订单管理列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Ex_Lt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/ex/lt',
        'Params': '',
        'Body': {"orderId": "", "exceptionType": 2, "startDate": "2019-05-12", "merchantName": "", "pageNumber": 1,
                 "pageSize": 10, "endDate": "2019-06-11", "lastPageNumber": 0, "firstRecordTime": 0,
                 "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '异常订单管理列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '异常订单管理列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 结算查询列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Settlement_Lt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/settlement/lt',
        'Params': '',
        'Body': {"hist": "0", "settleState": "", "orderId": "", "type": "", "ticket": "", "merchantName": "",
                 "pageNumber": 1, "pageSize": 10, "startDate": "2019-03-13", "endDate": "2019-06-11",
                 "lastPageNumber": 1, "firstRecordTime": 1559789631791, "lastRecordTime": 1559723423607},
        'Method': 'Post',
        'InterfaceDesc': '结算查询列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'settlementList',
                        'WarningDesc': '结算查询列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 结算查询详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Codl',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/order/codl',
        'Params': {
            "type": 0,
            "subOrderId": "{subOrderId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '结算查询详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'orgNames',
                        'WarningDesc': '结算查询详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 支付查询列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PayList',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pay/payList?hist=0&paymentId=&orderId=&billNo=&paymentReason=&paymentStatus=&pageNumber=1&startDate=2019-03-13+00%3A00%3A00&endDate=2019-06-11+23%3A59%3A59&lastPageNumber=0&firstRecordTime=0&lastRecordTime=0',
        'Params': '',
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '支付查询列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '支付查询列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 退款查询列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Refund_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/refund/list',
        'Params': '',
        'Body': {"orderId": "", "refundId": "", "startDate": "2019-03-13", "endDate": "2019-06-11", "status": "",
                 "loginID": "", "pageNumber": 1, "pageSize": 20, "lastPageNumber": 1, "firstRecordTime": 1559545290316,
                 "lastRecordTime": 1553830160598, "billNo": "", "hist": "0"},
        'Method': 'Post',
        'InterfaceDesc': '退款查询列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'refundList',
                        'WarningDesc': '退款查询列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 退款查询详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Refund_Detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/refund/detail',
        'Params': '',
        'Body': {"refundId": "{settlementId}"},
        'Method': 'Post',
        'InterfaceDesc': '退款查询详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'refundId',
                        'WarningDesc': '退款查询详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 预售账单查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Presellorder_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presellorder/list',
        'Params': {
            "hist": 0,
            "subOrderId": '',
            "orderStatus": "",
            "productName": "7BADFDF40000",
            "startDate": "2019-03-13 00:00:00",
            "endDate": "2019-06-11 23:59:59"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '预售账单查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '预售账单查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 账单查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Bill_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bill/lt',
        'Params': '',
        'Body': {"seqNo": "", "paymentNo": "", "payType": "", "moneyStart": "", "moneyEnd": "", "state": "",
                 "mobilePhone": "", "pageNumber": 1, "startDate": "2019-06-10 00:00:00",
                 "endDate": "2019-06-11 23:59:59", "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '账单查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageCount',
                        'WarningDesc': '账单查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 退款审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_BossPayment_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/refund/bossPayment/list',
        'Params': '',
        'Body': {"billNo": "", "refundNo": "", "payType": "", "refundStatus": "", "paymentId": "", "payerName": "",
                 "payerAccount": "", "pageNumber": 1, "pageSize": 10, "beginTime": "{beginTime} 00:00:00",
                 "endTime": "{endTime} 23:59:59", "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '退款审核',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'refundList',
                        'WarningDesc': '退款审核失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户管理列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_Lt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV['myOrgCode'], "merchantName": "",
                 "merchantId": "",
                 "startDate": "2019-03-13 00:00:00", "endDate": "2019-06-11 23:59:59", "isEnable": "", "auditState": "",
                 "phone": "", "payStatus": "", "auditStartTime": "", "auditEndTime": "", "auditType": "",
                 "startOperateTime": "", "endOperateTime": "", "license": "", "lastPageNumber": 0, "firstRecordTime": 0,
                 "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '商户管理列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchantList',
                        'WarningDesc': '商户管理列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_Dt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/dl',
        'Params': {
            "merchantId": "{merchantId}",
            "merchantUserId": "{merchantUserId}",
            "operator": Bank_ENV["farenName"]
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '商户详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchant',
                        'WarningDesc': '商户详情失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户新增所属分类查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_Gmc',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/gmc',
        'Params': '；',
        'Body': {},
        'Method': 'Post',
        'InterfaceDesc': '商户新增所属分类查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'categoryId',
                        'WarningDesc': '商户新增所属分类查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户新增之商户类型
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_Gmt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/gmt',
        'Params': '；',
        'Body': {},
        'Method': 'Post',
        'InterfaceDesc': '商户新增之商户类型',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'typeName',
                        'WarningDesc': '商户新增之商户类型查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 附加功能列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_BankOrg_Gof',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/gof',
        'Params': {
            "orgCode": Bank_ENV["slsOrgCodeNum"]
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '附加功能列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'name',
                        'WarningDesc': '附加功能列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户新增之所属机构
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_BankOrg_BS',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/bs',
        'Params': '',
        'Body': {"orgCode": Bank_ENV["myOrgCode"], "myOrgCode": Bank_ENV["myOrgCode"]},
        'Method': 'Post',
        'InterfaceDesc': '商户新增之所属机构',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'orgName',
                        'WarningDesc': '商户新增之所属机构查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    # {
    #     # 商户信息
    #     'ModelName': 'AnhuiBank_List',
    #     'InterfaceName': 'AnhuiBank_Merchant_BankOrg_BS',
    #     'Header':
    #         {
    #             'Referer': Domain + '/anhui/admin/bank/main.html',
    #             'Content-Type': 'application/json',
    #             'userId': '{userId}',
    #             'token': '{token}'
    #         },
    #     'URL': Domain + '/api/bank/merchant/comlt',
    #     'Params': {
    #         "dicCode": "IDD_MAERCHNAT_OC"
    #     },
    #     'Body': '',
    #     'Method': 'Get',
    #     'InterfaceDesc': '商户信息',
    #     'Assertion':
    #         {
    #             'SearchInfo': [
    #                 {
    #                     'Scope': 'body',
    #                     'Contain': '[',
    #                     'WarningDesc': '商户信息查询失败',
    #                     'IsStop': ''
    #                 },
    #             ]
    #         }
    # },

    {
        # 商户新增之地址
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_BankOrg_SA',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/sa',
        'Params': '',
        'Body': {
            "areaId": "100000000"
        },
        'Method': 'Post',
        'InterfaceDesc': '商户新增之地址',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'treePath',
                        'WarningDesc': '商户新增之地址失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增商户
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/ad',
        'Params': '',
        'Body': {"isOutsource": False, "openingBank": Bank_ENV["myOrgCode"], "merchantName": "{merchantName}",
                 "license": "{license}", "phone": "010-99999999", "contactPhone": "13702942404",
                 "contractStaff": "糊糊", "categoryType": ["100000001", "100000002", "100000000"], "address": "中山路",
                 "areaId": "100000029", "legalName": "丽丽", "legalCredentType": "1",
                 "legalCredentNo": "{legalCredentNo}", "category": "100000003", "acctName": "测试账户",
                 "acctNumber": "{acctNumber}", "loginName": "{loginName}", "loginPhone": "13702942404",
                 "companyId": None, "acctType": "1", "merchantFuncList": [{"id": 100000000}],
                 "myOrgCode": Bank_ENV["myOrgCode"],
                 "loginPassword": "96e79218965eb72c92a549dd5a330112", "operator": Bank_ENV['farenName']},
        'Method': 'Post',
        'InterfaceDesc': '新增商户',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '操作成功',
                        'WarningDesc': '新增商户失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 门店管理列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Outlet_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/outlet/list',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV["myOrgCode"], "merchantName": "",
                 "outletName": "",
                 "startDate": "2019-03-14 00:00:00", "endDate": "2019-06-12 23:59:59", "auditStartTime": "",
                 "auditEndTime": "", "license": "", "auditState": "5", "lastPageNumber": 0, "firstRecordTime": 0,
                 "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '门店管理列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'outletList',
                        'WarningDesc': '门店管理列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户聊天记录列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_MerchantChat_Lt',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchantChat/lt',
        'Params': '',
        'Body': {"outletName": "", "memberName": "", "userMobile": "", "pageNumber": 1, "pageSize": 10,
                 "startDate": "2019-03-14 00:00:00", "endDate": "2019-06-12 23:59:59", "env": ENV["env"],
                 "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '商户聊天记录列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '商户聊天记录列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户星级管理列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_MerchantComment_StarLevelReport',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchantComment/starLevelReport',
        'Params': '',
        'Body': {"merchantName": "", "pageSize": 10, "orgCode": Bank_ENV["myOrgCode"], "pageNumber": 1,
                 "startDate": "2019-03-14 00:00:00", "endDate": "2019-06-12 23:59:59", "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '商户星级管理列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageNumber',
                        'WarningDesc': '商户星级管理列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商品星级管理列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_ProductComment_StarLevelReport',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/productComment/starLevelReport',
        'Params': '',
        'Body': {"merchantName": "", "pageSize": 10, "orgCode": Bank_ENV["myOrgCode"], "pageNumber": 1,
                 "startDate": "2019-03-14 00:00:00", "endDate": "2019-06-12 23:59:59", "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '商品星级管理列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageNumber',
                        'WarningDesc': '商品星级管理列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 物流评价列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Shipping_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/shipping/lt',
        'Params': '',
        'Body': {"subOrderId": None, "trackingNo": None, "phone": None, "pageSize": 10, "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0, "orgCode": Bank_ENV["myOrgCode"], "pageNumber": 1,
                 "startDate": "2019-03-14 00:00:00", "endDate": "2019-06-12 23:59:59"},
        'Method': 'Post',
        'InterfaceDesc': '物流评价列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'pageNumber',
                        'WarningDesc': '物流评价列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行商户评价列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_MerchantComment_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchantComment/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "merchantName": "", "answerState": "", "startLevel": "",
                 "startDate": "2019-03-14", "endDate": "2019-06-12", "orgCode": Bank_ENV["myOrgCode"],
                 "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '银行商户评价列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchantCommentList',
                        'WarningDesc': '银行商户评价列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行商品评价列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_ProductComment_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/productComment/lt',
        'Params': '',
        'Body': {"startLevel": "", "orgCode": Bank_ENV["myOrgCode"], "type": "", "merchantName": "", "answerState": "",
                 "productName": "", "startDate": "2019-03-14", "endDate": "2019-06-12", "pageSize": 10, "pageNumber": 1,
                 "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '银行商品评价列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productCommentList',
                        'WarningDesc': '银行商品评价列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 点赞汇总统计列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Praise_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/praise/lt',
        'Params': '',
        'Body': {"type": None, "busId": "", "pageSize": 10, "orgCode": Bank_ENV["myOrgCode"], "pageNumber": 1,
                 "startDate": "2019-03-14 00:00:00", "endDate": "2019-06-12 23:59:59", "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '点赞汇总统计列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'praiseList',
                        'WarningDesc': '点赞汇总统计列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 预售商品列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PresaleProduct_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV["myOrgCode"], "auditState": "",
                 "isMarketable": "",
                 "productName": "{productName}", "productId": "", "deliveryOption": "", "auditStartTime": "",
                 "auditEndTime": "",
                 "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '预售商品列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productList',
                        'WarningDesc': '预售商品列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品预售商品新增
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PresaleProduct_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/ad',
        'Params': '',
        'Body': {"orgCode": Bank_ENV["myOrgCode"], "buyMethod": "0", "pratenOrgCodeList": [Bank_ENV["myOrgCodeNum"]],
                 "orgCodeList": ["54B3BA240000"],
                 "productName": "{productName}", "productFullName": "测试商品全称{productFullName}",
                 "marketPrice": "999", "salePrice": "888",
                 "storeNum": "999", "postage": "2", "memberlimitNum": "0", "startDate": 1560297600000,
                 "endDate": 1609387200000, "takeStartDate": 1609459200000, "takeEndDate": 1640923200000,
                 "description": "测试副标题", "distributionType": "2", "files": [
                {"source": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8",
                 "large": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8",
                 "medium": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8",
                 "thumbnail": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8"}], "productKnow": "测试购买须知",
                 "productDetails": "<h2>\n\t<s>测试购买详情</s>\n</h2>"},
        'Method': 'Post',
        'InterfaceDesc': '精品预售商品新增',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '添加商品成功',
                        'WarningDesc': '精品预售商品新增失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品预售商品修改
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PresaleProduct_UE',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/ue',
        'Params': '',
        'Body': {"productId": "{productId}", "orgCode": "340101", "buyMethod": "0", "pratenOrgCodeList": [340101],
                 "orgCodeList": ["54B3BA240000"], "productFullName": "{productFullName}",
                 "productName": "{productName}",
                 "marketPrice": "999.00", "salePrice": "888.00", "storeNum": "999", "postage": "2.00",
                 "memberlimitNum": "0", "startDate": 1560297600000, "endDate": 1609387200000,
                 "takeStartDate": 1609459200000, "takeEndDate": 1640836800000, "description": "测试副标题",
                 "distributionType": "2", "files": [
                {"default": False, "id": None, "title": "预售商品", "source": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8",
                 "large": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8",
                 "medium": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8",
                 "thumbnail": "1010_60d58e3a-c50b-4489-a9d5-5d928a8089e8"}], "productKnow": "测试购买须知",
                 "productDetails": "<h2>\n\t<s>测试购买详情</s> \n</h2>", "isMarketable": "1"},
        'Method': 'Put',
        'InterfaceDesc': '精品预售商品修改',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '精品预售商品修改失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品预售商品详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PresaleProduct_DL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/dl',
        'Params': {
            "productId": "{productId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '精品预售商品详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'activities',
                        'WarningDesc': '精品预售商品详情失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品预售商品下架
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PresaleProduct_IT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/it',
        'Params': '',
        'Body': {"productId": "{productId}", "isMarketable": "{isMarketable}"},
        'Method': 'Post',
        'InterfaceDesc': '精品预售商品下架',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '精品预售商品下架失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品预售商品删除
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PresaleProduct_DE',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/de',
        'Params': {
            "productId": "{productId}"
        },
        'Body': {},
        'Method': 'Delete',
        'InterfaceDesc': '精品预售商品删除',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '精品预售商品删除失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 提货查询列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Take_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/take/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV["myOrgCode"], "orderId": "",
                 "startDate": "2018-06-12",
                 "endDate": "2019-06-12", "takeState": "", "lastPageNumber": 0, "firstRecordTime": 0,
                 "lastRecordTime": 0, "hist": "0"},
        'Method': 'Post',
        'InterfaceDesc': '提货查询列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'deliveryList',
                        'WarningDesc': '提货查询列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 提货查询列表导出
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Take_ET',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/take/et',
        'Params': {"pageSize": "10", "pageNumber": "1", "orgCode": Bank_ENV["myOrgCode"], "orderId": "",
                   "startDate": "2018-06-12",
                   "endDate": "2019-06-12", "takeState": "", "lastPageNumber": "0", "firstRecordTime": "0",
                   "lastRecordTime": "0", "hist": "0", "token": "{token}",
                   "userId": "{userId}"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '提货查询列表导出',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'deliveryVoReq',
                        'WarningDesc': '提货查询列表导出失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 团购商品信息列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV["myOrgCode"], "auditStartTime": "",
                 "auditEndTime": "",
                 "productName": "", "productId": "", "auditState": "", "merchantName": "", "isMarketable": "",
                 "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '团购商品信息列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productList',
                        'WarningDesc': '团购商品信息列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 团购商品信息详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_DL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/dl',
        'Params': {
            "productId": "{productId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '团购商品信息详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'activities',
                        'WarningDesc': '团购商品信息详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 团购商品信息上下架
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_IT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/it',
        'Params': '',
        'Body': {"isMarketable": "{isMarketable}", "productId": "{productId}"},
        'Method': 'Post',
        'InterfaceDesc': '团购商品信息上下架',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '团购商品信息上下架失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 线下券码导入之获取商品信息
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_SupplierInput',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'userId': '{userId}',
                'token': '{token}'
            },
        'File': 'testing.xlsx',
        'URL': Domain + '/api/bank/groupProduct/supplierInput',
        'Params': {"token": "{token}", "userId": "{userId}", "productId": "5BB524D00000",
                   "settleType": "1", "originStore": "10000"},
        'Body': {
            "url": "/api/bank/groupProduct/supplierInput",
            "token": "{token}",
            "userId": "{userId}",
            "productId": "5BB524D00000",
            "settleType": 1,
            "originStore": 10000,
            "id": "WU_FILE_4",
            "name": "testing.xlsx",
            "type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            "lastModifiedDate": "Wed Jun 12 2019 15:34:25 GMT 0800 (中国标准时间)",
            "size": 8577
        },
        'Method': 'Post',
        'InterfaceDesc': '线下券码导入之获取商品信息',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '9999',
                        'WarningDesc': '线下券码导入之获取商品信息失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠商品列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialProduct_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialProduct/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV["myOrgCode"], "productId": "",
                 "productName": "{productName}",
                 "merchantName": "", "auditState": "", "auditStartTime": "", "auditEndTime": "", "isMarketable": "",
                 "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '名优特惠商品列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productList',
                        'WarningDesc': '名优特惠商品列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠商品修改
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialProduct_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialProduct/ue',
        'Params': '',
        'Body': {"productId": "{productId}", "merchantId": Bank_ENV['merchantId'], "orgCode": Bank_ENV['myOrgCode'],
                 "buyMethod": "0",
                 "productName": "{productName}", "productFullName": "{productFullName}", "marketPrice": "999.00",
                 "salePrice": "888.00", "postage": 0, "storeNum": "123", "limitNum": "0", "startDate": "1609430400000",
                 "endDate": "1638288000000", "description": "测试副标题1", "files": [
                {"source": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d",
                 "large": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d",
                 "medium": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d",
                 "thumbnail": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d"}], "productKnow": "测试购买须知",
                 "brandId": "100000061", "productDetails": "测试商品详情"},
        'Method': 'Post',
        'InterfaceDesc': '名优特惠商品修改',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '名优特惠商品修改失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠商品上下架
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialProduct_IT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/it',
        'Params': '',
        'Body': {"productId": "{productId}", "isMarketable": "{isMarketable}"},
        'Method': 'Post',
        'InterfaceDesc': '名优特惠商品上下架',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '名优特惠商品上下架失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠商品详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialProduct_DL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialProduct/dl',
        'Params': {
            "productId": "{productId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '名优特惠商品详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'activities',
                        'WarningDesc': '名优特惠商品详情失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠商品删除
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialProduct_DE',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/presaleProduct/de',
        'Params': {
            "productId": "{productId}"
        },
        'Body': {},
        'Method': 'Delete',
        'InterfaceDesc': '名优特惠商品删除',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '名优特惠商品删除失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增之发货商户查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_LM',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/lm',
        'Params': {"orgCode": Bank_ENV["myOrgCode"], "orgLevel": "2", "merchantName": "", "filter": "0",
                   "pageNumber": "1",
                   "pageSize": "100", "lastPageNumber": "0", "firstRecordTime": "0", "lastRecordTime": "0"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '新增之发货商户查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'clientId',
                        'WarningDesc': '新增之发货商户查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠商品新增
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialProduct_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialProduct/ad',
        'Params': '',
        'Body': {"merchantId": Bank_ENV['merchantId'], "orgCode": Bank_ENV["myOrgCode"], "buyMethod": "0",
                 "productName": "{productName}",
                 "productFullName": "接口测试商品{productFullName}", "marketPrice": "999", "salePrice": "888", "postage": 0,
                 "storeNum": "123", "limitNum": "0", "startDate": 1609430400000, "endDate": 1638288000000,
                 "description": "测试副标题", "files": [{"source": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d",
                                                    "large": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d",
                                                    "medium": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d",
                                                    "thumbnail": "1010_dcb1e7dc-32f0-4fb1-a160-659a8861668d"}],
                 "productKnow": "测试购买须知", "brandId": "100000061", "productDetails": "测试商品详情"},
        'Method': 'Post',
        'InterfaceDesc': '名优特惠商品新增',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '名优特惠商品新增失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌管理列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_PreferentialProduct_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialBrand/lt',
        'Params': '',
        'Body': {"brandName": "", "marketStatus": "", "auditState": "", "orgCode": Bank_ENV["myOrgCode"],
                 "merchantId": "",
                 "merchantName": "", "clientId": "anhui", "pageNumber": 1, "pageSize": 10, "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '品牌管理列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '品牌管理列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌管理广告列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_BrandAd_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/brandAd/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "adOrg": Bank_ENV["myOrgCode"], "adName": "", "adState": "",
                 "adType": 1, "brandId": 0, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '品牌管理广告列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'brandAdvertList',
                        'WarningDesc': '品牌管理广告列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌排序列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_PreferentialBrand_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialBrand/lt',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "orgCode": Bank_ENV["myOrgCode"], "auditState": "", "brandName": "",
                 "marketStatus": "", "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '品牌排序列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'productList',
                        'WarningDesc': '品牌排序列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 操作日志列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_OperatorLog_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/operatorLog/lt',
        'Params': '',
        'Body': {"loginName": "", "orgCode": Bank_ENV["myOrgCode"], "startDate": "", "endDate": "", "pageSize": 10,
                 "pageNumber": 1,
                 "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '操作日志列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'operatorLogList',
                        'WarningDesc': '操作日志列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增组织机构
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_BankOrg_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/ad',
        'Params': '',
        'Body': {"orgCode": "{orgCode}", "orgName": "{orgName}", "orgType": "true", "orgLevel": "3",
                 "proinceAgency": "340000", "cityAgency": "340101", "countyAgency": "", "areaCode": "100000155",
                 "cityCode": "785", "countyCode": "786", "address": "中山路", "longitude": "", "latitude": "",
                 "tel": "13702942404", "isMutualAudit": False},
        'Method': 'Post',
        'InterfaceDesc': '新增组织机构',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '新增组织机构失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增组织之组织信息获取
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_BankOrg_DL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/dl',
        'Params': {
            "orgCode": Bank_ENV["myOrgCode"]
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '新增组织之组织信息获取',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'address',
                        'WarningDesc': '新增组织之组织信息获取失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增组织之用户列表查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Operator_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/operator/lt',
        'Params': '',
        'Body': {"name": "", "loginName": "", "orgCode": Bank_ENV["myOrgCode"], "pageSize": 5, "pageNumber": 1,
                 "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '新增组织之用户列表查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'operatorList',
                        'WarningDesc': '新增组织之用户列表查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增组织之地址查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_BankOrg_SA',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/sa',
        'Params': '',
        'Body': {"areaId": 0},
        'Method': 'Post',
        'InterfaceDesc': '新增组织之地址查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'treePath',
                        'WarningDesc': '新增组织之地址查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端新增用户
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Operator_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/operator/ad',
        'Params': '',
        'Body': {"loginName": "testing{loginName}", "operatorName": "测试用户",
                 "userPassword": "bcb15f821479b4d5772bd0ca866c00ad5f926e3580720659cc80d39c9d09802a",
                 "orgCode": Bank_ENV["myOrgCode"], "state": True, "remark": "测试备注", "department": "", "position": "",
                 "roleId": "100000339", "prefix": "AHRCU"},
        'Method': 'Post',
        'InterfaceDesc': '银行端新增用户',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端新增用户失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 新增用户之角色查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Role_ALT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/role/alt',
        'Params': '',
        'Body': {"orgCode": Bank_ENV["myOrgCode"], "operUserId": Bank_ENV["operUserId"]},
        'Method': 'Post',
        'InterfaceDesc': '新增用户之角色查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'roleName',
                        'WarningDesc': '新增用户之角色查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 组织查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_bankOrg_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/lt',
        'Params': '',
        'Body': {"orgName": "测试", "state": True, "myOrgCode": Bank_ENV["myOrgCode"], "orgCode": Bank_ENV["myOrgCode"],
                 "pageSize": 5,
                 "pageNumber": 1, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '组织查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'orgList',
                        'WarningDesc': '组织查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 角色新增
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Role_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/role/ad',
        'Params': '',
        'Body': {"roleName": "测试新增角色{roleName}", "remark": "测试新增角色说明", "tag": "1",
                 "resourceList": [100000001, 100000002, 100000003], "orgCode": Bank_ENV["myOrgCode"]},
        'Method': 'Post',
        'InterfaceDesc': '角色新增',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '角色新增失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 授权资源列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Role_RLT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/role/rlt',
        'Params': '',
        'Body': {},
        'Method': 'Post',
        'InterfaceDesc': '授权资源列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'resourceName',
                        'WarningDesc': '授权资源列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 用户信息查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Member_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/member/list',
        'Params': '',
        'Body': {"nickName": "", "phone": "", "cardNo": "", "identifyNo": "440402199302219110"},
        'Method': 'Post',
        'InterfaceDesc': '用户信息查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'memberMsg',
                        'WarningDesc': '用户信息查询列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 广告管理查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_AD_List',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/ad/list',
        'Params': {"title": "", "enableStatus": "", "adPositionId": "", "overdue": "", "paramOneValue": "",
                   "pageSize": "10", "pageNumber": "1", "lastPageNumber": "0", "firstRecordTime": "0",
                   "lastRecordTime": "0"},
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '广告管理查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'adList',
                        'WarningDesc': '广告管理查询列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 广告详情之地区查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_AD_AREA',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/ad/area',
        'Params': {
            "clientId": "anhui"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '广告详情之地区查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'AreaList',
                        'WarningDesc': '广告详情之地区查询列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 广告详情之广告位查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_AD_PositionPage',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/ad/positionPage',
        'Params': {
            "type": None
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '广告详情之广告位查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'adPositionList',
                        'WarningDesc': '广告详情之广告位查询列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 限时特价活动列表
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_SaleActivity_LT',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/saleActivity/lt',
        'Params': '',
        'Body': {"orgCode": Bank_ENV["slsOrgCode"], "activityId": "", "name": "", "beginTime": "2019-06-13 00:00:00",
                 "endTime": "2019-09-11 23:59:59", "activityStatus": "", "auditStatus": "", "pageNumber": 1,
                 "pageSize": 10, "clientId": "anhui", "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': '限时特价活动列表',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'data',
                        'WarningDesc': '限时特价活动列表失败',
                        'IsStop': ''
                    },
                ]
            }
    },
    # -------------------------------------------------------
    {
        # 待审核商户列表-依赖查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Approvallt_depar',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/approvallt',
        'Params': '',
        'Body':
            {
                "category": "",
                "endDate": "",
                "firstRecordTime": 0,
                "lastPageNumber": 0,
                "lastRecordTime": 0,
                "merchantName": "{merchantName}",
                "myOrgCode": Bank_ENV['myOrgCode'],
                "pageNumber": 1,
                "pageSize": 10,
                "startDate": "",
                "type": ""
            },
        'Method': 'Post',
        'InterfaceDesc': '待审核商户列表-依赖查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'totalCount',
                        'WarningDesc': '待审核商户列表-依赖查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        # 待审核商户详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Bank_Merchant_ADDL',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/addl',
        'Params': {
            "merchantId": "{merchantId}",
            "auditId": "{auditId}",
            "merchantUserId": "{merchantUserId}"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': '待审核商户详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'merchant',
                        'WarningDesc': '待审核商户详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户的审核-法人审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Audit_ma',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/audit/ma',
        'Params': '',
        'Body':
            {"remark": "测试审核备注", "auditState": 1, "auditId": "{auditId}", "taskId": "{taskId}",
             "bessId": "{bessId}", "myOrgCode": Bank_ENV["myOrgCode"], "operator": Bank_ENV["farenName"]},
        'Method': 'Post',
        'InterfaceDesc': '商户的审核-法人审核',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '商户的审核-法人审核失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 待审核商户列表-省联社依赖查询
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Approvallt_sls_depar',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/approvallt',
        'Params': '',
        'Body':
            {
                "category": "",
                "endDate": "",
                "firstRecordTime": 0,
                "lastPageNumber": 0,
                "lastRecordTime": 0,
                "merchantName": "{merchantName}",
                "myOrgCode": Bank_ENV['slsOrgCode'],
                "pageNumber": 1,
                "pageSize": 10,
                "startDate": "",
                "type": ""
            },
        'Method': 'Post',
        'InterfaceDesc': '待审核商户列表-省联社依赖查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'totalCount',
                        'WarningDesc': '待审核商户列表-省联社依赖查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 商户的审核-省联社审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Audit_ma_sls',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/audit/ma',
        'Params': '',
        'Body':
            {"remark": "测试审核备注", "auditState": 1, "auditId": "{auditId}", "taskId": "{taskId}",
             "bessId": "{bessId}", "myOrgCode": Bank_ENV["slsOrgCode"], "operator": Bank_ENV["slsName"]},
        'Method': 'Post',
        'InterfaceDesc': '商户的审核-省联社审核',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '商户的审核-省联社审核失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端商户编辑
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_UE',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/ue',
        'Params': '',
        'Body': {"phone": "010-99999998{phone}", "myOrgCode": Bank_ENV["myOrgCode"],
                 "loginPassword": "96e79218965eb72c92a549dd5a330112",
                 "merchantUserId": "{merchantUserId}", "merchantId": "{merchantId}", "isOutsource": False,
                 "companyId": ""},
        'Method': 'Put',
        'InterfaceDesc': '银行端商户编辑',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端商户编辑失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端商户重置密码
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_RP',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/rp',
        'Params': '',
        'Body': {"merchantId": "{merchantId}", "merchantUserId": "{merchantUserId}",
                 "userPassword": "96e79218965eb72c92a549dd5a330112"},
        'Method': 'Put',
        'InterfaceDesc': '银行端商户重置密码',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端商户重置密码失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端商户禁用
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_UF_false',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/uf',
        'Params': '',
        'Body': {"isEnable": False, "merchantId": "{merchantId}"},
        'Method': 'Put',
        'InterfaceDesc': '银行端商户禁用',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端商户禁用失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端商户启用
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_UF_true',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/uf',
        'Params': '',
        'Body': {"isEnable": True, "merchantId": "{merchantId}"},
        'Method': 'Put',
        'InterfaceDesc': '银行端商户启用',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端商户启用失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端商户解约
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Merchant_TN',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/merchant/tn',
        'Params': '',
        'Body': {"isEnable": False, "merchantId": "{merchantId}"},
        'Method': 'Put',
        'InterfaceDesc': '银行端商户解约',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端商户解约失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 门店详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_Outlet_Detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/outlet/detail',
        'Params': {
            "outletId": Bank_ENV["outletId"]
        },
        'Body': "",
        'Method': 'Get',
        'InterfaceDesc': '门店详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '门店详情失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PendAuit_Detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/pendAuit/brandDetail',
        'Params': {
            "brandId": "{brandId}",
            "typeDetail": 0,
            "auditNumber": "{auditNumber}"
        },
        'Body': "",
        'Method': 'Get',
        'InterfaceDesc': '品牌详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'newDetail',
                        'WarningDesc': '品牌详情失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌新增
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_PreferentialBrand_AD',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/preferentialBrand/ad',
        'Params': '',
        'Body': {"userOrgCode": Bank_ENV['myOrgCode'], "brandName": "{brandName}",
                 "logoUrl": "/froad-cb/coremodule/201906/ca0025c6-d59c-4241-8178-d453ee57d68e.png", "orderValue": "0",
                 "orgCode": Bank_ENV['myOrgCode'], "description": "测试品牌简介", "marketStatus": "1",
                 "merchantId": "{merchantId}",
                 "merchantName": "{merchantName}", "parentId": ""},
        'Method': 'Post',
        'InterfaceDesc': '品牌新增',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '品牌新增失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌审核-法人行社
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body': {"productId": "{productId}", "remark": "123", "auditState": "1", "taskId": "{taskId}",
                 "instanceId": "{instanceId}"},
        'Method': 'Post',
        'InterfaceDesc': '品牌审核-法人行社',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '品牌审核-法人行社失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 品牌审核-省联社
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_Audit_sls',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body': {"productId": "{productId}", "remark": "123", "auditState": "1", "taskId": "{taskId}",
                 "instanceId": "{instanceId}"},
        'Method': 'Post',
        'InterfaceDesc': '品牌审核-省联社',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '品牌审核-省联社失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 团购审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_tg_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body': {"productId": "{productId}", "remark": "123", "auditState": "1", "taskId": "{taskId}",
                 "instanceId": "{instanceId}"},
        'Method': 'Post',
        'InterfaceDesc': '团购审核-法人行社',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '团购审核失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 名优特惠审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_my_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body': {"productId": "{productId}", "remark": "123", "auditState": "1", "taskId": "{taskId}",
                 "instanceId": "{instanceId}"},
        'Method': 'Post',
        'InterfaceDesc': '名优特惠审核',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '名优特惠审核失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 精品预售审核
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_GroupProduct_jp_Audit',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/groupProduct/audit',
        'Params': '',
        'Body': {"productId": "{productId}", "remark": "123", "auditState": "1", "taskId": "{taskId}",
                 "instanceId": "{instanceId}"},
        'Method': 'Post',
        'InterfaceDesc': '精品预售审核',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '精品预售审核核失败',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        # 银行端退款详情
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_refund_bossPayment_detail',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/refund/bossPayment/detail',
        'Params': '',
        'Body': {"refundNo": "{refundNo}", "billNo": "{billNo}"},
        'Method': 'Post',
        'InterfaceDesc': '银行端退款详情',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'detail',
                        'WarningDesc': '银行端退款详情查询失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端批量退款初审
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_refund_bossPayment_auditOnce',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/refund/bossPayment/auditOnce',
        'Params': '',
        'Body': {"refundNo": "{refundNo}", "aduitResult": "YES", "aduitContent": "初审批处理成功",
                 "operator": Bank_ENV['farenName'], "remark": ""},
        'Method': 'Post',
        'InterfaceDesc': '银行端批量退款初审',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端批量退款初审失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端批量退款复审
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_refund_bossPayment_auditTwice',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/refund/bossPayment/auditTwice',
        'Params': '',
        'Body': {"refundNo": "{refundNo}", "aduitResult": "YES", "aduitContent": "复审批处理成功",
                 "operator": Bank_ENV['farenName'], "remark": ""},
        'Method': 'Post',
        'InterfaceDesc': '银行端批量退款复审',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端批量退款复审失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端修改密码
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_safeCenter_lpue',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/safeCenter/lpue',
        'Params': '',
        'Body': {"userId": "100004806",
                 "oldPassword": "{oldPassword}",
                 "password": "{password}"},
        'Method': 'Post',
        'InterfaceDesc': '银行端修改密码',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'isReset',
                        'WarningDesc': '银行端修改密码失败',
                        'IsStop': ''
                    },
                ]
            }
    },

    {
        # 银行端编辑组织
        'ModelName': 'AnhuiBank_List',
        'InterfaceName': 'AnhuiBank_Merchant_bankOrg_ue',
        'Header':
            {
                'Referer': Domain + '/anhui/admin/bank/main.html',
                'Content-Type': 'application/json',
                'userId': '{userId}',
                'token': '{token}'
            },
        'URL': Domain + '/api/bank/bankOrg/ue',
        'Params': '',
        'Body': {"merchantId": "7E2D51438000", "outletId": "7E2D51428000", "orgId": "0", "orgCode": "830139892",
                 "orgName": "测试组织9000", "orgType": "true", "orgLevel": "3", "proinceAgency": "340000",
                 "cityAgency": "340101", "countyAgency": "830139892", "areaCode": "100000155", "cityCode": "785",
                 "countyCode": "786", "address": "中山路", "longitude": "", "latitude": "", "tel": "13702942404",
                 "isMutualAudit": False},
        'Method': 'Put',
        'InterfaceDesc': '银行端编辑组织',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '银行端编辑组织失败',
                        'IsStop': ''
                    },
                ]
            }
    },
]
