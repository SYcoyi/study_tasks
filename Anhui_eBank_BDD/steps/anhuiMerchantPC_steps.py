#!/usr/bin/env python
# -- coding=utf-8 --
import logging
from behave import then, given

from database.__global_params import MWECHANT_ENV, APP_ENV
from utils import generatorTools
from utils.generatorTools import StringBar
from utils.http_manager import send_request
from utils.common import *
from utils.readTools import launch_request
from utils.tools import push_replaceParams, assertion_tools
import time

gb = generatorTools.RandomBar()


####安徽商户PC端自动化脚本
@given('商户端登陆')
def anhuimerchantpc_login(context):
    time.sleep(0.3)
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Login')
    push_replaceParams(ParamsObject, 'Body', userName=MWECHANT_ENV["username"], password=MWECHANT_ENV["pwd"])
    # push_replaceParams(ParamsObject, 'Body', userName='shengtestm', password='4297f44b13955235245b2497399d7a93')
    result = send_request(ParamsObject, context=context)
    context.userid = generatorTools.StringBar.LRFindString(result.text, '"userId":', ',"userName"')[0]
    context.token = generatorTools.StringBar.LRFindString(result.text, '"token":"', '","userId"')[0]
    context.userName = generatorTools.StringBar.LRFindString(result.text, '"userName":"', '","verify"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiMerchantPC_ProductList_TuanGou')
