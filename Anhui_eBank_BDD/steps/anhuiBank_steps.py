#!/usr/bin/env python
# -- coding=utf-8 --

import logging
import math

from behave import when, then

from database.__global_params import DATABASE_ENV
from utils import generatorTools
from utils.dbUtil import SingletonModel
from utils.generatorTools import RandomBar, StringBar
from utils.http_manager import send_request
from utils.common import *
from utils.readTools import launch_request
from utils.tools import push_replaceParams, assertion_tools

gb = generatorTools.RandomBar()
strb = StringBar()


@when('获取图片验证码')
def anhuibank_login_getgic(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Login_getGic')
    result = send_request(ParamsObject, context=context)
    context.preToken = generatorTools.StringBar.LRFindString(result.text, '"token":"', '","codeUrl')[0]
    select_sql = "SELECT `code`FROM `cb_sms_log` WHERE mobile is null ORDER BY `create_time` DESC LIMIT 1"
    db = SingletonModel(host=DATABASE_ENV["host"], port=DATABASE_ENV["port"], user=DATABASE_ENV["user"],
                        passwd=DATABASE_ENV["pwd"], db=DATABASE_ENV["db"])
    context.code = db.sqlFetchone(sql=select_sql)[0]['code']
    assertion_tools(ParamsObject, result, order=0)


@then('银行端法人登陆')
def anhuibank_login_faren(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Login_FaRen')
    push_replaceParams(ParamsObject, 'Header', )
    push_replaceParams(ParamsObject, 'Body', code=context.code, token=context.preToken)
    result = send_request(ParamsObject, context=context)
    context.userId = generatorTools.StringBar.LRFindString(result.text, '"userId":', ',"code"')[0]
    context.token = generatorTools.StringBar.LRFindString(result.text, '"token":"', '","tag"')[0]
    context.orgCode = generatorTools.StringBar.LRFindString(result.text, '"orgCode":"', '","userId"')[0]
    context.loginName = generatorTools.StringBar.LRFindString(result.text, '"loginName":"', '","orgLevel"')[0]
    context.orgLevel = generatorTools.StringBar.LRFindString(result.text, '"orgLevel":"', '"}')[0]
    context.proOrgCode = generatorTools.StringBar.LRFindString(result.text, '{"proOrgCode":"', '","resourceList"')[0]
    context.orgName = generatorTools.StringBar.LRFindString(result.text, '"orgName":"', '","isReset"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('银行端省联社登录')
def anhuibank_login_shenglianshe(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Login_ShengLianShe')
    push_replaceParams(ParamsObject, 'Header', )
    push_replaceParams(ParamsObject, 'Body', code=context.code, token=context.preToken)
    result = send_request(ParamsObject, context=context)
    context.userId = generatorTools.StringBar.LRFindString(result.text, '"userId":', ',"code"')[0]
    context.token = generatorTools.StringBar.LRFindString(result.text, '"token":"', '","tag"')[0]
    context.orgCode = generatorTools.StringBar.LRFindString(result.text, '"orgCode":"', '","userId"')[0]
    context.loginName = generatorTools.StringBar.LRFindString(result.text, '"loginName":"', '","orgLevel"')[0]
    context.orgLevel = generatorTools.StringBar.LRFindString(result.text, '"orgLevel":"', '"}')[0]
    context.proOrgCode = generatorTools.StringBar.LRFindString(result.text, '{"proOrgCode":"', '","resourceList"')[0]
    context.orgName = generatorTools.StringBar.LRFindString(result.text, '"orgName":"', '","isReset"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_AddProduct_MingYou')
def anhuibank_addproduct_mingyou(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_AddProduct_MingYou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productName=ran(4) + '限时特价名优', productFullName='名限时特价名优全称' + ran(8),
                       startDate=str(int(round(time.time() * 1000))),
                       endDate=str(int(round(time.time() * 1000 + 2592000000))))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_AddProduct_YuShou')
def anhuibank_addproduct_yushou(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_AddProduct_YuShou')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productName=ran(4) + '限时特价预售', productFullName='限时特价预售全称' + ran(8),
                       startDate=str(int(round(time.time() * 1000))),
                       endDate=str(int(round(time.time() * 1000 + 2592000000))),
                       takeStartDate=str(int(round(time.time() * 1000 + 2692000000))),
                       takeEndDate=str(int(round(time.time() * 1000 + 2792000000))), storeNum='1000',
                       memberlimitNum='10')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_MingYou_Detail')
def anhuibank_pendaudit_mingyou_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_MingYou_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.productIDs.split(';')[0],
                       auditNumber=context.auditNumbers.split(';')[0], typeDetail=context.typeDetails.split(';')[0])
    result = send_request(ParamsObject, context=context)
    context.taskIds = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '","createTime"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_MingYou_Audit_Step1')
def anhuibank_pendaudit_mingyou_audit_step1(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_MingYou_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.productIDs.split(';')[0], auditState='1',
                       instanceId=context.auditNumbers.split(';')[0], taskId=context.taskIds.split(';')[0])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_MingYou_Audit_Step2')
def anhuibank_pendaudit_mingyou_audit_step2(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_MingYou_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.productIDs.split(';')[0], auditState='1',
                       instanceId=context.auditNumbers.split(';')[0], taskId=context.taskIds.split(';')[1])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_YuShou_List')
def anhuibank_pendaudit_yushou_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_YuShou_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', myOrgCode=context.orgCode, orgCode=context.orgCode)
    result = send_request(ParamsObject, context=context)
    context.auditNumbers = generatorTools.StringBar.LRFindString(result.text, '"auditNumber":"', '","productName"')[0]
    context.productIDs = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '","merchantId"')[0]
    context.typeDetails = generatorTools.StringBar.LRFindString(result.text, '"typeDetail":"', '","type"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_YuShou_Detail')
def anhuibank_pendaudit_yushou_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_YuShou_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.productIDs.split(';')[0],
                       auditNumber=context.auditNumbers.split(';')[0], typeDetail=context.typeDetails.split(';')[0])
    result = send_request(ParamsObject, context=context)
    context.taskIds = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '","createTime"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_YuShou_Audit_Step1')
