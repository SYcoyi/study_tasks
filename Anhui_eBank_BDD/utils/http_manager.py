#!/usr/bin/env python
# -- coding=utf-8 --

'''
http请求工具类
'''
import logging

import requests

from utils.basicSwitch import switch
from utils.readTools import launch_request
from utils.tools import push_replaceParams, assertion_tools

from requests import post, get
import json


def add_step_info(scenarioId, content):
    path = 'http_result/' + 'scenario' + str(scenarioId) + '.json'
    with open(path, 'a+') as f:
        f.write(content + '\n')


def generate_result_json(context, result, ParamsObject):
    http_result = {
        'step_name': context.current_step.name,
        'step_id': str(id(context.current_step)),
        'step_keyword': context.current_step.keyword,
        'url': result.url,
        'method': result.request.method,
        'cookies': '{}',
        'waste_time': result.elapsed.total_seconds(),
        'rest_headers': ParamsObject['Header'],
        'resp_headers': result.headers,
        'resp_status_code': result.status_code,
        'resp_body': result.text,
    }
    if result.request.method == 'POST':
        http_result['rest_body'] = ParamsObject['Body']
    else:
        http_result['rest_body'] = ParamsObject['Params']
    return str(http_result)


def send_request(ParamsObject, context=None):
    for case in switch(ParamsObject['Method']):
        if case('Post'):
            return post_request(ParamsObject, context=context)
            break

        if case('Get'):
            return get_request(ParamsObject, context=context)
            break

        if case('Put'):
            return put_request(ParamsObject, context=context)
            break

        if case('Delete'):
            return delete_request(ParamsObject, context=context)
            break


