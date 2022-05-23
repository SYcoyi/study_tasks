#!/usr/bin/env python
# -- coding=utf-8 --
# coding: unicode_escape
"""
Created on 2019.02.18
安徽社区银行__银行管理平台自动化case
"""
from database.__global_params import APP_ENV

Domains = APP_ENV["Domain"]
hosts = APP_ENV["host"]

##银行端登录Header
Header_App_user = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '{Cookie}',
    'memberCode': '{memberCode}',
    'Host': hosts,
    'Upgrade-Insecure-Requests': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': Domains + '/anhui/m/anhuiLogin.html',
    'Content-Type': 'application/json'
}

Header_App_user_imgcode = {
    "Accept": "application/json",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Host": hosts,
    "Referer": "https://test3.ubank365.com/anhui/m/loginFindPsdTw.html?loginId='{mobile_a}'&encryptMobile='{mobile_b}'&mobile='{mobile_c}'",
    "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1",
    "X-Requested-With": "XMLHttpRequest",
}

__all__ = ["Header_App_user"]

Header_App_user = [
    {
        # app个人端获取登录验证码
        'ModelName': 'Header_App_user',
        'InterfaceName': 'anhuiuserapp_user_getcode',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/code/check_send_sms",
        "Params": "",
        "Body": {
            "mobile": APP_ENV["loginId"],
            "smsType": "1317",
        },
        "Method": "Post",
        'InterfaceDesc': 'app个人端获取登录验证码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"code":"0000"',
                    'WarningDesc': '没有找到:"code":"0000"',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app个人端验证码登录
        'ModelName': 'Header_App_user',
        'InterfaceName': 'anhuiuserapp_user_login',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/login/mobileCheckLogin",
        "Params": "",
        "Body": {
            "code": "{code}",
            "token": "{smsToken}",
            "mobile": APP_ENV["loginId"],
            "loginTime": "{loginTime}",
            "createChannel": "CB_P_ANDROID",
            "devicesToken": "12345"
        },
        "Method": "Post",
        'InterfaceDesc': 'app个人端登录',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'loginId',
                    'WarningDesc': '没有找到:loginId',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app个人端密码登录 1q2w3e4r
        'ModelName': 'Header_App_user_passwork',
        'InterfaceName': 'anhuiuserapp_user_login_passwork',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/login/login",
        "Params": "",
        "Body": {"loginId": APP_ENV["loginId"],
                 "loginPwd": APP_ENV["pwd"],
                 "createChannel": "CB_P_ANDROID",
                 "devicesToken": APP_ENV["devicesToken"]},
        "Method": "Post",
        'InterfaceDesc': '手机个人端密码登录',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'loginId',
                    'WarningDesc': '没有找到:loginId',
                    'isStop': ''
                }
            ]
        }
    },

    {
        # 首页点击找回密码
        'ModelName': 'Header_App_update_passwork',
        'InterfaceName': 'anhuiuserapp_update_login_passwork',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/code/generate_image",
        "Params": "",
        "Body": {},
        "Method": "Get",
        'InterfaceDesc': '点击忘记密码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'imgToken',
                    'WarningDesc': 'imgToken',
                    'isStop': ''
                }
            ]
        }
    },

    {
        # 首页点击找回密码
        'ModelName': 'Header_one_update_passwork',
        'InterfaceName': 'anhuiuserapp_one_update_passwork',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/safe/loginpwd/forget",
        "Params": "",
        "Body": {"imgCode": "{imgCode}",
                 "imgToken": "{imgToken}",
                 "mobile": "{mobile}"}
        ,
        "Method": "Post",
        'InterfaceDesc': '首次点击找回登陆密码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"loginId":' + '\"' + APP_ENV["loginId"] + '\"',
                    'WarningDesc': '没有找到:"loginId":' + APP_ENV["loginId"],
                    'isStop': ''
                }
            ]
        }
    },

    {
        # 首次点击找回登陆密码，更新页面及图片验证码
        'ModelName': 'Header_oneimg_update_passwork',
        'InterfaceName': 'anhuiuserapp_oneimg_update_passwork',
        'Header': Header_App_user_imgcode,
        "URL": Domains + "/api/user/code/generate_image",
        "Params": "",
        "Body": {}
        ,
        "Method": "Get",
        'InterfaceDesc': '首次点击找回登陆密码，更新页面及图片验证码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'imgToken',
                    'WarningDesc': '没有找到:imgToken',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 找回登陆密码页面获取短信验证码
        'ModelName': 'Header_oneimg_update_passwork',
        'InterfaceName': 'anhuiuserapp_oneimg_update_passwork',
        'Header': Header_App_user_imgcode,
        "URL": Domains + "/api/user/code/send_sms_visitor",
        "Params": "",
        "Body": {
            "imgCode": "{img_Code}",
            "imgToken": "{img_Token}",
            "mobile": "{mobile_d}",
            "smsType": "1307"
        },
        "Method": "Post",
        'InterfaceDesc': '找回登陆密码页面获取短信验证码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'imgToken',
                    'WarningDesc': '没有找到:imgToken',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app生成团购商品
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_gen',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/order/generate",
        "Params": "",
        "Body": {
            "isShoppingCartOrder": 'false',
            "createSource": 300,
            "phone": APP_ENV["phone"],
            "recvId": APP_ENV["recvId"],
            "areaId": 0,
            "bankPoint": 0,
            "unionPoint": 0,
            "addProducts": [{
                "merchantId": APP_ENV["merchantId"],
                "productId": APP_ENV["productId"],
                "quantity": 1,
                "vipQuantity": "0",
                "type": "1",
                "deliveryType": "1"
            }]
        },
        "Method": "Post",
        'InterfaceDesc': '生成团购商品',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'orderId',
                    'WarningDesc': '无法生成订单',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app生成名优特惠订单
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_my_gen',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/order/generate",
        "Params": "",
        "Body": {
            "isShoppingCartOrder": 'false',
            "createSource": 300,
            "phone": APP_ENV["myPhone"],
            "recvId": APP_ENV["myRecvId"],
            "areaId": APP_ENV['areaId'],
            "bankPoint": 0,
            "unionPoint": 0,
            "addProducts": [{
                "merchantId": APP_ENV["merchantId"],
                "productId": APP_ENV["myProductId"],
                "quantity": 1,
                "vipQuantity": "0",
                "type": "3",
                "deliveryType": "1"
            }]
        },
        "Method": "Post",
        'InterfaceDesc': '生成名优特惠订单',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'orderId',
                    'WarningDesc': '无法生成订单',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app团购支付
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_pay',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/cashier/payOrders",
        "Params": "",
        "Body": {
            "userName": "mc_30435775536",
            "orderId": "{orderId}",
            "cashOrgNo": 664,
            "ciphertextPwd": APP_ENV["payPwd"],
            "createSource": 300,
            "type": 7,
            "foilCardNum": "",
            "cardType": 1,
            "cardcouponsNo": "",
            "cardMerchantId": ""
        },
        "Method": "Post",
        'InterfaceDesc': '团购支付',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '0000',
                    'WarningDesc': '无法成功支付',
                    'isStop': ''
                }
            ]
        }
    },

    {
        # app团购退款
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_refund_do',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/refund/do",
        "Params": "",
        "Body": {
            "option": 2,
            "subOrderId": "{subOrderId}",
            "reason": "买多了",
            "productList": [{
                "productId": APP_ENV['productId'],
                "quantity": "1"
            }]
        },
        "Method": "Post",
        'InterfaceDesc': 'app团购退款',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'refundId',
                    'WarningDesc': 'app团购退款失败',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app二维码现金支付
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_qr_pay',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/cashier/payQrcodeOrders",
        "Params": "",
        "Body": {
            "pointOrgNo": 'null',
            "cashOrgNo": "664",
            "foilCardNum": "",
            "ciphertextPwd": "{ciphertextPwd}",
            "createSource": 300,
            "type": 7,
            "qrCode": "{qrCode}",
            "cardType": 1
        },
        "Method": "Post",
        'InterfaceDesc': '二维码现金支付',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '0000',
                    'WarningDesc': '无法成功支付',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app积分商品支付
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_points_pay',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/order/payExchangeOnline",
        "Params": "",
        "Body": {
            "productId": "{productId}",
            "quantity": 1
        },
        "Method": "Post",
        'InterfaceDesc': '积分商品支付',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '0000',
                    'WarningDesc': '无法成功支付',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app名优特惠支付
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_pay',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/cashier/payOrders",
        "Params": "",
        "Body": {
            "userName": "mc_30435775536",
            "orderId": "{orderId}",
            "cashOrgNo": 664,
            "ciphertextPwd": APP_ENV["payPwd"],
            "createSource": 300,
            "type": 7,
            "foilCardNum": "",
            "cardType": 1,
            "cardcouponsNo": "",
            "cardMerchantId": ""
        },
        "Method": "Post",
        'InterfaceDesc': '名优特惠支付',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '0000',
                    'WarningDesc': '无法成功支付',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # appC扫B惠付付款
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_pay',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/cashier/payOrders",
        "Params": "",
        "Body": {
            "userName": "mc_30435775536",
            "orderId": "{orderId}",
            "cashOrgNo": 664,
            "ciphertextPwd": APP_ENV["payPwd"],
            "createSource": 300,
            "type": 7,
            "foilCardNum": "",
            "cardType": 1,
            "cardcouponsNo": "",
            "cardMerchantId": ""
        },
        "Method": "Post",
        'InterfaceDesc': 'C扫B惠付付款',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '0000',
                    'WarningDesc': '无法成功支付',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app名优特惠确认收货
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_receipt',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/myorder/receipt",
        "Params": "",
        "Body": {
            "orderId": "{orderId}",
            "subOrderId": "{subOrderId}"
        },
        "Method": "Post",
        'InterfaceDesc': '名优特惠确认收货',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '确认收货成功',
                    'WarningDesc': '确认收货失败',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app名优特惠物流评价
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_order_shipping_comment',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/comment/shipping/add",
        "Params": "",
        "Body": {
            "subOrderId": "{subOrderId}",
            "orderId": "{orderId}",
            "trackinNo": "SFUIUIUIUIUI001",
            "deliveryCorpId": "100000002",
            "starLevel": "{starLevel}",
            "commentDescription": "简直太快了这个物流！！！！！{commentDescription}",
            "starLevelOne": "{starLevelOne}",
            "starLevelTwo": "{starLevelTwo}",
            "starLevelThree": "{starLevelThree}"
        },
        "Method": "Post",
        'InterfaceDesc': '名优特惠物流评价',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '添加评论成功',
                    'WarningDesc': '添加评论失败',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app获取团购码
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_ticketList',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/ticket/subOrderId",
        "Params": {
            "subOrderId": '{orderId}',
            "pageNumber": 1,
            "pageSize": 10,
            "lastPageNumber": 0,
            "firstRecordTime": 0,
            "lastRecordTime": 0,
            "totalCount": 0,
            "pageCount": 0
        },
        "Body": '',
        "Method": "Get",
        'InterfaceDesc': '获取团购码',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'ticketList',
                    'WarningDesc': '无法找到团购码列表',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app团购客户评价
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_add_comment',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/comment/product/add",
        "Params": '',
        "Body": {
            "productId": "{productId}",
            "orderId": "{orderId}",
            "bigOrderId": "{bigOrderId}",
            "orderType": "1",
            "starLevel": "{starLevel}",
            "commentDescription": "{comment}"
        },
        "Method": "Post",
        'InterfaceDesc': '团购客户评价',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '{}',
                    'WarningDesc': '评价失败',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # app名优特惠客户评价
        'ModelName': 'appTuangou',
        'InterfaceName': 'anhui_app_tuangou_add_my_comment',
        'Header': Header_App_user,
        "URL": Domains + "/api/user/comment/product/add",
        "Params": '',
        "Body": {
            "productId": "{productId}",
            "orderId": "{orderId}",
            "bigOrderId": "{bigOrderId}",
            "orderType": "3",
            "starLevel": "{starLevel}",
            "commentDescription": "{comment}"
        },
        "Method": "Post",
        'InterfaceDesc': '名优特惠客户评价',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '{}',
                    'WarningDesc': '评价失败',
                    'isStop': ''
                }
            ]
        }
    }
]