def anhuibank_pendaudit_yushou_audit_step1(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_YuShou_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.productIDs.split(';')[0], auditState='1',
                       instanceId=context.auditNumbers.split(';')[0], taskId=context.taskIds.split(';')[0])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_YuShou_Audit_Step2')
def anhuibank_pendaudit_yushou_audit_step2(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_YuShou_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.productIDs.split(';')[0], auditState='1',
                       instanceId=context.auditNumbers.split(';')[0], taskId=context.taskIds.split(';')[1])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_TuanGou_List')
def anhuibank_pendaudit_tuangou_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_TuanGou_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', orgCode=context.orgCode)
    result = send_request(ParamsObject, context=context)
    context.auditIds = generatorTools.StringBar.LRFindString(result.text, '"auditId":"', '","taskId"')[0]
    context.productIDs = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '","merchantName"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_TuanGou_Detail')
def anhuibank_pendaudit_tuangou_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_TuanGou_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.productIDs.split(';')[0],
                       auditNumber=context.auditIds.split(';')[0])
    result = send_request(ParamsObject, context=context)
    context.taskIds = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '","createTime"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_TuanGou_Audit_Step1')
def anhuibank_pendaudit_tuangou_audit_step1(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_TuanGou_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.productIDs.split(';')[0], auditState='1',
                       instanceId=context.auditIds.split(';')[0], taskId=context.taskIds.split(';')[0])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('AnhuiBank_PendAudit_TuanGou_Audit_Step2')