def anhuimerchantpc_productlist_tuangou(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_ProductList_TuanGou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('AnhuiMerchantPC_ProductList_MingYou')
def anhuimerchantpc_productlist_mingyou(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_ProductList_MingYou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('AnhuiMerchantPC_OrderList_TuanGou')
def anhuimerchantpc_orderlist_tuangou(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_OrderList_TuanGou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('AnhuiMerchantPC_OrderList_MingYou')
def anhuimerchantpc_orderlist_mingyou(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_OrderList_MingYou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.orderId = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '","subOrderId"')[0]
    context.subOrderId = generatorTools.StringBar.LRFindString(result.text, '"subOrderId":"', '","createTime"')[0]
    context.subOrderId = generatorTools.StringBar.LRFindString(result.text, '"type":"', '","orderStatus"')[0]
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('AnhuiMerchantPC_OrderList_CtoB')
def anhuimerchantpc_orderlist_ctob(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_OrderList_CtoB')
    strb = StringBar()
    y = str(strb.getYMD('Y'))
    m = str(strb.getYMD('M'))
    d = str(strb.getYMD('D'))
    now_time = strb.getTimestamp()
    yy = str(strb.getYMD('Y', timestamp=now_time - 7776000))
    mm = str(strb.getYMD('M', timestamp=now_time - 7776000))
    dd = str(strb.getYMD('D', timestamp=now_time - 7776000))
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token, sdt=yy + '-' + mm + '-' + dd,
                       edt=y + '-' + m + '-' + d)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('AnhuiMerchantPC_OrderList_BtoC')
def anhuimerchantpc_orderlist_btoc(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_OrderList_BtoC')
    strb = StringBar()
    y = str(strb.getYMD('Y'))
    m = str(strb.getYMD('M'))
    d = str(strb.getYMD('D'))
    now_time = strb.getTimestamp()
    yy = str(strb.getYMD('Y', timestamp=now_time - 7776000))
    mm = str(strb.getYMD('M', timestamp=now_time - 7776000))
    dd = str(strb.getYMD('D', timestamp=now_time - 7776000))
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token, sdt=yy + '-' + mm + '-' + dd,
                       edt=y + '-' + m + '-' + d)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('AnhuiMerchantPC_OrderList_HuiFu')
def anhuimerchantpc_orderlist_huifu(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_OrderList_HuiFu')
    strb = StringBar()
    y = str(strb.getYMD('Y'))
    m = str(strb.getYMD('M'))
    d = str(strb.getYMD('D'))
    now_time = strb.getTimestamp()
    yy = str(strb.getYMD('Y', timestamp=now_time - 7776000))
    mm = str(strb.getYMD('M', timestamp=now_time - 7776000))
    dd = str(strb.getYMD('D', timestamp=now_time - 7776000))
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token, sdt=yy + '-' + mm + '-' + dd,
                       edt=y + '-' + m + '-' + d)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
    assertion_tools(ParamsObject, result, order=1)


@then('商户端添加团购商品')
def anhuimerchantpc_addproduct_tuangou(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_AddProduct_TuanGou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    context.current_tg = '团购商品' + ran(4)
    push_replaceParams(ParamsObject, 'Body', name=context.current_tg, fullName='团购商品全称' + ran(4), startTime=startTime(),
                       endTime=endTime(), expireEndTime=expireEndTime(), max='0', categoryId=categoryId(),
                       userName=context.userName)
    result = send_request(ParamsObject, context=context)
    context.productId = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '"}]')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠发货')
def anhuimerchantpc_orderlist_ship(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_OrderList_Ship')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', orderId=context.myOrderId, subOrderId=context.myOrderId)
    tryTime = 0
    while tryTime < 10:
        result = send_request(ParamsObject, context=context)
        if '系统错误' in result.text:
            tryTime = tryTime + 1
        else:
            break
    assertion_tools(ParamsObject, result, order=0)


# 交易额统计
@then('AnhuiMerchantPC_Trade_Count')
def anhuimerchantpc_trade_count(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Trade_Count')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', beginTime='1551369600000', endTime='1553851074298', orderStatus='',
                       outletId='', subMerchantId='67FB69428000', tradeChannel='00,01,02,06')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 门店新增
@then('AnhuiMerchantPC_Outlet_Add')
def anhuimerchantpc_outlet_add(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Outlet_Add')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', address='auto地址' + ran(4), areaId='100000017',
                       businessHours='8:00', contactName='联系人姓名' + ran(2), contactPhone='17799991234',
                       discountRate='9.9', latitude='31.863787', longitude='117.315587',
                       outletFullname='auto门店全称' + ran(3), outletName='auto门店简称' + ran(3), phone='14412341234',
                       preferDetails='门店详情' + ran(4))
    result = send_request(ParamsObject, context=context)
    context.merchantIds = generatorTools.StringBar.LRFindString(result.text, '"merchantId":"', '","outletId"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 门店列表查询
@then('AnhuiMerchantPC_Outlet_List')
def anhuimerchantpc_outlet_list(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Outlet_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', auditState='5', outletId='68765FD20000', pageNumber='1', pageSize='10')
    result = send_request(ParamsObject, context=context)
    print("************" + str(result.text))
    context.merchantIds = generatorTools.StringBar.LRFindString(result.text, '"merchantId":"', '","outletId"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 查看门店详情
@then('AnhuiMerchantPC_Outlet_Details')
def anhuimerchantpc_outlet_details(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Outlet_Details')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Params', outletId=outletId(), type='1')
    result = send_request(ParamsObject, context=context)
    context.deliveryCorpIds = generatorTools.StringBar.LRFindString(result.text, '"id":"', '","resourceName"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 门店修改
@then('AnhuiMerchantPC_Outlet_Modify')
def anhuimerchantpc_outlet_add(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Outlet_Add')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Body', outletId='76CD61128000',
                       businessHours='8:00', contactName='联系人姓名' + ran(2), contactPhone='17799991234',
                       discountRate='9.9', latitude='31.863787', longitude='117.315587',
                       outletFullname='auto门店全称' + ran(3), outletName='auto门店简称' + ran(3), phone='14412341234',
                       preferDetails='门店详情' + ran(4))
    result = send_request(ParamsObject, context=context)
    context.merchantIds = generatorTools.StringBar.LRFindString(result.text, '"merchantId":"', '","outletId"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 添加用户
@then('AnhuiMerchantPC_User_Add')
def anhuimerchantpc_user_add(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_User_Add')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Body', outletId='68765FD20000', username='auto' + ran(3),
                       realname='real' + ran(3), phone='18899990000')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 用户列表显示
@then('AnhuiMerchantPC_User_List')
def anhuimerchantpc_user_list(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_User_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Body', outletId='')
    result = send_request(ParamsObject, context=context)
    context.userIds = generatorTools.StringBar.LRFindString(result.text, '"userId":"', '","}"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 修改用户
@then('AnhuiMerchantPC_User_Modify')
def anhuimerchantpc_user_modify(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_User_Modify')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Body', id='100090508', outletId='68765FD20000', username='auto' + ran(2),
                       realname='real' + ran(2), phone='18899990000')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 用户密码重置
@then('AnhuiMerchantPC_User_PwdReset')
def anhuimerchantpc_user_pwdreset(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_User_PwdReset')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Body', mobile='autofU', userId='100090587')
    result = send_request(ParamsObject, context=context)
    context.userIds = generatorTools.StringBar.LRFindString(result.text, '"userId":"', '","}"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 查看用户权限
@then('AnhuiMerchantPC_UserOrigin_List')
def anhuimerchantpc_userorigin_list(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_UserOrigin_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Params', userId='100090560')
    result = send_request(ParamsObject, context=context)
    context.userIds = generatorTools.StringBar.LRFindString(result.text, '"id":"', '","resourceName"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 商品评价列表
@then('商品评价列表')
def anhuimerchantpc_merchandisreview_list(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant',
                                  'AnhuiMerchantPC_MerchandiseReview_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    strb = StringBar()
    y = str(strb.getYMD('Y'))
    m = str(strb.getYMD('M'))
    d = str(strb.getYMD('D'))
    now_time = strb.getTimestamp()
    yy = str(strb.getYMD('Y', timestamp=now_time - 7776000))
    mm = str(strb.getYMD('M', timestamp=now_time - 7776000))
    dd = str(strb.getYMD('D', timestamp=now_time - 7776000))
    push_replaceParams(ParamsObject, 'Body', isReply='-1', pageNumber='1', pageSize='10', starLevel='0',
                       sdt=yy + '-' + mm + '-' + dd, edt=y + '-' + m + '-' + d)
    time.sleep(5)
    result = send_request(ParamsObject, context=context)
    context.commentId = generatorTools.StringBar.LRFindString(result.text, '"commentId":"', '","')[0]
    context.orderId = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '","')[0]
    context.productId = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('商品评价回复')
def anhuimerchantpc_merchandisereview_action(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant',
                                  'AnhuiMerchantPC_MerchandiseReview_Action')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', commentId=context.commentId, productId=context.productId,
                       recomment='你也很棒棒哦~！！！' + str(gb.getRandomBetweenInt(99999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 商品评价
@then('AnhuiMerchantPC_Merchandise_Review')
def anhuimerchantpc_merchant_review(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Merchandise_Review')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info("************", ParamsObject)
    push_replaceParams(ParamsObject, 'Body', commentId='5c7f8771e4b0e5e22b258fe4', productId='75AC31038000',
                       recomment='团购商品全称' + ran(4))
    result = send_request(ParamsObject, context=context)
    context.orderIds = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '","orderType"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 商品评价详情界面
@then('AnhuiMerchantPC_MerchandiseReview_Details')
def anhuimerchantpc_merchandisreview_details(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant',
                                  'AnhuiMerchantPC_MerchandiseReview_Details')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', commentId='5c7f8771e4b0e5e22b258fe4', orderId='75BFA4408000',
                       productId='75AC31038000')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 商户评价列表
@then('AnhuiMerchantPC_MerchantReview_List')
def anhuimerchantpc_merchantreview_list(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_MerchantReview_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    logging.info(ParamsObject)
    push_replaceParams(ParamsObject, 'Body', pageNumber='1', pageSize='10', starLevel='0')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 商户评价界面
@then('AnhuiMerchantPC_Merchant_Review')
def anhuimerchantpc_merchant_review(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Merchant_Review')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', id='764EE1620000', recomment='评价内容' + ran(4))
    result = send_request(ParamsObject, context=context)
    context.ids = generatorTools.StringBar.LRFindString(result.text, '"id":"', '","merchantId"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 商户评价详情界面
@then('AnhuiMerchantPC_MerchantReview_Details')
def anhuimerchantpc_merchantreview_details(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant',
                                  'AnhuiMerchantPC_MerchantReview_Details')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', id='75D711818000')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# 物流评价列表
@then('AnhuiMerchantPC_Delivery_List')
def anhuimerchantpc_delivery_list(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Delivery_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', pageNumber='1', pageSize='10', shippingBegTime='2019-02-25',
                       shippingEndTime='2019-03-27')
    result = send_request(ParamsObject, context=context)
    context.deliveryCorpIds = generatorTools.StringBar.LRFindString(result.text, '"deliveryCorpId":"', '","deliveryCorpName"')[0]
    context.trackinNos = generatorTools.StringBar.LRFindString(result.text, '"trackinNo":"', '","shippingTime"')[0]
    assertion_tools(ParamsObject, result, order=0)


# 物流评价详情界面
@then('AnhuiMerchantPC_Delivery_Details')
def anhuimerchantpc_delivery_details(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Delivery_Details')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Params', deliveryCorpId='100000004', trackinNo='805152811294630424')
    result = send_request(ParamsObject, context=context)
    context.shippingNos = generatorTools.StringBar.LRFindString(result.text, '"shippingNo":"', '","status"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiMerchantPC_LogOut')
def anhuimerchantpc_logout(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_LogOut')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('提货码列表查询')
def anhuimerchantpc_orderqcl(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_orderqcl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    strb = StringBar()
    y = str(strb.getYMD('Y'))
    m = str(strb.getYMD('M'))
    d = str(strb.getYMD('D'))
    now_time = strb.getTimestamp()
    yy = str(strb.getYMD('Y', timestamp=now_time - 7776000))
    mm = str(strb.getYMD('M', timestamp=now_time - 7776000))
    dd = str(strb.getYMD('D', timestamp=now_time - 7776000))
    push_replaceParams(ParamsObject, 'Body', sdt=yy + '-' + mm + '-' + dd, edt=y + '-' + m + '-' + d)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购提货')
def anhuimerchantpc_seall(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_seall')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    push_replaceParams(ParamsObject, 'Body', ticketId=context.ticketId, productIds=APP_ENV["productId"],
                       memberCode=context.app_user_memberCode, subOrderId=context.orderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('创建二维码订单')
def anhuimerchantpc_order_create_code(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Order_Create_Code')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', money=str(gb.getRandomBetweenInt(1, 6)))
    result = send_request(ParamsObject, context=context)
    context.qrcode = generatorTools.StringBar.LRFindString(result.text, '"qrcode":"', '"')[0]
    context.productId = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('商户PC端创建商品')
def anhuimerchantpc_product_add(context):
    ParamsObject = launch_request('anhuiMerchantPC', 'INTERFACE_PARAMS_Merchant', 'AnhuiMerchantPC_Product_Add')
    push_replaceParams(ParamsObject, 'Header', userId=context.userid, token=context.token)
    context.tuangou_name = '测试团购商品' + str(gb.getRandomBetweenInt(99999))
    push_replaceParams(ParamsObject, 'Body', name=context.tuangou_name,
                       fullName='测试团购全称' + str(gb.getRandomBetweenInt(99999)), startTime='', endTime='')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
