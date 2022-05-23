#!/usr/bin/env python
# -- coding=utf-8 --
import logging

from behave import given, when, then
from utils.http_manager import send_request
import json
from utils.readTools import launch_request
from utils.tools import push_replaceParams, assertion_tools
import utils.generatorTools as generatorTools
import time

number = 3

@when('通过渠道编码，展位类型获取展位信息')
def get_file_homepage_one(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_homepage_one')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('通过手机GPS定位获取城市信息')
def get_file_homepage_two(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_homepage_two')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('获取展位下的上架的活动列表')
def get_file_homepage_third(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_homepage_third')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.film_activityId = generatorTools.StringBar.LRFindString(result.text, '"activityId":"', '",')[0]

@when('查询在映影片列表')
def get_file_homepage_four(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_homepage_four')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.filmCollectionId = generatorTools.StringBar.LRFindString(result.text, '"filmCollectionId":"', '",')[0]
    context.filmName = generatorTools.StringBar.LRFindString(result.text, '"filmName":"', '",')[0]

@when('查询距离最近影院')
def get_file_homepage_five(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_homepage_five')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('获取当前用户的电影卡信息')
def get_file_homepage_six(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_homepage_six')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@then('获取电影票城市')
def get_file_city(context):
    ParamsObject = launch_request('film_database', 'film', 'get_file_city')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('查看活动奖品领取信息')
def query_activity_prize_info(context):
    ParamsObject = launch_request('film_database', 'film', 'query_activity_prize_info')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', activityId=context.film_activityId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('电影票参加活动')
def robbing_activity(context):
    ParamsObject = launch_request('film_database', 'film', 'robbing_activity')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', activityId=context.film_activityId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('获取会员开卡选项列表信息')
def listbankvip(context):
    ParamsObject = launch_request('film_database', 'film', 'listbankvip')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.film_vipCardId = generatorTools.StringBar.LRFindString(result.text, '"id":"', '",')[-1]

@given('获取当前用户的会员卡信息')
def get_my_bank_vip_info(context):
    ParamsObject = launch_request('film_database', 'film', 'get_my_bank_vip_info')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('电影票获取当前用户')
def base_info(context):
    ParamsObject = launch_request('film_database', 'film', 'base_info')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('开通会员卡')
def film_order_generate(context):
    ParamsObject = launch_request('film_database', 'film', 'film_order_generate')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', vipCardId=context.film_vipCardId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@then('查看开卡记录')
def query_film_order_card_record_list(context):
    ParamsObject = launch_request('film_database', 'film', 'query_film_order_card_record_list')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('查询在映影片列表')
def get_hot_film(context):
    ParamsObject = launch_request('film_database', 'film', 'get_hot_film')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@then('获取影片详情信息')
def get_film_collection_info_by_id(context):
    ParamsObject = launch_request('film_database', 'film', 'get_film_collection_info_by_id')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', filmCollectionId=context.filmCollectionId,filmName=context.filmName)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@then('获取视频剧照信息列表')
def get_film_stills_by_id(context):
    ParamsObject = launch_request('film_database', 'film', 'get_film_stills_by_id')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', filmCollectionId=context.filmCollectionId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('获取影片全部评论')
def query_film_comment(context):
    ParamsObject = launch_request('film_database', 'film', 'query_film_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', targetId=context.filmCollectionId,movieName=context.filmName)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.film_commentId = generatorTools.StringBar.LRFindString(result.text, '"commentId":"', '",')[0]

@when('写影评')
def write_film_comment(context):
    ParamsObject = launch_request('film_database', 'film', 'write_film_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', targetId=context.filmCollectionId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@then('点赞')
def film_to_approve(context):
    ParamsObject = launch_request('film_database', 'film', 'film_to_approve')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', commentId=context.film_commentId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('查询城市包含区县列表')
def get_film_location_area(context):
    ParamsObject = launch_request('film_database', 'film', 'get_film_location_area')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('查询按经纬度定位离我最近影院列表')
def get_cinema_by_distance(context):
    ParamsObject = launch_request('film_database', 'film', 'get_cinema_by_distance')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.film_cinemaId = generatorTools.StringBar.LRFindString(result.text, '"cinemaId":"', '",')[0]

@when('查看影院详情')
def get_cinema_detail(context):
    ParamsObject = launch_request('film_database', 'film', 'get_cinema_detail')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', cinemaId=context.film_cinemaId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.cinemaName = generatorTools.StringBar.LRFindString(result.text, '"cinemaName":"', '",')[0]

@when('查询影院在映影片列表')
def get_cinema_film_show_list(context):
    ParamsObject = launch_request('film_database', 'film', 'get_cinema_film_show_list')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', cinemaCollectionId=context.film_cinemaId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.filmId = generatorTools.StringBar.LRFindString(result.text, '"filmId":"', '",')[0]
    context.cinema_filmId = generatorTools.StringBar.LRFindString(result.text, '"filmName":"', '",')[0]

@then('查看影院影片场次')
def get_cinema_show_list(context):
    ParamsObject = launch_request('film_database', 'film', 'get_cinema_show_list')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', filmId=context.filmId,cinemaCollectionId=context.film_cinemaId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    # 取第十个值，避免出现电影快开场无法购票或无法锁座的情况
    context.cinema_showId = generatorTools.StringBar.LRFindString(result.text, '"showId":"', '",')[number]
    context.cinema_hallName = generatorTools.StringBar.LRFindString(result.text, '"hallName":"', '",')[number]
    context.cinema_price = generatorTools.StringBar.LRFindString(result.text, '"filmCinemaPrice":"', '",')[number]
    context.cinema_filmType = generatorTools.StringBar.LRFindString(result.text, '"filmType":"', '",')[number]
    context.cinema_showTime = generatorTools.StringBar.LRFindString(result.text, '"showTime":"', '",')[number]
    context.cinema_showStartTime = generatorTools.StringBar.LRFindString(result.text, '"showStartTime":"', '",')[number]
    context.cinema_showTime = context.cinema_showTime[5:].replace('-','月')+'日 '+ context.cinema_showStartTime

@when('查看影院评价')
def query_cinema_comment(context):
    ParamsObject = launch_request('film_database', 'film', 'query_cinema_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', targetId=context.film_cinemaId,movieName=context.cinemaName)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@when('评价电影院')
def cinema_to_comment(context):
    ParamsObject = launch_request('film_database', 'film', 'cinema_to_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', targetId=context.film_cinemaId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@given('查看动态座位图')
def get_cinema_hall_seat(context):
    ParamsObject = launch_request('film_database', 'film', 'get_cinema_hall_seat')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', hallId=context.film_cinemaId,showId=context.cinema_showId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.cinema_sectionId = generatorTools.StringBar.LRFindString(result.text, '"sectionId":"', '",')[0]
    # 判断座位是否可选
    my_dict = json.loads(result.text)
    mylist = my_dict['result']['seatDetailList']['5']
    for i in mylist:
        if i['canSell'] == True:
            context.cinema_seatNo = i['seatNo']
            break
        else:
            pass

@when('锁定座位')
def cinema_lock_seat(context):
    ParamsObject = launch_request('film_database', 'film', 'cinema_lock_seat')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', cinemaName=context.cinemaName,showId=context.cinema_showId,movieName=context.cinema_filmId,
                       hallName=context.cinema_hallName,price=context.cinema_price,version=context.cinema_filmType,showTime=context.cinema_showTime,
                       sectionId=context.cinema_sectionId,seatNo=context.cinema_seatNo)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.cinema_orderId = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '",')[0]
    time.sleep(1)

@when('查询订单信息')
def query_cinema_order_info(context):
    ParamsObject = launch_request('film_database', 'film', 'query_cinema_order_info')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', orderId=context.cinema_orderId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
    # 获取单个vip会员折扣费
    context.singleVipdiscount = generatorTools.StringBar.LRFindString(result.text, '"singleVipdiscount":"', '",')[0]

@then('购买电影票')
def cinema_order_generate(context):
    ParamsObject = launch_request('film_database', 'film', 'cinema_order_generate')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', movieOrderId=context.cinema_orderId,money=context.cinema_price,movieVipDiscount=context.singleVipdiscount)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)

@then('解锁座位')
def unlock_cinema_seat(context):
    ParamsObject = launch_request('film_database', 'film', 'unlock_cinema_seat')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie,token=context.app_user_login_token,memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', orderId=context.cinema_orderId)
    result = send_request(ParamsObject,context=context)
    assertion_tools(ParamsObject, result, order=0)
