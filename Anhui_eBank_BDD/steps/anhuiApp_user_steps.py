#!/usr/bin/env python
# -- coding=utf-8 --

import logging
from behave import given, when, then

from database.__global_params import APP_ENV, DATABASE_ENV
from utils.http_manager import send_request
from utils.common import *
from utils.readTools import launch_request
from utils.tools import push_replaceParams, assertion_tools
import utils.generatorTools as generatorTools
from utils.dbUtil import SingletonModel


@when('手机个人端登录获取验证码')
def anhuiuserapp_user_getcode(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_user_getcode')
    push_replaceParams(ParamsObject, 'Header', Cookie='', memberCode='')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.app_user_smsToken = generatorTools.StringBar.LRFindString(result.text, '"smsToken":"', '",')[0]


@then('手机个人端登录')
def anhuiuserapp_user_login(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_user_login')
    select_sql = "select * from cb_sms_log where mobile = '" + ParamsObject['Body'][
        'mobile'] + "' and is_used = '0'  ORDER BY `create_time` DESC LIMIT 1;"
    db = SingletonModel(host=DATABASE_ENV["host"], port=DATABASE_ENV["port"], user=DATABASE_ENV["user"],
                        passwd=DATABASE_ENV["pwd"], db=DATABASE_ENV["db"])
    sms_verification = db.sqlFetchone(sql=select_sql)[0]['code']
    push_replaceParams(ParamsObject, 'Header', Cookie='', memberCode='')
    push_replaceParams(ParamsObject, 'Body', smsToken=context.app_user_smsToken, loginTime=startTime(),
                       code=sms_verification)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.app_user_JSESSIONID = generatorTools.StringBar.LRFindString(result.headers, 'JSESSIONID=', ';')[0]
    context.app_user_login_token = generatorTools.StringBar.LRFindString(result.headers, 'u_login_token=', ';')[0]
    context.app_user_memberCode = generatorTools.StringBar.LRFindString(result.text, '"memberCode":', ',')[0]
    context.app_user_Cookie = 'loginId=' + APP_ENV[
        'loginId'] + '; u_login_token=' + context.app_user_login_token + '; memberCode=' + context.app_user_memberCode + ';areaId=100000001; cityCode=; cityName=%E5%90%88%E8%82%A5%E5%B8%82; parentCityCode=127'


@when('手机个人端密码登录')
def anhuiuserapp_user_login_passwork(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_user_login_passwork')
    push_replaceParams(ParamsObject, 'Header', Cookie='')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@when('点击忘记密码')
def anhuiuserapp_update_login_passwork(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_update_login_passwork')
    push_replaceParams(ParamsObject, 'Header', Cookie='')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    # 获取图片返回token
    context.app_user_imgToken = generatorTools.StringBar.LRFindString(result.text, '"imgToken":"', '",')[0]


@when('首次点击找回登陆密码')
def anhuiuserapp_one_update_passwork(context):
    mobile = APP_ENV["loginId"]
    # 需要找回密码的手机号
    context.app_mobile = mobile
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_one_update_passwork')
    push_replaceParams(ParamsObject, 'Header', Cookie='')
    updatepassword_one_select_spl = " SELECT s.code FROM cb_sms_log s ORDER BY id desc limit 1;"
    update_password = SingletonModel()
    img_code_one = update_password.sqlFetchone(sql=updatepassword_one_select_spl)[0]['code']
    print("-------code-------:%s" % img_code_one)
    push_replaceParams(ParamsObject, 'Body', imgCode=img_code_one, imgToken=context.app_user_imgToken,
                       mobile=context.app_mobile)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@when('首次点击找回登陆密码，更新页面及图片验证码')
def anhuiuserapp_oneimg_update_passwork(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_oneimg_update_passwork')
    push_replaceParams(ParamsObject, 'Header', mobile_a=context.app_mobile, mobile_b=context.app_mobile,
                       mobile_c=context.app_mobile)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    context.app_user_imgToken_2 = generatorTools.StringBar.LRFindString(result.text, '"imgToken":"', '",')[0]


@when('找回登陆密码页面获取短信验证码')
def anhuiuserapp_oneimg_update_passwork(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhuiuserapp_oneimg_update_passwork')
    push_replaceParams(ParamsObject, 'Header', mobile_a=context.app_mobile, mobile_b=context.app_mobile,
                       mobile_c=context.app_mobile)
    updatepassword_two_select_spl = " SELECT s.code FROM cb_sms_log s ORDER BY id desc limit 1;"
    update_password = SingletonModel()
    img_code_two = update_password.sqlFetchone(sql=updatepassword_two_select_spl)[0]['code']
    push_replaceParams(ParamsObject, 'Body', img_Code=img_code_two, img_Token=context.app_user_imgToken_2,
                       mobile_d=context.app_mobile)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端首页
@then('AnhuiUserApp_User_Index')
def anhuiuserapp_user_index(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_Index')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    result = send_request(ParamsObject, context=context)
    print("qqqqqqqqqqqqqq&&&&&&&&&&&&%s" % ParamsObject)
    assertion_tools(ParamsObject, result, order=0)


# 个人端订单列表
@then('AnhuiUserApp_User_OrderTop')
def anhuiuserapp_user_ordertop(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_OrderTop')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端特惠商户列表
@then('AnhuiUserApp_User_MerchantList')
def anhuiuserapp_user_merchantlist(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_MerchantList')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端名优特惠商品列表
@then('AnhuiUserApp_User_MingyouList')
def anhuiuserapp_user_mingyoulist(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_MingyouList')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端预售商品列表
@then('AnhuiUserApp_User_YushouList')
def anhuiuserapp_user_yushoulist(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_YushouList')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端积分兑换商品列表
@then('AnhuiUserApp_User_PointProductList')
def anhuiuserapp_user_pointproductlist(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_PointProductList')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端商户详情
@then('AnhuiUserApp_User_MerchantDetail')
def anhuiuserapp_user_merchantdetail(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_MerchantDetail')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端团购商品详情
@then('AnhuiUserApp_User_TuangouDetail')
def anhuiuserapp_user_tuangoudetail(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_TuangouDetail')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端首页商户搜索
@then('AnhuiUserApp_User_MerchantSearch')
def anhuiuserapp_user_merchantsearch(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_MerchantSearch')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 个人端首页商品搜索
@then('AnhuiUserApp_User_ProductSearch')
def anhuiuserapp_user_ProductSearch(context):
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_ProductSearch')
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Params')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiUserApp_User_LogOut')
def anhuiuserapp_user_logout(context):
    """
        退出登陆
    """
    ParamsObject = launch_request('anhuiUserApp', 'INTERFACE_PARAMS_User', 'AnhuiUserApp_User_LogOut')
    logging.info("**************%s" % ParamsObject)
    push_replaceParams(ParamsObject, 'Header', token=context.token)
    push_replaceParams(ParamsObject, 'Body')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('生成团购商品')
def anhui_app_tuangou_order_gen(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_gen')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject, context=context)
    # 运行时添加 orderID
    context.orderId = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('app团购退款')
def anhui_app_tuangou_refund_do(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_refund_do')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', subOrderId=context.orderId)
    result = send_request(ParamsObject, context=context)
    k = 0
    while (k > 5):
        if ('4012' in result.text) or ('4001' in result.text):
            time.sleep(2)
            k = k + 1
            result = send_request(ParamsObject, context=context)
        else:
            break
    assertion_tools(ParamsObject, result, order=0)


@then('团购支付')
def anhui_app_tuangou_order_pay(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_pay')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', orderId=context.orderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('获取团购码')
def anhui_app_tuangou_ticketlist(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_ticketList')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Params', orderId=context.orderId)
    result = send_request(ParamsObject, context=context)
    # 运行时添加 ticketId
    tryTimes = 0
    context.ticketId = None
    while tryTimes < 5 and context.ticketId == None:
        try:
            context.ticketId = generatorTools.StringBar.LRFindString(result.text, '"ticketId":"', '","')[0]
        except:
            tryTimes = tryTimes + 1
            time.sleep(1)
    assertion_tools(ParamsObject, result, order=0)


@then('二维码现金支付')
def anhui_app_tuangou_order_pay(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_qr_pay')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body',
                       ciphertextPwd='05FA3F921950980D9F5D4B780D54686C67CE98C2BC8011B50097F97A5764950E40AA47770D11323FBE58A7EEC1FF4A720BB40E3765C43A00F617DA5B61AA31857DCD36D3F36704D1825605285CC643D4BEB5A32939C5B924BFFCE8EDDD08C59C44B6C891942C444E9B5180431390F23CB9F9092A4C9870A4A5C7F7FDF2DAACC7',
                       qrCode=context.qrcode)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购客户评价')
def anhui_app_tuangou_add_comment(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_add_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', productId=APP_ENV["productId"], orderId=context.orderId,
                       bigOrderId=context.orderId, comment='太棒了~！！！！' + str(gb.getRandomBetweenInt(99999)),
                       starLevel=str(gb.getRandomBetweenInt(1, stop=6)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠客户评价')
def anhui_app_tuangou_add_comment(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_add_my_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', productId=APP_ENV["myProductId"], orderId=context.myOrderId,
                       bigOrderId=context.myOrderId, starLevel=str(gb.getRandomBetweenInt(1, stop=6)),
                       comment='太棒了~！简直跟不要钱一样~！' + str(gb.getRandomBetweenInt(99999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('生成名优特惠订单')
def anhui_app_tuangou_order_my_gen(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_my_gen')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    result = send_request(ParamsObject, context=context)
    # 运行时添加 myOrderID 名优特惠订单ID
    context.myOrderId = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠支付')
def anhui_app_tuangou_order_pay(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_pay')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', orderId=context.myOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分商品支付')
def anhui_app_tuangou_order_points_pay(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_points_pay')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', productId=APP_ENV["pointsProductsId"])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠确认收货')
def anhui_app_tuangou_order_receipt(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_receipt')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    push_replaceParams(ParamsObject, 'Body', orderId=context.myOrderId, subOrderId=context.myOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠物流评价')
def anhui_app_tuangou_order_shipping_comment(context):
    ParamsObject = launch_request('anhuiApp_user', 'Header_App_user', 'anhui_app_tuangou_order_shipping_comment')
    push_replaceParams(ParamsObject, 'Header', Cookie=context.app_user_Cookie, memberCode=context.app_user_memberCode)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', subOrderId=context.myOrderId, orderId=context.myOrderId,
                       starLevel=str(gb.getRandomBetweenInt(1, 6)),
                       commentDescription=str(gb.getRandomBetweenInt(99999)),
                       starLevelOne=str(gb.getRandomBetweenInt(1, 6)), starLevelTwo=str(gb.getRandomBetweenInt(1, 6)),
                       starLevelThree=str(gb.getRandomBetweenInt(1, 6)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
