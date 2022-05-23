#!/usr/bin/env python
# -- coding=utf-8 --
# coding: unicode_escape
"""
Created on 2019.01.31
安徽社区银行__商户PC端自动化case
"""

# 接口对象注入在类的__all__函数中，
from database.__global_params import MWECHANT_ENV

__all__ = ['INTERFACE_PARAMS_Merchant']
Domain = MWECHANT_ENV["Domain"]
host = MWECHANT_ENV["host"]

##商户PC端登录Header
Header_login = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': host,
    'Upgrade-Insecure-Requests': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': Domain + '/anhui/admin/merchant/index.html',
    'Content-Type': 'application/json'
}
# 商户PC端_名优商品发货Header
Header_Logined = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie': '',
    'Host': host,
    'Upgrade-Insecure-Requests': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': Domain + '/anhui/admin/merchant/delivery.html?sOId=765405F40001&t=0&oId=765405F08000&id=',
    'Content-Type': 'application/json',
    'uid': '{userId}',
    'token': '{token}'
}
# 接口参数对象
# 请保证参数在调用后都是静态的
# 如果其中的值在用例阶段才被赋值请将值用{}包裹
INTERFACE_PARAMS_Merchant = [
    {
        ##商户PC端登录接口
        'ModelName': 'AnhuiMerchantPC_Login',
        'InterfaceName': 'AnhuiMerchantPC_Login',
        'Header': Header_login,
        'URL': Domain + '/api/merchant/verify',
        'Params': '',
        'Body': {"userName": "{userName}", "password": "{password}", "code": "", "ko": ""},
        'Method': 'Post',
        'InterfaceDesc': '商户端登陆',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"userName":"' + MWECHANT_ENV['username'] + '"',
                    'WarningDesc': '商户PC端登录异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_商品管理_团购商品查询
        'ModelName': 'AnhuiMerchantPC_ProductList',
        'InterfaceName': 'AnhuiMerchantPC_ProductList_TuanGou',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/product/list',
        'Params': '',
        'Body': {"pageSize": 10, "pageNumber": 1, "startTime": "", "endTime": "", "type": "1", "lastPageNumber": 0,
                 "firstRecordTime": 0, "lastRecordTime": 0},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_ProductList_TuanGou',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'productList'
                    },
                    'Scope': 'body',
                    'Contain': '"productList"',
                    'WarningDesc': '商户PC端团购商品查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"1"',
                    'WarningDesc': '商户PC端团购商品查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_商品管理_名优特惠商品列表查询
        'ModelName': 'AnhuiMerchantPC_ProductList',
        'InterfaceName': 'AnhuiMerchantPC_ProductList_MingYou',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/product/list',
        'Params': '',
        'Body': {"productName": "", "type": 3, "startTime": "", "endTime": "", "isMarketable": "-1", "auditState": "",
                 "orgCode": "340000", "pageSize": 10, "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_ProductList_MingYou',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'productList'
                    },
                    'Scope': 'body',
                    'Contain': '"productList"',
                    'WarningDesc': '商户PC端名优特惠查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"3"',
                    'WarningDesc': '商户PC端名优特惠查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_交易管理_团购订单查询
        'ModelName': 'AnhuiMerchantPC_OrderList',
        'InterfaceName': 'AnhuiMerchantPC_OrderList_TuanGou',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/qfg',
        'Params': '',
        'Body': {"outletId": "", "type": "1", "subOrderId": "", "orderStatus": "", "startTime": "", "endTime": "",
                 "deliveryStatus": "", "pageSize": 10, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0,
                 "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_OrderList_TuanGou',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'orderList'
                    },
                    'Scope': 'body',
                    'Contain': '"orderList"',
                    'WarningDesc': '商户PC端团购订单查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"1"',
                    'WarningDesc': '商户PC端团购订单查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_交易管理_名优特惠订单查询
        'ModelName': 'AnhuiMerchantPC_OrderList',
        'InterfaceName': 'AnhuiMerchantPC_OrderList_MingYou',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/qfg',
        'Params': '',
        'Body': {"outletId": "", "type": "3", "subOrderId": "", "orderStatus": "", "startTime": "", "endTime": "",
                 "deliveryStatus": "", "pageSize": 10, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0,
                 "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_OrderList_MingYou',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'orderList'
                    },
                    'Scope': 'body',
                    'Contain': '"orderList"',
                    'WarningDesc': '商户PC端名优特惠订单查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"3"',
                    'WarningDesc': '商户PC端名优特惠订单查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_交易管理_扫码收银订单查询
        ##扫码收银（C扫B/面对面收银）：
        # 1、商户APP使用“订单二维码”生成包含订单金额的二维码，然后个人端扫描商户端该二维码
        # 2、商户PC端--交易管理--收银台--输入金额后生成二维码，个人端扫描付款。
        'ModelName': 'AnhuiMerchantPC_OrderList',
        'InterfaceName': 'AnhuiMerchantPC_OrderList_CtoB',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/qfg',
        'Params': '',
        'Body': {"outletId": "", "type": "8", "subOrderId": "", "orderStatus": "", "startTime": "{sdt}",
                 "endTime": "{edt}",
                 "deliveryStatus": "", "pageSize": 10, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0,
                 "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_OrderList_CtoB',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'orderList'
                    },
                    'Scope': 'body',
                    'Contain': '"orderList"',
                    'WarningDesc': '商户PC端—扫码收银(C扫B)订单查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"1"',
                    'WarningDesc': '商户PC端—扫码收银(C扫B)订单查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_交易管理_付款码支付订单查询
        ##付款码支付（B扫C）：商户APP端使用“扫码收款”，扫描个人端二维码。优先使用积分进行抵扣
        'ModelName': 'AnhuiMerchantPC_OrderList',
        'InterfaceName': 'AnhuiMerchantPC_OrderList_BtoC',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/qfg',
        'Params': '',
        'Body': {"outletId": "", "type": "10", "subOrderId": "", "orderStatus": "", "startTime": "{sdt}",
                 "endTime": "{edt}",
                 "deliveryStatus": "", "pageSize": 10, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0,
                 "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_OrderList_BtoC',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'orderList'
                    },
                    'Scope': 'body',
                    'Contain': '"orderList"',
                    'WarningDesc': '商户PC端—付款码支付(B扫C)订单查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"0"',
                    'WarningDesc': '商户PC端—付款码支付(B扫C)订单查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_交易管理_惠付订单查询
        ##惠付（惠付-买单付）：个人端进入商家门店点击“买单”，输入消费金额后可使用该门店设置的折扣优惠，可以直接进行抵扣。所优惠金额由门店自己承担。（有积分会默认使用积分）
        'ModelName': 'AnhuiMerchantPC_OrderList',
        'InterfaceName': 'AnhuiMerchantPC_OrderList_HuiFu',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/qfg',
        'Params': '',
        'Body': {"outletId": "", "type": "9", "subOrderId": "", "orderStatus": "", "startTime": "{sdt}",
                 "endTime": "{edt}",
                 "deliveryStatus": "", "pageSize": 10, "lastPageNumber": 0, "firstRecordTime": 0, "lastRecordTime": 0,
                 "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_OrderList_HuiFu',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'orderList'
                    },
                    'Scope': 'body',
                    'Contain': '"orderList"',
                    'WarningDesc': '商户PC端惠付订单查询异常',
                    'IsStop': ''
                },
                {
                    'before': {
                        'type': 1,
                        'content': 'type'
                    },
                    'Scope': 'body',
                    'Contain': '"type":"0"',
                    'WarningDesc': '商户PC端惠付订单查询异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_交易额统计
        'ModelName': 'AnhuiMerchantPC_Trade_Count',
        'InterfaceName': 'AnhuiMerchantPC_Trade_Count',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/funpay/logic/query/queryTradeMoneyAndCount',
        'Params': '',
        'Body':
            {
                'beginTime': '{beginTime}',  ##开始时间
                'endTime': '{endTime}',  ###结束时间
                'orderStatus': '{orderStatus}',  ##订单状态
                'outletId': '{outletId}',  ##门店ID
                'subMerchantId': '{subMerchantId}',  ###商户ID
                'tradeChannel': '{tradeChannel}',  ##交易渠道
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_Trade_Count',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'message',
                        'WarningDesc': '查询成功',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##商户PC端_名优商品发货
        'ModelName': 'AnhuiMerchantPC_OrderList_Ship',
        'InterfaceName': 'AnhuiMerchantPC_OrderList_Ship',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/ship',
        'Params': '',
        'Body':
            {
                'deliveryCorpId': "100000002",  ##物流ID
                'deliveryCorpName': "顺丰速运",  ###物流公司名称
                'orderId': '{orderId}',  ##订单编号
                'subOrderId': '{subOrderId}',  ##子订单编号
                'trackingNo': "SFUIUIUIUIUI001",  ###物流单号
            },
        'Method': 'Post',
        'InterfaceDesc': '名优特惠发货',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '{}',
                        'WarningDesc': '发货成功',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##商户PC端_提货码列表查询
        'ModelName': 'AnhuiMerchantPC_staff_qr',
        'InterfaceName': 'AnhuiMerchantPC_orderqcl',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/qcl',
        'Params': '',
        'Body':
            {"type": 1, "status": 2, "startDate": "{sdt}", "endDate": "{edt}", "userName": "", "outletId": "",
             "securitiesNo": "", "hist": "0", "pageSize": 10, "pageNumber": 1},
        'Method': 'Post',
        'InterfaceDesc': '提货码列表查询',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'before': {
                            'type': 1,
                            'content': 'message'
                        },
                        'Scope': 'body',
                        'Contain': '查询无记录',
                        'WarningDesc': '发货成功',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##商户PC端_团购提货
        'ModelName': 'AnhuiMerchantPC_staff_qr',
        'InterfaceName': 'AnhuiMerchantPC_seall',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/seall',
        'Params': '',
        'Body':
            {"mustValidTicketId": "{ticketId}", "productIds": "{productIds}", "type": "1",
             "memberCode": "{memberCode}", "subOrderId": "{subOrderId}", "quantitys": "1"},
        'Method': 'Post',
        'InterfaceDesc': '团购提货',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'successTicketCodes',
                        'WarningDesc': '提货失败',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##商户PC端_新增团购商品
        'ModelName': 'AnhuiMerchantPC_AddProduct',
        'InterfaceName': 'AnhuiMerchantPC_AddProduct_TuanGou',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/product/add',
        'Params': '',
        'Body':
            {
                'name': '{name}',  ##商品简称
                'fullName': '{fullName}',  ###商品名称
                'store': '1000',  ##商品原始库存
                'marketPrice': '100',  ##市场价
                'price': '80',  ###销售价/团购价
                'startTime': '{startTime}',  ##团购开始时间
                'endTime': '{endTime}',  ##团购结束时间
                'expireEndTime': '{expireEndTime}',  ##验码有效期
                'briefIntroduction': '副标题副标题',
                'buyKnow': '购买须知购买须知',
                'introduction': '商品详情商品详情',
                'imgList': [
                    {
                        'isDefault': 'false',
                        'source': '3f58dfe2-0a37-48e7-b86c-f3571636ae49',
                        'large': '3f58dfe2-0a37-48e7-b86c-f3571636ae49',
                        'medium': '3f58dfe2-0a37-48e7-b86c-f3571636ae49',
                        'thumbnail': '3f58dfe2-0a37-48e7-b86c-f3571636ae49'
                    }
                ],
                'type': '1',  ##商品类型，1为团购商品
                'max': '{max}',  ###限购数量
                'boxType': '1',  ##是否提交审核，1为提交，0为不提交
                'categoryId': '{categoryId}',  ##商品分类，如农副特产/餐饮美食等
                'roleId': '100000001',
                'userName': '{userName}',  ##录入当前商品的操作员名称，当前登录用户名
                'buyMethod': '0'  ###购买方式：0不限制，1仅限杜鹃信用卡
            },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_AddProduct_TuanGou',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': '"result":"0000"',
                        'WarningDesc': '商户PC端新增团购商品异常',
                        'IsStop': ''
                    },
                ]
            }
    },
    {
        ##商户PC端_新增门店
        'ModelName': 'AnhuiMerchantPC_Outlet_Add',
        'InterfaceName': 'AnhuiMerchantPC_Outlet_Add',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/add',
        'Params': '',
        'Body': {
            'acctName': '',
            'acctNumber': '',  # 优惠详情
            'address': 'auto地址',  # 详细地址
            'areaId': '100000017',  # 区号
            "businessHours": "{businessHours}",  # 营业时间
            'categoryInfo': [100000010],  # 门店分类
            'contactName': '{contactName}',  # 联系人姓名
            'contactPhone': '{contactPhone}',  # 联系人号码
            'description': '主营&&&&商品类型',  # 门店描述包含主营和商品类型
            'discountCode': '安徽农金',  # 优惠详情
            'discountRate': '{discountRate}',  # 优惠详情折扣
            'fax': '',  # 传真
            'imgList': [
                {
                    'isDefault': 'true',
                    'source': '80fe70df-a3cd-4fb7-994b-7a88b3da588e',
                    'large': '80fe70df-a3cd-4fb7-994b-7a88b3da588e',
                    'medium': '80fe70df-a3cd-4fb7-994b-7a88b3da588e',
                    'thumbnail': '80fe70df-a3cd-4fb7-994b-7a88b3da588e'
                },
                {
                    'isDefault': 'false',
                    'large': '698443a7-6ebc-4db9-a168-02b16f31e720',
                    'medium': '698443a7-6ebc-4db9-a168-02b16f31e720',
                    'source': '698443a7-6ebc-4db9-a168-02b16f31e720',
                    'thumbnail': '698443a7-6ebc-4db9-a168-02b16f31e720'
                }
            ],
            'latitude': '{latitude}',  # 经度
            'longitude': '{longitude}',  # 纬度
            'outletFullname': '{outletFullname}',  # 门店全称
            'outletName': '{outletName}',  # 门店名称
            'phone': '{phone}',  # 手机号
            'preferDetails': '{preferDetails}'  # 优惠详情
        },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_Outlet_Add',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'message',
                    'WarningDesc': '门店新增成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_门店列表查询
        'ModelName': 'AnhuiMerchantPC_Outlet_List',
        'InterfaceName': 'AnhuiMerchantPC_Outlet_List',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/list',
        'Params': '',
        'Body': {
            "address": "",
            "auditState": "{auditState}",
            "outletId": "{outletId}",
            "outletName": "",
            "pageNumber": "{pageNumber}",
            "pageSize": "{pageSize}"
        },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_Outlet_List',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'outletList'
                    },
                    'Scope': 'body',
                    'Contain': 'outletList',
                    'WarningDesc': '门店列表查询成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_门店详情查询
        'ModelName': 'AnhuiMerchantPC_Outlet_Details',
        'InterfaceName': 'AnhuiMerchantPC_Outlet_Details',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/ld',
        'Params': {
            'outletId': '{outletId}',
            'type': '{type}',
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': 'AnhuiMerchantPC_Outlet_Details',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'outletDetail',
                    'WarningDesc': '门店详情界面',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_门店修改
        'ModelName': 'AnhuiMerchantPC_Outlet_Modify',
        'InterfaceName': 'AnhuiMerchantPC_Outlet_Modify',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/mdy',
        'Params': '',
        'Body': {
            'acctName': '',
            'acctNumber': '',  # 优惠详情
            'address': '{address}',  # 详细地址
            'areaId': '{areaId}',  # 区号
            "businessHours": "{businessHours}",  # 营业时间
            'categoryInfo': [100000010],  # 门店分类
            'contactName': '{contactName}',  # 联系人姓名
            'contactPhone': '{contactPhone}',  # 联系人号码
            'description': '主营&&&&商品类型',  # 门店描述包含主营和商品类型
            'discountCode': '安徽农金',  # 优惠详情
            'discountRate': '{discountRate}',  # 优惠详情折扣
            'editAuditState': '1',
            'fax': '',  # 传真
            'imgList': [
                {
                    'isDefault': 'true',
                    'source': '63026375-2251-4f5e-aa7b-814e1d475d8d',
                    'large': '63026375-2251-4f5e-aa7b-814e1d475d8d',
                    'medium': '63026375-2251-4f5e-aa7b-814e1d475d8d',
                    'thumbnail': '63026375-2251-4f5e-aa7b-814e1d475d8d'
                },
                {
                    'isDefault': 'false',
                    'large': 'abb387fa-83d3-4a54-b374-427b286939f2',
                    'medium': 'abb387fa-83d3-4a54-b374-427b286939f2',
                    'source': 'abb387fa-83d3-4a54-b374-427b286939f2',
                    'thumbnail': 'abb387fa-83d3-4a54-b374-427b286939f2'
                }
            ],
            'latitude': '{latitude}',  # 经度
            'longitude': '{longitude}',  # 纬度
            'outletFullname': '{outletFullname}',  # 门店全称
            'outletName': '{outletName}',  # 门店名称
            'outletId': '{outletId}',  # 门店ID
            'phone': '{phone}',  # 手机号
            'preferDetails': '{preferDetails}'  # 优惠详情
        },
        'Method': 'Get',
        'InterfaceDesc': 'AnhuiMerchantPC_Outlet_Modify',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'message',
                    'WarningDesc': '修改成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_新增用户
        'ModelName': 'AnhuiMerchantPC_User',
        'InterfaceName': 'AnhuiMerchantPC_User_Add',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/moua',
        'Params': '',
        'Body': {"outletId": "{outletId}",
                 "username": "{username}",
                 "realname": "{realname}",
                 "phone": "{phone}",
                 "resourceIds": [200000001, 200000002, 200000003, 200000004, 200000005, 200000006, 200000007, 200000008,
                                 200000009, 200000010, 200000011, 200000012, 200000013, 200000014, 200000015, 200000016,
                                 200000017, 200000021, 200000022, 200000018, 200000019, 300000366, 300000367, 300000368,
                                 300000369, 300000371, 300000374, 300000375, 300000376, 300000377, 300000378]
                 },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_User_Add',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '{}',
                    'WarningDesc': '商户PC端新增用户异常',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_用户修改
        'ModelName': 'AnhuiMerchantPC_User',
        'InterfaceName': 'AnhuiMerchantPC_User_Modify',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/moup',
        'Params': '',
        'Body': {
            "id": "{id}",
            "outletId": "{outletId}",
            "username": "{username}",
            "realname": "{realname}",
            "phone": "{phone}",
            "resourceIds": [200000001, 200000002, 200000003, 200000004, 200000005, 200000006, 200000007, 200000008,
                            200000009, 200000010, 200000011, 200000012, 200000013, 200000014, 200000015, 200000016,
                            200000017, 200000021, 200000022, 200000018, 200000019, 300000366, 300000367, 300000368,
                            300000369, 300000371, 300000374, 300000375, 300000376, 300000377, 300000378]
        },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_User_Modify',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '{}',
                    'WarningDesc': '商户PC端用户修改成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_重置用户密码
        'ModelName': 'AnhuiMerchantPC_User',
        'InterfaceName': 'AnhuiMerchantPC_User_PwdReset',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/reset',
        'Params': '',
        'Body': {
            "mobile": "{mobile}",
            "userId": "{userId}"
        },
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_User_PwdReset',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '{}',
                    'WarningDesc': '商户PC端用户密码重置成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_用户列表
        'ModelName': 'AnhuiMerchantPC_User',
        'InterfaceName': 'AnhuiMerchantPC_User_List',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/outlet/qall',
        'Params': '',
        'Body': {"outletId": "{outletId}"},
        'Method': 'Post',
        'InterfaceDesc': 'AnhuiMerchantPC_User_LIst',
        'Assertion': {
            'SearchInfo': [
                {
                    'before': {
                        'type': 1,
                        'content': 'areaId'
                    },
                    'Scope': 'body',
                    'Contain': 'areaId',
                    'WarningDesc': '用户列表查询成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_用户权限查看
        'ModelName': 'AnhuiMerchantPC_UserOrigin_List',
        'InterfaceName': 'AnhuiMerchantPC_UserOrigin_List',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/resource/byUserInfo',
        'Params': {
            "userId": "{userId}",
            "origin": "list"
        },
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': 'AnhuiMerchantPC_UserOrigin_List',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': 'rootResources',
                    'WarningDesc': '用户权限查询成功',
                    'IsStop': ''
                },
            ]
        }
    },
    {
        ##商户PC端_口碑管理_商品评论列表
        'ModuleName': 'AnhuiMerchantPC_MerchandiseReview_List',
        'InterfaceName': 'AnhuiMerchantPC_MerchandiseReview_List',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/qpcl',
        'Params': '',
        'Body': {
            "isReply": "{isReply}",
            "pageNumber": "{pageNumber}",
            "pageSize": "{pageSize}",
            "pointEndTime": "{edt}",
            "pointStartTime": "{sdt}",
            "productName": "",
            "starLevel": "{starLevel}"
        },
        'Method': 'Post',
        'InterfaceDesc': '商品评价列表',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': 'page',
                        'WarningDesc': '商品评价列表查询成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商品评论
        'ModuleName': 'AnhuiMerchantPC_Merchandise_Review',
        'InterfaceName': 'AnhuiMerchantPC_Merchandise_Review',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/rpy',
        'Params': '',
        'Body': {
            "commentId": "{commentId}",
            "productId": "{productId}",
            "recomment": "{recomment}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': '"message":"0000"',
                        'WarningDesc': '商品评价成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_创建二维码订单
        'ModuleName': 'AnhuiMerchantPC_Order',
        'InterfaceName': 'AnhuiMerchantPC_Order_Create_Code',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/order/fcreate',
        'Params': '',
        'Body': {"money": "{money}", "remark": ""},
        'Method': 'Post',
        'InterfaceDesc': '创建二维码订单',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': 'qrcode',
                        'WarningDesc': '二维码创建失败',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商品评论_名优特惠评论回复
        'ModuleName': 'AnhuiMerchantPC_Merchandise_Review',
        'InterfaceName': 'AnhuiMerchantPC_Merchandise_Review',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/rpy',
        'Params': '',
        'Body': {
            "commentId": "{commentId}",
            "productId": "{productId}",
            "recomment": "{recomment}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': '"message":"0000"',
                        'WarningDesc': '商品评价成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商品评论详情界面
        'ModuleName': 'AnhuiMerchantPC_MerchandiseReview_Details',
        'InterfaceName': 'AnhuiMerchantPC_MerchandiseReview_Details',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/qpd',
        'Params': '',
        'Body': {
            "commentId": "{commentId}",
            "orderId": "{orderId}",
            "productId": "{productId}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': 'commentId',
                        'WarningDesc': '商品评价详情界面显示正确',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商品评价回复
        'ModuleName': 'AnhuiMerchantPC_MerchandiseReview',
        'InterfaceName': 'AnhuiMerchantPC_MerchandiseReview_Action',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/rpy',
        'Params': '',
        'Body': {"commentId": "{commentId}", "productId": "{productId}", "recomment": "{recomment}"},
        'Method': 'Post',
        'InterfaceDesc': '商品评价回复',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': '操作成功',
                        'WarningDesc': '无法回复',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端创建商品
        'ModuleName': 'AnhuiMerchantPC_MerchandiseReview',
        'InterfaceName': 'AnhuiMerchantPC_Product_Add',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/product/add',
        'Params': '',
        'Body': {"name": "{name}", "fullName": "{fullName}", "store": "999999", "marketPrice": "999", "price": "4",
                 "startTime": "{startTime}", "endTime": "{endTime}",
                 "expireEndTime": "2019-12-31 11:17:10", "briefIntroduction": "副标题", "buyKnow": "购买须知",
                 "introduction": "商品详情", "imgList": [
                {"isDefault": False, "source": "a6ef35ca-2cb5-4790-bf43-1f7dc5fb13f6",
                 "large": "a6ef35ca-2cb5-4790-bf43-1f7dc5fb13f6", "medium": "a6ef35ca-2cb5-4790-bf43-1f7dc5fb13f6",
                 "thumbnail": "a6ef35ca-2cb5-4790-bf43-1f7dc5fb13f6"}], "type": "1", "max": "0", "boxType": "1",
                 "categoryId": "100000000", "roleId": "100000000", "userName": MWECHANT_ENV['username'],
                 "buyMethod": "0"},
        'Method': 'Post',
        'InterfaceDesc': '商户PC端创建商品',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': '0000',
                        'WarningDesc': '商户PC端创建商品失败',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商户评论列表
        'ModuleName': 'AnhuiMerchantPC_MerchantReview_List',
        'InterfaceName': 'AnhuiMerchantPC_MerchantReview_List',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/qoc',
        'Params': '',
        'Body': {
            "begTime": "2019-01-27",
            "endTime": "2019-03-24",
            "isReply": "",
            "outletName": "",
            "pageNumber": "{pageNumber}",
            "pageSize": "{pageSize}",
            "starLevel": "{starLevel}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': 'message',
                        'WarningDesc': '查询成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商户评论
        'ModuleName': 'AnhuiMerchantPC_Merchant_Review',
        'InterfaceName': 'AnhuiMerchantPC_Merchant_Review',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/roc',
        'Params': '',
        'Body': {
            "id": "{id}",
            "recomment": "{recomment}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': '{}',
                        'WarningDesc': '商户评价失败',
                        'IsStop': ''
                    },
                ]
            },
    },

    {
        ##商户PC端_口碑管理_商户评论
        'ModuleName': 'AnhuiMerchantPC_Merchant_Review',
        'InterfaceName': 'AnhuiMerchantPC_Merchant_Review',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/roc',
        'Params': '',
        'Body': {
            "id": "{id}",
            "recomment": "{recomment}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': '{}',
                        'WarningDesc': '商户评价失败',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_商户评论详情
        'ModuleName': 'AnhuiMerchantPC_MerchantReview_Details',
        'InterfaceName': 'AnhuiMerchantPC_MerchantReview_Details',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/pcd',
        'Params': '',
        'Body': {
            "id": "{id}"
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': 'id',
                        'WarningDesc': '商户评价成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_物流评价列表
        'ModuleName': 'AnhuiMerchantPC_Delivery_List',
        'InterfaceName': 'AnhuiMerchantPC_Delivery_List',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/shipping',
        'Params': '',
        'Body': {
            "pageNumber": "{pageNumber}",
            "pageSize": "{pageSize}",
            "shippingBegTime": "{shippingBegTime}",
            "shippingEndTime": "{shippingEndTime}",
            "trackingNo": "",
        },
        'Method': 'Post',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'body',
                        'Contain': 'page',
                        'WarningDesc': '物流列表查询成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_口碑管理_物流评价详情
        'ModuleName': 'AnhuiMerchantPC_Delivery_Details',
        'InterfaceName': 'AnhuiMerchantPC_Delivery_Details',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/comment/delivery/obtainExpress',
        'Params': {
            "deliveryCorpId": "{deliveryCorpId}",
            "trackinNo": "{trackinNo}"
        },
        'Body': '',
        'Method': 'Get',
        'Assertion':
            {
                'SearchInfo': [
                    {

                        'Scope': 'body',
                        'Contain': 'express',
                        'WarningDesc': '物流详情查看成功',
                        'IsStop': ''
                    },
                ]
            },
    },
    {
        ##商户PC端_退出登录
        'ModelName': 'AnhuiMerchantPC_LogOut',
        'InterfaceName': 'AnhuiMerchantPC_LogOut',
        'Header': Header_Logined,
        'URL': Domain + '/api/merchant/loginOut',
        'Params': '',
        'Body': '',
        'Method': 'Get',
        'InterfaceDesc': 'AnhuiMerchantPC_LogOut',
        'Assertion':
            {
                'SearchInfo': [
                    {
                        'Scope': 'header',
                        'Contain': 'm_token=""',
                        'WarningDesc': '商户PC端用户登出异常',
                        'IsStop': ''
                    },
                ]
            }

    },
]