def delete_request(ParamsObject, context=None):
    logging.info('---------开始' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    logging.info('请求URL：' + str(ParamsObject['URL']))
    logging.info('请求Params：' + str(ParamsObject['Params']))
    logging.info('请求头：' + str(ParamsObject['Header']))
    logging.info('请求体：' + str(ParamsObject['Body']))
    result = None
    result = requests.delete(ParamsObject['URL'], json=ParamsObject['Body'], params=ParamsObject['Params'],
                             headers=ParamsObject['Header'])
    add_step_info(id(context.scenario), generate_result_json(context, result, ParamsObject))
    logging.info('Delete:' + str(result.request.url))
    logging.info('返回报文：' + result.text)
    logging.info('---------结束' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    return result


def get_request(ParamsObject, context=None):
    logging.info('---------开始' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    logging.info('请求URL：' + str(ParamsObject['URL']))
    logging.info('请求Params：' + str(ParamsObject['Params']))
    logging.info('请求头：' + str(ParamsObject['Header']))
    files = None
    if ParamsObject['File'] is not None:
        files = {'file': (ParamsObject['File'].split('/')[-1], open(ParamsObject['File'], 'rb'))}
        result = requests.get(ParamsObject['URL'], headers=ParamsObject['Header'],
                              params=ParamsObject['Params'], files=files)
    else:
        result = requests.get(ParamsObject['URL'], params=ParamsObject['Params'], headers=ParamsObject['Header'],
                              files=files)
    isByte = False
    try:
        result.content.decode('utf-8')
    except:
        isByte = True
    if isByte == False:
        add_step_info(id(context.scenario), generate_result_json(context, result, ParamsObject))
        logging.info(result.text)
    logging.info('Get:' + str(result.request.url))
    logging.info('返回报文：' + result.text)
    logging.info('---------结束' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    return result


def put_request(ParamsObject, context=None):
    logging.info('---------开始' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    logging.info('请求URL：' + str(ParamsObject['URL']))
    logging.info('请求Params：' + str(ParamsObject['Params']))
    logging.info('请求头：' + str(ParamsObject['Header']))
    logging.info('请求体：' + str(ParamsObject['Body']))
    result = None
    if ParamsObject['File'] is not None:
        files = {'file': (ParamsObject['File'].split('/')[-1], open(ParamsObject['File'], 'rb'))}
        result = requests.put(ParamsObject['URL'], headers=ParamsObject['Header'],
                              data=ParamsObject['Body'], files=files)
    else:
        result = requests.put(ParamsObject['URL'], json=ParamsObject['Body'], headers=ParamsObject['Header'])
    add_step_info(id(context.scenario), generate_result_json(context, result, ParamsObject))
    logging.info('Put:' + str(result.request.url))
    logging.info('返回报文：' + result.text)
    logging.info('---------结束' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    return result


def post_request(ParamsObject, context=None):
    logging.info('---------开始' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    logging.info('请求URL：' + str(ParamsObject['URL']))
    logging.info('请求Params：' + str(ParamsObject['Params']))
    logging.info('请求头：' + str(ParamsObject['Header']))
    logging.info('请求体：' + str(ParamsObject['Body']))
    result = None
    if ParamsObject['File'] is not None:
        files = {'file': (ParamsObject['File'].split('/')[-1], open(ParamsObject['File'], 'rb'))}
        result = requests.post(ParamsObject['URL'], headers=ParamsObject['Header'],
                               data=ParamsObject['Body'], files=files)
    else:
        result = requests.post(ParamsObject['URL'], json=ParamsObject['Body'], headers=ParamsObject['Header'])
    add_step_info(id(context.scenario), generate_result_json(context, result, ParamsObject))
    logging.info('Post:' + str(result.request.url))
    logging.info('返回报文：' + result.text)
    logging.info('---------结束' + ParamsObject['InterfaceName'] + '请求---------' + ParamsObject['Method'])
    return result


if __name__ == '__main__':
    cookies = 'BAIDUID=5A8DA6DF4CFB63EB2E1F7DC20484539F:FG=1; PSTM=1517197616; BIDUPSID=B6438A6D4B057E726F040A4804054BE6; BD_UPN=123253; __cfduid=d338216f717216c0e31186ed57c583ff01522720111; ispeed_lsm=2; BDSFRCVID=ZqtOJeC629mj7w79aT_hUCIiiHnvcpvTH6aoMJ93ga-t-KmFyGoREG0PDf8g0KAbHA5togKK3gOTHx-F_2uxOjjg8UtVJeC6EG0P3J; H_BDCLCKID_SF=tJFOoDtbJDK3hDt4j-OHb-oH-UnLqh0fX2OZ0l8Ktqjae-8w56rB-lDd3tbAa4chMmjianomWIQHDp66y4j1X-tHjJbvapTPaN74KKJx5RLWeIJo5t5jyU_shUJiB5JMBan7XT6IXKohJh7FM4tW3J0ZyxomtfQxtN4eaDFKJKP-hCKRePbSMttfqxQQaRctato2WbCQyJjPqpcNLUbWQTtpQMnBqlvaBjFObfJ8yJRtq-cGKjQlKhtFDPCEJ6-8Jb4qoCIQKbREHnkk-tvE2JLHqxby26nuJ5T9aJ5nJD_BhJ3OjxCByTtrbRomB4c05C7I3qQlQpP-HJ7kM-cx-jkdjb7tJqFD0m7HKl0MLncWbb0xyUQD3xcXqfnMBMPe52OnaPPE3fAKftnOM46JehL3346-35543bRTohFLtDLBbD_le503MPJLqlQ02JbebbuX3b7EfKjoOq7_bf--Dlj-0l-HLTFttKtj-lOY2RTqsxn62jjxy5K_hprn5bbTfN7hKD3dKlQ_S66HQT3mbfrbbN3i-4j2f6TGWb3cWKOJ8UbS2KcPBTD02-nBat-OQ6npaJ5nJq5nhMtRy6CKjjJ0ja_DtTn2aI6eQ5rVaR7oHTrnhPF3Qj8vXP6-35KHJKLOQlOKfCK5flraLUrEMtK9BPQxJh37JD6yhPTs0K5vehRS2-Qohjk-2-oxJpOBQRbMopvaKtcjs-ovbURvDP-g3-7Oex5dtjTO2bc_5KnlfMQ_bf--QfbQ0abZqj_8tRCf_IDXf-3bfTrvh-ODhnF8bh_X5-RLfaQDLp7F5l8-hCTzM6JbjTF_3bn3LxJA2C57WtQJ-PQxOKQphUckejts-ecJexnL3j5xWMoN3KJmsbL9bT3vLtDnLHoJ2-biWb7M2MbdMT6P_IoG2Mn8M4bb3qOpBtQmJeTxoUtbWDcjqR8Zj6K-DjbP; BDUSS=nJoY1MwLXBQZlA0d3JaanJqNTF1cHFsaVU2b0RZYXdYa0Y2YmJFMEFTfk51MVpjQVFBQUFBJCQAAAAAAAAAAAEAAADH5e8Htrm2uc37zOy~1QAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAM0uL1zNLi9cZ; H_PS_PSSID=1460_21120_28205_28132_28267_27245; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=6; pgv_pvi=4639846400; pgv_si=s698589184; ZD_ENTRY=baidu; BD_HOME=1; sug=3; sugstore=1; ORIGIN=0; bdime=0; H_PS_645EC=054b%2B2%2FadhyoWoYFY6WU9ux9PVVGAInO2p9gzkXpehfhE7QojoBokolWcHQ; BDSVRTM=0'
    ParamsObject = launch_request('params', 'INTERFACE_PARAMS', 'Login interface')
    push_replaceParams(ParamsObject, 'Header', cookie=cookies)
    result = send_request(ParamsObject)
    abc = assertion_tools(ParamsObject, result, order=2, scope='aaa', lb='bbb', rb='ccc', matchString='ddd',
                          warningDesc='eee', isStop='fff')


# sheng写的请求，预留备用
def httprequest(header, url, method, params=None):
    """
        根据不同传入请求类型参数参数分出不同的请求
    """
    if method == 'post':
        html = post(url, data=json.dumps(params), headers=header)
        strss = html.text
        return strss
    elif method == 'get':
        html = get(url, headers=header)
        strss = html.text
        return strss