def anhuibank_pendaudit_tuangou_audit_step2(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_TuanGou_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.productIDs.split(';')[0], auditState='1',
                       instanceId=context.auditIds.split(';')[0], taskId=context.taskIds.split(';')[1])
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端退出登录')
def anhuibank_logout(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Logout')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核商户列表')
def anhuibank_merchant_approvallt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Approvallt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核品牌列表')
def anhuibank_merchant_brand(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_brand')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.brandId = generatorTools.StringBar.LRFindString(result.text, 'brandId":"', '","')[0]
    context.auditNumber = generatorTools.StringBar.LRFindString(result.text, 'auditNumber":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核品牌列表-名称查询')
def anhuibank_merchant_brand_check(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_brand_check')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', brandName=context.current_brand_name)
    result = send_request(ParamsObject, context=context)
    context.brandId = generatorTools.StringBar.LRFindString(result.text, 'brandId":"', '","')[0]
    context.auditNumber = generatorTools.StringBar.LRFindString(result.text, 'auditNumber":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核品牌列表-名称查询-省联社查询')
def anhuibank_merchant_brand_check_sls(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_brand_check_sls')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', brandName=context.current_brand_name)
    result = send_request(ParamsObject, context=context)
    context.brandId = generatorTools.StringBar.LRFindString(result.text, 'brandId":"', '","')[0]
    context.auditNumber = generatorTools.StringBar.LRFindString(result.text, 'auditNumber":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('商户分类')
def anhuibank_merchant_gmc(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Gmc')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核团购列表')
def anhuibank_merchant_auditlt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_AuditLt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    pd_name = ''
    if getAttr(context, 'current_tg') != None:
        pd_name = context.current_tg
    push_replaceParams(ParamsObject, 'Body', productName=pd_name)
    result = send_request(ParamsObject, context=context)
    context.tg_auditId = generatorTools.StringBar.LRFindString(result.text, 'auditId":"', '"')[0]
    context.tg_productId = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[0]
    context.tg_taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核团购详情')
def anhuibank_pendaudit_tuangou_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_TuanGou_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.tg_productId, auditNumber=context.tg_auditId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购审核')
def anhuibank_merchant_groupproduct_tg_audit(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_tg_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.tg_productId, taskId=context.tg_taskId,
                       instanceId=context.tg_auditId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购列表详情')
def anhuibank_order_godl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Order_Godl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.tg_subOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核线下礼品列表')
def anhuibank_merchant_offline(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Offline')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.jf_auditNumber = generatorTools.StringBar.LRFindString(result.text, '"auditNumber":"', '"')[0]
    context.jf_productId = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品审核详情')
def anhuibank_merchant_pendauit_offlinedetail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PendAuit_OfflineDetail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.jf_productId, auditNumber=context.jf_auditNumber)
    result = send_request(ParamsObject, context=context)
    context.jf_taskId = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '"')[-1]
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品审核')
def anhuibank_merchant_groupproduct_audit_jf(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_Audit_jf')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.jf_productId, taskId=context.jf_taskId,
                       instanceId=context.jf_auditNumber)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品下架')
def anhuibank_merchant_lineproduct_it(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_LineProduct_IT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productIdList=context.jf_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品删除')
def anhuibank_merchant_lineproduct_de(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_LineProduct_DE')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productIdList=context.jf_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品上架')
def anhuibank_merchant_lineproduct_it_up(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_LineProduct_IT_up')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productIdList=context.jf_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核名优特惠列表')
def anhuibank_merchant_special(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Special')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    pd_name = ''
    if getAttr(context, 'current_my_name') != None:
        pd_name = context.current_my_name
    logging.info(pd_name)
    push_replaceParams(ParamsObject, 'Body', productName=pd_name, userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.my_auditNumber = generatorTools.StringBar.LRFindString(result.text, '"auditNumber":"', '"')[0]
    context.my_productId = generatorTools.StringBar.LRFindString(result.text, '"productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核名优特惠详情')
def anhuibank_pendaudit_mingyou_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_MingYou_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.my_productId, typeDetail=0,
                       auditNumber=context.my_auditNumber)
    result = send_request(ParamsObject, context=context)
    if getAttr(context, 'my_taskId') != None:
        if context.my_taskId == generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '"')[-1]:
            context.my_taskId = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '"')[0]
        else:
            context.my_taskId = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '"')[-1]
    else:
        context.my_taskId = generatorTools.StringBar.LRFindString(result.text, '"taskId":"', '"')[-1]
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠审核')
def anhuibank_merchant_groupproduct_my_audit(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_my_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.my_productId, taskId=context.my_taskId,
                       instanceId=context.my_auditNumber)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售商品新增')
def anhuibank_merchant_presaleproduct_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    context.current_jp_name = '测试商品名称' + str(gb.getRandomBetweenInt(999999))
    push_replaceParams(ParamsObject, 'Body', productName=context.current_jp_name,
                       productFullName=str(gb.getRandomBetweenInt(999999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售商品修改')
def anhuibank_merchant_presaleproduct_ue(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_UE')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.jp_productId, productFullName=context.current_jp_name,
                       productName=context.current_jp_name)
    result = send_request(ParamsObject, context=context)
    k = 0
    while (k < 5):
        if '9999' in result.text:
            time.sleep(2)
            k = k + 1
            result = send_request(ParamsObject, context=context)
        else:
            break
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售商品下架')
def anhuibank_merchant_presaleproduct_it(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_IT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.jp_productId, isMarketable=2)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售商品上架')
def anhuibank_merchant_presaleproduct_it(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_IT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.jp_productId, isMarketable=1)
    result = send_request(ParamsObject, context=context)
    k = 0
    while (k < 5):
        if '9999' in result.text:
            k = k + 1
            time.sleep()
            result = send_request(ParamsObject, context=context)
        else:
            break
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售商品删除')
def anhuibank_merchant_presaleproduct_de(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_DE')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.jp_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售商品详情')
def anhuibank_merchant_presaleproduct_dl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_DL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.jp_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核预售列表')
def anhuibank_merchant_presell(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Presell')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    jp_name = getAttr(context, 'current_jp_name', defaultStr='')
    push_replaceParams(ParamsObject, 'Body', productName=jp_name)
    result = send_request(ParamsObject, context=context)
    context.jp_auditNumber = generatorTools.StringBar.LRFindString(result.text, 'auditNumber":"', '"')[0]
    context.jp_productId = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核限时特价活动列表')
def anhuibank_merchant_ac_approvallt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_AC_Approvallt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('审核监控列表')
def anhuibank_merchant_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.sh_auditId = generatorTools.StringBar.LRFindString(result.text, 'auditId":"', '"')[0]
    context.sh_productId = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('审核监控详情')
def anhuibank_merchant_pendauit_specialdetail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PendAuit_SpecialDetail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.sh_productId, auditNumber=context.sh_auditId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('综合查询列表')
def anhuibank_merchant_composite(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Composite')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.zh_auditId = generatorTools.StringBar.LRFindString(result.text, 'auditId":"', '"')[0]
    context.zh_merchantId = generatorTools.StringBar.LRFindString(result.text, 'merchantId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('综合查询详情')
def anhuibank_merchant_editdl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Editdl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', merchantId=context.zh_merchantId, auditId=context.zh_auditId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品列表')
def anhuibank_merchant_plt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PLT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.jf_productId = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品详情')
def anhuibank_bank_lineproduct_dl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_LineProduct_DL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.jf_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品新增')
def anhuibank_bank_lineproduct_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_LineProduct_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    context.current_jf_name = '积分测试' + str(gb.getRandomBetweenInt(99999))

    push_replaceParams(ParamsObject, 'Body', productName=context.current_jf_name,
                       startDate=math.ceil(strb.getTimestamp()) + 86400,
                       endDate=math.ceil(strb.getTimestamp()) + (86400 * 2))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分礼品图片上传探测')
def anhuibank_bank_img_token(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_IMG_token')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购订单列表')
def anhuibank_merchant_plt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Golt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.tg_subOrderId = generatorTools.StringBar.LRFindString(result.text, 'subOrderId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('预售订单列表')
def anhuibank_merchant_plt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Polt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.ys_subOrderId = generatorTools.StringBar.LRFindString(result.text, 'subOrderId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('预售订单限时特价详情')
def anhuibank_merchant_order_sdl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Order_Sdl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.ys_subOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('预售订单详情')
def anhuibank_merchant_order_podl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Order_Podl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.ys_subOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('面对面订单列表')
def anhuibank_merchant_plt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Colt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.mdm_orderId = generatorTools.StringBar.LRFindString(result.text, 'orderId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('面对面订单详情')
def anhuibank_merchant_codl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Codl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.mdm_orderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠订单列表')
def anhuibank_merchant_fpolt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Fpolt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.my_subOrderId = generatorTools.StringBar.LRFindString(result.text, 'subOrderId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠订单详情')
def anhuibank_bank_order_fpdl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Order_Fpdl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.my_subOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠订单限时特价详情')
def anhuibank_bank_saleproduct_sdl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_SaleProduct_SDL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.my_subOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分兑换订单列表')
def anhuibank_merchant_ceolt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Ceolt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.jf_subOrderId = generatorTools.StringBar.LRFindString(result.text, 'subOrderId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('积分兑换订单详情')
def anhuibank_bank_order_cedl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Order_Cedl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.jf_subOrderId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分报表中购物订单明细')
def anhuibank_bank_point_shoppingtotal(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Point_ShoppingTotal')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分报表银行积分总计')
def anhuibank_bank_point_ftftotal(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Point_FtfTotal')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分报表商户总和')
def anhuibank_bank_point_merchanttotal(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Point_MerchantTotal')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('精品商城订单列表')
def anhuibank_merchant_bsol(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Bsol')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('积分报表列表')
def anhuibank_merchant_total(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Total')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('异常订单管理列表')
def anhuibank_merchant_ex_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Ex_Lt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.yc_paymentId = generatorTools.StringBar.LRFindString(result.text, '"paymentId":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('结算查询列表')
def anhuibank_merchant_ex_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Settlement_Lt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.settlementId = generatorTools.StringBar.LRFindString(result.text, '"orderId":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('结算查询详情')
def anhuibank_merchant_codl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Codl')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', subOrderId=context.settlementId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('支付查询列表')
def anhuibank_merchant_paylist(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PayList')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('退款查询列表')
def anhuibank_merchant_ex_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Refund_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.settlementId = generatorTools.StringBar.LRFindString(result.text, '"refundId":"', '","')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('退款查询详情')
def anhuibank_merchant_refund_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Refund_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', settlementId=context.settlementId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('预售账单查询')
def anhuibank_merchant_presellorder_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Presellorder_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('账单查询')
def anhuibank_merchant_bill_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Bill_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('退款审核')
def anhuibank_merchant_bosspayment_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_BossPayment_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body',
                       beginTime=str(strb.getYMD('Y')) + '-' + str(strb.getYMD('M')) + '-' + str(strb.getYMD('D')),
                       endTime=str(strb.getYMD('Y')) + '-' + str(strb.getYMD('M')) + '-' + str(strb.getYMD('D')))
    result = send_request(ParamsObject, context=context)
    context.tk_billNo = generatorTools.StringBar.LRFindString(result.text, '"billNo":"', '"')[0]
    context.tk_refundNo = generatorTools.StringBar.LRFindString(result.text, '"refundNo":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('银行端退款详情')
def anhuibank_merchant_refund_bossPayment_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_refund_bossPayment_detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', refundNo=context.tk_refundNo, billNo=context.tk_billNo)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端批量退款初审')
def anhuibank_merchant_refund_bosspayment_auditonce(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank',
                                  'AnhuiBank_Merchant_refund_bossPayment_auditOnce')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', refundNo=context.tk_refundNo)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端批量退款复审')
def anhuibank_merchant_refund_bosspayment_audittwice(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank',
                                  'AnhuiBank_Merchant_refund_bossPayment_auditTwice')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', refundNo=context.tk_refundNo)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户管理列表')
def anhuibank_merchant_merchant_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_Lt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.merchantId = generatorTools.StringBar.LRFindString(result.text, '"merchantId":"', '","')[0]
    context.merchantUserId = generatorTools.StringBar.LRFindString(result.text, '"merchantUserId":', ',"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('商户详情')
def anhuibank_merchant_merchant_dt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_Dt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', merchantId=context.merchantId, merchantUserId=context.merchantUserId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户新增所属分类查询')
def anhuibank_merchant_merchant_gmc(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_Gmc')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户新增之商户类型')
def anhuibank_merchant_merchant_gmt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_Gmt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('附加功能列表')
def anhuibank_merchant_bankorg_gof(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_BankOrg_Gof')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户新增之所属机构')
def anhuibank_merchant_bankorg_bs(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_BankOrg_BS')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户信息')
def anhuibank_merchant_bankorg_bs(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_BankOrg_BS')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户新增之地址')
def anhuibank_merchant_bankorg_sa(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_BankOrg_SA')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('新增商户')
def anhuibank_merchant_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    merchant_num = str(gb.getRandomBetweenInt(99999))
    push_replaceParams(ParamsObject, 'Body', merchantName='接口测试商户' + merchant_num,
                       license='interfacelicese' + str(gb.getRandomBetweenInt(999999)),
                       legalCredentNo=RandomBar.getRandomId(),
                       acctNumber='6217788300130' + str(gb.getRandomBetweenInt(100000, stop=999999)),
                       loginName='interface' + str(gb.getRandomBetweenInt(9999)))
    context.current_merchant_name = '接口测试商户' + merchant_num
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('门店管理列表')
def anhuibank_merchant_outlet_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Outlet_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户聊天记录列表')
def anhuibank_merchant_merchantchat_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_MerchantChat_Lt')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户星级管理列表')
def anhuibank_merchant_merchantcomment_starlevelreport(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank',
                                  'AnhuiBank_Merchant_MerchantComment_StarLevelReport')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商品星级管理列表')
def anhuibank_merchant_productcomment_starlevelreport(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank',
                                  'AnhuiBank_Merchant_ProductComment_StarLevelReport')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('物流评价列表')
def anhuibank_merchant_shipping_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Shipping_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行商户评价列表')
def anhuibank_merchant_merchantcomment_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_MerchantComment_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行商品评价列表')
def anhuibank_merchant_productcomment_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_ProductComment_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('点赞汇总统计列表')
def anhuibank_merchant_praise_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Praise_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('预售商品列表')
def anhuibank_merchant_presaleproduct_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PresaleProduct_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productName=getAttr(context, 'current_jp_name', defaultStr=''))
    result = send_request(ParamsObject, context=context)
    context.jp_productId = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[-1]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核精品预售详情')
def anhuibank_pendaudit_yushou_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_PendAudit_YuShou_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.jp_productId, typeDetail=0,
                       auditNumber=context.jp_auditNumber)
    result = send_request(ParamsObject, context=context)
    if getAttr(context, 'jp_taskId') != None:
        if context.jp_taskId == generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[-1]:
            context.jp_taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[0]
        else:
            context.jp_taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[-1]
    else:
        context.jp_taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[-1]
    assertion_tools(ParamsObject, result, order=0)


@then('精品预售审核')
def anhuibank_merchant_groupproduct_jp_audit(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_jp_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.jp_productId, taskId=context.jp_taskId,
                       instanceId=context.jp_auditNumber)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('提货查询列表')
def anhuibank_merchant_take_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Take_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('提货查询列表导出')
def anhuibank_merchant_take_et(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Take_ET')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', token=context.token, userId=context.userId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购商品信息列表')
def anhuibank_merchant_groupproduct_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    context.check_tg_productId = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[0]
    if generatorTools.StringBar.LRFindString(result.text, 'isMarketableName":"', '"')[0] == '已上架':
        context.tg_marketable = 0
    else:
        context.tg_marketable = 1
    assertion_tools(ParamsObject, result, order=0)


@then('团购商品信息详情')
def anhuibank_merchant_groupproduct_dl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_DL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.check_tg_productId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('团购商品信息上下架')
def anhuibank_merchant_groupproduct_it(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_IT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.check_tg_productId, isMarketable=context.tg_marketable)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('线下券码导入之获取商品信息')
def anhuibank_merchant_groupproduct_supplierinput(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_SupplierInput')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', token=context.token, userId=context.userId)
    push_replaceParams(ParamsObject, 'Body', token=context.token, userId=context.userId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品列表')
def anhuibank_merchant_preferentialproduct_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productName=getAttr(context, 'current_my_name', ''))
    result = send_request(ParamsObject, context=context)
    context.current_my_product_id = generatorTools.StringBar.LRFindString(result.text, 'productId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品修改')
def anhuibank_merchant_preferentialproduct_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.current_my_product_id,
                       productName=context.current_my_name, productFullName=context.current_my_name)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品详情')
def anhuibank_merchant_preferentialproduct_dl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_DL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.current_my_product_id)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品删除')
def anhuibank_merchant_preferentialproduct_de(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_DE')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', productId=context.current_my_product_id)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品上架')
def anhuibank_merchant_preferentialproduct_it(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_IT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.current_my_product_id, isMarketable=1)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品下架')
def anhuibank_merchant_preferentialproduct_it(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_IT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.current_my_product_id, isMarketable=2)
    result = send_request(ParamsObject, context=context)
    k = 0
    while (k < 5):
        if '9999' in result.text:
            k = k + 1
            time.sleep(2)
            result = send_request(ParamsObject, context=context)
        else:
            break
    assertion_tools(ParamsObject, result, order=0)


@then('新增之发货商户查询')
def anhuibank_merchant_lm(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_LM')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('名优特惠商品新增')
def anhuibank_merchant_preferentialproduct_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialProduct_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    context.current_my_name = '接口测试商品' + str(gb.getRandomBetweenInt(99999))
    push_replaceParams(ParamsObject, 'Body', productName=context.current_my_name,
                       productFullName=str(gb.getRandomBetweenInt(99999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('品牌管理列表')
def anhuibank_bank_preferentialproduct_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_PreferentialProduct_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('品牌管理广告列表')
def anhuibank_bank_brandad_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_BrandAd_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('品牌排序列表')
def anhuibank_bank_preferentialbrand_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_PreferentialBrand_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('操作日志列表')
def anhuibank_bank_operatorlog_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_OperatorLog_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('新增组织机构')
def anhuibank_bank_bankorg_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_BankOrg_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    context.org_name = '测试组织' + str(gb.getRandomBetweenInt(9999))
    push_replaceParams(ParamsObject, 'Body', orgName=context.org_name,
                       orgCode=str(gb.getRandomBetweenInt(999999999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


# TODO：为动态化，测试组织9000若没被删除不影响
@then('银行端编辑组织')
def anhuibank_merchant_bankorg_ue(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_bankOrg_ue')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('新增组织之组织信息获取')
def anhuibank_bank_bankorg_dl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_BankOrg_DL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('新增组织之用户列表查询')
def anhuibank_bank_operator_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Operator_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('新增组织之地址查询')
def anhuibank_bank_bankorg_sa(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_BankOrg_SA')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端新增用户')
def anhuibank_bank_operator_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Operator_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', loginName=str(gb.getRandomBetweenInt(99999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('新增用户之角色查询')
def anhuibank_bank_role_alt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Role_ALT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('组织查询')
def anhuibank_bank_bankorg_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_bankOrg_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('角色新增')
def anhuibank_bank_role_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Role_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', roleName=str(gb.getRandomBetweenInt(99999)))
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('授权资源列表')
def anhuibank_bank_role_rlt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Role_RLT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('用户信息查询')
def anhuibank_bank_member_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Member_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('广告管理查询')
def anhuibank_bank_ad_list(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_AD_List')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('广告详情之地区查询')
def anhuibank_bank_ad_area(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_AD_AREA')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('广告详情之广告位查询')
def anhuibank_bank_ad_positionpage(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_AD_PositionPage')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('限时特价活动列表')
def anhuibank_bank_saleactivity_lt(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_SaleActivity_LT')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核商户列表-依赖查询')
def anhuibank_merchant_approvallt_depar(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Approvallt_depar')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', merchantName=context.current_merchant_name)
    result = send_request(ParamsObject, context=context)
    # 捕获创建的商户信息
    context.merchantId = generatorTools.StringBar.LRFindString(result.text, 'merchantId":"', '","')[0]
    context.auditId = generatorTools.StringBar.LRFindString(result.text, 'auditId":"', '","')[0]
    context.merchantUserId = generatorTools.StringBar.LRFindString(result.text, 'merchantUserId":"', '","')[0]
    context.taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('待审核商户详情')
def anhuibank_bank_merchant_addl(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Bank_Merchant_ADDL')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', merchantId=context.merchantId, auditId=context.auditId,
                       merchantUserId=context.merchantUserId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('商户的审核-法人审核')
def anhuibank_merchant_audit_ma(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Audit_ma')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', auditId=context.auditId, taskId=context.taskId, bessId=context.merchantId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('待审核商户列表-省联社依赖查询')
def anhuibank_merchant_approvallt_sls_depar(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Approvallt_sls_depar')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', merchantName=context.current_merchant_name)
    result = send_request(ParamsObject, context=context)
    context.taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('商户的审核-省联社审核')
def anhuibank_merchant_audit_ma_sls(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Audit_ma_sls')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', auditId=context.auditId, taskId=context.taskId, bessId=context.merchantId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端商户编辑')
def anhuibank_merchant_merchant_ue(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_UE')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    gb = generatorTools.RandomBar()
    push_replaceParams(ParamsObject, 'Body', phone=str(gb.getRandomBetweenInt(999)),
                       merchantUserId=context.merchantUserId, merchantId=context.merchantId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端商户重置密码')
def anhuibank_merchant_merchant_rp(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_RP')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', merchantId=context.merchantId, merchantUserId=context.merchantUserId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端商户禁用')
def anhuibank_merchant_merchant_uf_false(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_UF_false')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', merchantId=context.merchantId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端商户启用')
def anhuibank_merchant_merchant_uf_true(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_UF_true')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', merchantId=context.merchantId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端商户解约')
def anhuibank_merchant_merchant_tn(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Merchant_TN')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', merchantId=context.merchantId)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('门店详情')
def anhuibank_merchant_outlet_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_Outlet_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('品牌详情')
def anhuibank_merchant_pendauit_detail(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PendAuit_Detail')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Params', brandId=context.brandId, auditNumber=context.auditNumber)
    result = send_request(ParamsObject, context=context)
    context.brandId = generatorTools.StringBar.LRFindString(result.text, 'brandId":"', '"')[-1]
    context.auditNumber = generatorTools.StringBar.LRFindString(result.text, 'auditNumber":"', '"')[-1]
    if getAttr(context, 'pp_taskId') == generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[0]:
        context.pp_taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[-1]
    else:
        context.pp_taskId = generatorTools.StringBar.LRFindString(result.text, 'taskId":"', '"')[0]
    assertion_tools(ParamsObject, result, order=0)


@then('品牌新增')
def anhuibank_merchant_preferentialbrand_ad(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_PreferentialBrand_AD')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    context.current_brand_name = '品牌' + str(gb.getRandomBetweenInt(99999))
    push_replaceParams(ParamsObject, 'Body', brandName=context.current_brand_name,
                       merchantId=context.merchantId, merchantName=context.current_merchant_name)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('品牌审核-法人行社')
def anhuibank_merchant_groupproduct_audit(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_Audit')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.brandId, taskId=context.pp_taskId,
                       instanceId=context.auditNumber)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('品牌审核-省联社')
def anhuibank_merchant_groupproduct_audit_sls(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_GroupProduct_Audit_sls')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body', productId=context.brandId, taskId=context.pp_taskId,
                       instanceId=context.auditNumber)
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端修改密码新')
def anhuibank_merchant_safecenter_lpue(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_safeCenter_lpue')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body',
                       oldPassword='96cae35ce8a9b0244178bf28e4966c2ce1b8385723a96a6b838858cdd6ca0a1e',
                       password='efa2a77528f5d155530a8994aa3244a08c509f15060ebbce73cf9b75ea6937d0')
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)


@then('银行端修改密码旧')
def anhuibank_merchant_safecenter_lpue(context):
    ParamsObject = launch_request('anhuiBank', 'INTERFACE_PARAMS_Bank', 'AnhuiBank_Merchant_safeCenter_lpue')
    push_replaceParams(ParamsObject, 'Header', userId=context.userId, token=context.token)
    push_replaceParams(ParamsObject, 'Body',
                       oldPassword="efa2a77528f5d155530a8994aa3244a08c509f15060ebbce73cf9b75ea6937d0",
                       password="b2ab0c8c24c5d5109b40434079e5b7ea19f63095c00c9f69323879280dec1f6c")
    result = send_request(ParamsObject, context=context)
    assertion_tools(ParamsObject, result, order=0)
