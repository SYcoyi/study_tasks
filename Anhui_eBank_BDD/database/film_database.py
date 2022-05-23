#!/usr/bin/env python
# -- coding=utf-8 --
# coding: unicode_escape
"""
Created on 2019.02.18
安徽社区银行__银行管理平台自动化case
"""

Domain = 'https://test33.ubank365.com'
host = 'test3.ubank365.com'


##银行端登录Header
Header_App_user = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
    'Connection': 'keep-alive',
    'Cookie':'{Cookie}',
    'Host': 'test3.ubank365.com',
    'Upgrade-Insecure-Requests': '0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
    'Referer': Domain+'/anhui',
    'Content-Type':'application/json',
    'token': '{token}',
    'memberCode':'{memberCode}'
}

__all__ = ["film"]

film=[

    {
        # 通过渠道编码，展位类型获取展位信息
        'ModelName': 'film',
        'InterfaceName': 'get_file_homepage_one',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/actPublish/findByAppCodeAndBoothType.do",
        "Params": "",
        "Body": {
            "boothType":"booth_homepage_banner",
        },
        "Method": "Post",
        'InterfaceDesc': '通过渠道编码，展位类型获取展位信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 通过手机GPS定位获取城市信息
        'ModelName': 'film',
        'InterfaceName': 'get_file_homepage_two',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/city/location.do",
        "Params": "",
        "Body": {
            "latitude":"22.2707300000",
            "longitude":"113.5766800000",
        },
        "Method": "Post",
        'InterfaceDesc': '通过手机GPS定位获取城市信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取展位下的上架的活动列表
        'ModelName': 'film',
        'InterfaceName': 'get_file_homepage_third',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/actPublish/listBoothActs.do",
        "Params": "",
        "Body": {
            "boothCode":"c8549676b2ec4c2fb7fdeb5887a1a6e3",
        },
        "Method": "Post",
        'InterfaceDesc': '获取展位下的上架的活动列表',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查询在映影片列表
        'ModelName': 'film',
        'InterfaceName': 'get_file_homepage_four',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wofilm/getHotFilm.do",
        "Params": "",
        "Body": {
            "cityId":"4404",
            "pageSize":"10",
            "currentPage":"1",
        },
        "Method": "Post",
        'InterfaceDesc': '查询在映影片列表',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查询距离最近影院
        'ModelName': 'film',
        'InterfaceName': 'get_file_homepage_five',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/home/cinemaRecommend.do",
        "Params": "",
        "Body": {
            "latitude":"22.2707300000",
            "longitude":"113.5766800000",
            "cityId":"4404",
        },
        "Method": "Post",
        'InterfaceDesc': '查询距离最近影院',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取当前用户的电影卡信息
        'ModelName': 'film',
        'InterfaceName': 'get_file_homepage_six',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/bankVip/getMyBankVipInfo.do",
        "Params": "",
        "Body": {
        },
        "Method": "Post",
        'InterfaceDesc': '获取当前用户的电影卡信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取电影票地址
        'ModelName': 'film',
        'InterfaceName': 'get_file_city',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/city/selectedCity.do",
        "Params": "",
        "Body": {
        },
        "Method": "Post",
        'InterfaceDesc': '获取电影票地址',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查看活动奖品领取信息
        'ModelName': 'film',
        'InterfaceName': 'query_activity_prize_info',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/activity/queryActivityPrizeInfo.do",
        "Params": "",
        "Body": {
            'activityId':'{activityId}'
        },
        "Method": "Post",
        'InterfaceDesc': '查看活动奖品领取信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 电影票参加活动
        'ModelName': 'film',
        'InterfaceName': 'robbing_activity',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/activity/robbingActivity.do",
        "Params": "",
        "Body": {
            'activityId':'{activityId}',
            'recordKey':'155495176650473107086'
        },
        "Method": "Post",
        'InterfaceDesc': '电影票参加活动',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取会员开卡选项列表信息
        'ModelName': 'film',
        'InterfaceName': 'listbankvip',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/bankVip/listBankVip.do",
        "Params": "",
        "Body": {
        },
        "Method": "Post",
        'InterfaceDesc': '获取会员开卡选项列表信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取当前用户的会员卡信息
        'ModelName': 'film',
        'InterfaceName': 'get_my_bank_vip_info',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/bankVip/getMyBankVipInfo.do",
        "Params": "",
        "Body": {
        },
        "Method": "Post",
        'InterfaceDesc': '获取当前用户的会员卡信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到:成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 电影票获取当前用户
        'ModelName': 'film',
        'InterfaceName': 'base_info',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/user/baseInfo",
        "Params": "",
        "Body": {
        },
        "Method": "Post",
        'InterfaceDesc': '电影票获取当前用户',
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
        # 开通会员卡
        'ModelName': 'film',
        'InterfaceName': 'film_order_generate',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/order/generate",
        "Params": "",
        "Body": {
            "payPassWord":"",
            "bankPoint":0,
            "addProducts":[{
                "merchantId":"movie",
                "productId":"vipCard",
                "quantity":1,
                "type":"8",
                "vipCardId":"{vipCardId}",
                "vipCardMonths":12,
                "vipCardName":"会员卡（年卡）",
                "money":120
                }],
            "createSource":200
        },
        "Method": "Post",
        'InterfaceDesc': '开通会员卡',
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
        # 查看开卡记录
        'ModelName': 'film',
        'InterfaceName': 'query_film_order_card_record_list',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/bankVip/queryOrderCardRecordList.do",
        "Params": "",
        "Body": {
            "pageSize":"20",
            "currentPage":"1",
        },
        "Method": "Post",
        'InterfaceDesc': '查看开卡记录',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取影片详情信息
        'ModelName': 'film',
        'InterfaceName': 'get_film_collection_info_by_id',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wofilm/getFilmCollectionInfoByID.do",
        "Params": "",
        "Body": {
            "cityId":"3401",
            "filmCollectionId":"{filmCollectionId}",
            "filmName":"{filmName}",
        },
        "Method": "Post",
        'InterfaceDesc': '获取影片详情信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取视频剧照信息列表
        'ModelName': 'film',
        'InterfaceName': 'get_film_stills_by_id',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wofilm/getFilmStillsByID.do",
        "Params": "",
        "Body": {
            "filmCollectionId":"{filmCollectionId}",
        },
        "Method": "Post",
        'InterfaceDesc': '获取视频剧照信息列表',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 获取影片全部评论
        'ModelName': 'film',
        'InterfaceName': 'query_film_comment',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/comment/queryComment.do",
        "Params": "",
        "Body": {
            "targetId":"{targetId}",
            "movieName":"{movieName}",
            "type":"0",
            "currentPage":"1",
            "pageSize":"10",
        },
        "Method": "Post",
        'InterfaceDesc': '获取影片全部评论',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 写影评
        'ModelName': 'film',
        'InterfaceName': 'write_film_comment',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/comment/toComment.do",
        "Params": "",
        "Body": {
            "targetId":"{targetId}",
            "content":"自动化测试影评！",
            "stars":"5",
        },
        "Method": "Post",
        'InterfaceDesc': '写影评',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 点赞
        'ModelName': 'film',
        'InterfaceName': 'film_to_approve',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/comment/toApprove.do",
        "Params": "",
        "Body": {
            "type":"0",
            "commentId":"{commentId}",
        },
        "Method": "Post",
        'InterfaceDesc': '点赞',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查询城市包含区县列表
        'ModelName': 'film',
        'InterfaceName': 'get_film_location_area',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wocinema/getLocationArea.do",
        "Params": "",
        "Body": {
            "cityId":"3401",
        },
        "Method": "Post",
        'InterfaceDesc': '查询城市包含区县列表',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查询按经纬度定位离我最近影院列表
        'ModelName': 'film',
        'InterfaceName': 'get_cinema_by_distance',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wocinema/getCinemaByDistance.do",
        "Params": "",
        "Body": {
            "longitude":"117.233657",
            "latitude":"31.826956",
            "cityId":"3401",
            "areaId":"",
            "currentPage":"1",
            "pageSize":"10",
        },
        "Method": "Post",
        'InterfaceDesc': '查询按经纬度定位离我最近影院列表',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查看影院详情
        'ModelName': 'film',
        'InterfaceName': 'get_cinema_detail',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wocinema/getCinemaDetail.do",
        "Params": "",
        "Body": {
            "suppliers":"maoyan",
            "cinemaId":"{cinemaId}",
        },
        "Method": "Post",
        'InterfaceDesc': '查看影院详情',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查询影院在映影片列表
        'ModelName': 'film',
        'InterfaceName': 'get_cinema_film_show_list',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wocinema/getCinemaFilmShowList.do",
        "Params": "",
        "Body": {
            "cinemaCollectionId":"{cinemaCollectionId}",
        },
        "Method": "Post",
        'InterfaceDesc': '查询影院在映影片列表',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查看影院影片场次
        'ModelName': 'film',
        'InterfaceName': 'get_cinema_show_list',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wocinema/getCinemaShowList.do",
        "Params": "",
        "Body": {
            "filmId":"{filmId}",
            "cinemaCollectionId":"{cinemaCollectionId}",
        },
        "Method": "Post",
        'InterfaceDesc': '查看影院影片场次',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查看影院评价
        'ModelName': 'film',
        'InterfaceName': 'query_cinema_comment',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/comment/queryComment.do",
        "Params": "",
        "Body": {
            "targetId":"{targetId}",
            "movieName":"{movieName}",
            "type":"0",
            "currentPage":"1",
            "pageSize":"2",
        },
        "Method": "Post",
        'InterfaceDesc': '查看影院评价',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 评价电影院
        'ModelName': 'film',
        'InterfaceName': 'cinema_to_comment',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/comment/toComment.do",
        "Params": "",
        "Body": {
            "targetId":"{targetId}",
            "content":"自动化测试评价影院",
            "stars":"6",
        },
        "Method": "Post",
        'InterfaceDesc': '评价电影院',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查看动态座位图
        'ModelName': 'film',
        'InterfaceName': 'get_cinema_hall_seat',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/wocinema/getCinemaHallSeat.do",
        "Params": "",
        "Body": {
            "hallId":"{hallId}",
            "showId":"{showId}",
            "suppliers":"maoyan",
        },
        "Method": "Post",
        'InterfaceDesc': '查看动态座位图',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 锁定座位
        'ModelName': 'film',
        'InterfaceName': 'cinema_lock_seat',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/LockSeat/LockSeat.do",
        "Params": "",
        "Body": {
            "cinemaName":"{cinemaName}",
            "showId":"{showId}",
            "movieName":"{movieName}",
            "hallName":"{hallName}",
            "hallId":"",
            "price":"{price}",
            "seatNames":"1排1座",
            "version":"{version}",
            "showTime":"{showTime}",
            "couponDetailsId":"",
            "seatList":[{
                    "rowId":"1",
                    "columnId":"1",
                    "sectionId":"{sectionId}",
                    "seatNo":"{seatNo}"
                }],
            "areaId":"3401",
            "areaName":"合肥市",
            "suppliers":"maoyan"
        },
        "Method": "Post",
        'InterfaceDesc': '锁定座位',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 查询订单信息
        'ModelName': 'film',
        'InterfaceName': 'query_cinema_order_info',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/order/queryOrderInfo.do",
        "Params": "",
        "Body": {
            "orderId": "{orderId}",
        },
        "Method": "Post",
        'InterfaceDesc': '查询订单信息',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 购买电影票
        'ModelName': 'film',
        'InterfaceName': 'cinema_order_generate',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/order/generate",
        "Params": "",
        "Body": {
            "movieOrderId":"{movieOrderId}",
            "payPassWord":"",
            "bankPoint":0,
            "isMovieVip":False,
            "addProducts":[{
                "merchantId":"movie",
                "productId":"movie",
                "quantity":"1",
                "type":"7",
                "money":"{money}",
                "moviePicture":"https://p0.meituan.net/moviemachine/f7d2ad70eb79d6d9b8a197713db9b8c41711752.jpg@128w_180h",
                "movieVipDiscount":"{movieVipDiscount}",
            }],
            "createSource":200
        },
        "Method": "Post",
        'InterfaceDesc': '购买电影票',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '"code":"0000"',
                    'WarningDesc': '没有找到："code":"0000"',
                    'isStop': ''
                }
            ]
        }
    },
    {
        # 解锁座位
        'ModelName': 'film',
        'InterfaceName': 'unlock_cinema_seat',
        'Header': Header_App_user,
        "URL": Domain + "/api/film/LockSeat/unLockSeat.do",
        "Params": "",
        "Body": {
            "orderId":"{orderId}",
        },
        "Method": "Post",
        'InterfaceDesc': '解锁座位',
        'Assertion': {
            'SearchInfo': [
                {
                    'Scope': 'body',
                    'Contain': '成功',
                    'WarningDesc': '没有找到：成功',
                    'isStop': ''
                }
            ]
        }
    },
]