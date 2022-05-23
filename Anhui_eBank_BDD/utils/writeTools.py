# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
import os

# 指定不编译哪些文件可以传递一个文件名数据，注意，文件名不包含后缀
import sys

import shutil

from utils.readTools import launch_request, get_all_ParamObject
from utils.tools import is_params_exist


# 列出所有需要遍历的文件
def listDir(root, notNeedFileList=[]):
    fileList = []
    for filename in os.listdir(root):
        if 'pyc' not in filename and '__pycache__' not in filename and '__init__' not in filename:
            fileList.append(filename.split('.')[0])
    for value in notNeedFileList:
        fileList.remove(value)
    return fileList


# 获取参数对象
def getParamObject(path='steps', notNeedFileList=[]):
    fileNameList = listDir('../database', notNeedFileList=notNeedFileList)
    for filename in fileNameList:
        if filename != '__global_params':
            file_path = make_dir(path, filename)
            mod = get_all_ParamObject(filename)
            for object_name in mod.__all__:
                param = getattr(mod, object_name)
                for p in param:
                    InterfaceLocation = filename + '__' + object_name + '__' + p['InterfaceName']
                    writeFiles(file_path, InterfaceLocation, p)


# 获取文件列表以及参数位置
def get_fileList_location(notNeedFileList=[]):
    fileList = listDir('../database', notNeedFileList=notNeedFileList)
    fileObject = []
    for filename in fileList:
        if filename != '__global_params':
            mod = get_all_ParamObject(filename)
            InterfaceLocationList = []
            for object_name in mod.__all__:
                param = getattr(mod, object_name)
                for p in param:
                    InterfaceLocation = filename + '__' + object_name + '__' + p['InterfaceName']
                    InterfaceLocationList.append(InterfaceLocation)
            fileObject.append([filename, InterfaceLocationList])
    return fileObject


def make_dir(path, fileName, isCopy=True, typeName="stepts"):
    if ('darwin' in sys.platform):
        cutPathString = '/'
    else:
        cutPathString = '\\'
    fileName = sys.path[0] + cutPathString + '..' + cutPathString + path + cutPathString + fileName + '_' + typeName + '.py'
    initFileName = sys.path[0] + cutPathString + '..' + cutPathString + path + cutPathString + '__init__.py'
    if not os.path.exists(initFileName):
        open(initFileName, 'w')
    f = open(fileName, 'w')
    f.truncate()
    f.close()
    if isCopy:
        shutil.copy(sys.path[0] + cutPathString + 'originFile.py', fileName)
    return fileName

# 书写steps文件
def writeFiles(file_path, InterfaceLocation, ParamsObject):
    file_info = InterfaceLocation.split('__')
    with open(file_path, 'a+') as f:
        if 'InterfaceDesc' in ParamsObject:
            f.write("@then('" + ParamsObject['InterfaceDesc'] + "')\n")
        else:
            f.write("@then('" + ParamsObject['InterfaceName'] + "')\n")
        f.write("def " + ParamsObject['InterfaceName'].lower().replace(' ', '_') + "(context):\n")
        f.write(
            "\tParamsObject = launch_request('" + file_info[0] + "', '" + file_info[1] + "', '" + file_info[2] + "')\n")
        # 深度遍历各项参数，寻找出关键词
        searchList = ['Header', 'URL', 'Params', 'Body']
        for searchString in searchList:
            Keys = is_params_exist(ParamsObject[searchString])
            if Keys:
                stringList = ''
                for keys in Keys:
                    value = keys.replace('{', '').replace('}', '')
                    stringList = stringList + value + "='',"
                f.write("\tpush_replaceParams(ParamsObject, '" + searchString + "', " + stringList[0:-1] + ")\n")
        isAssertion = 'Assertion' in ParamsObject.keys()
        if isAssertion:
            f.write("\tresult = send_request(ParamsObject, context=context)\n")
            write_assertion(f, ParamsObject)
        else:
            f.write("\tsend_request(ParamsObject)\n\n\n")


# 继续书写断言部分
def write_assertion(f, params_object):
    search_info = params_object['Assertion']['SearchInfo']
    for info in search_info:
        Keys = is_params_exist(info)
        if Keys:
            stringList = ''
            for keys in Keys:
                value = keys.replace('{', '').replace('}', '')
                stringList = stringList + value + "='',"
            f.write("\tassertion_tools(ParamsObject, result, order=" + str(search_info.index(info)) + ", " + stringList[
                                                                                                             0:-1] + ")\n")
        else:
            f.write("\tassertion_tools(ParamsObject, result, order=" + str(search_info.index(info)) + ")\n")
    f.write("\n\n")


# 书写静态参数文件内容
def write_static_file_content(file_path, params_list):
    with open(file_path, 'a+') as f:
        f.write("# -*- coding:utf-8 -*-\n\n\n")
        f.write("__all__ = ['PARAMS_LIST']\n\n\n")
        f.write("PARAMS_LIST = [\n")
        for name in params_list:
            f.write("\t{\n")
            f.write("\t\t\'name\': \'" + name + "\',\n")
            f.write("\t\t\'data\': \'\'\n")
            f.write("\t},\n")
        f.write("]\n")


# 书写静态参数文件
def write_static_file():
    info_list = get_fileList_location()
    for info in info_list:
        file_path = make_dir('temp', info[0], isCopy=False, typeName='params')
        write_static_file_content(file_path, info[1])


if __name__ == '__main__':
    write_static_file()
    getParamObject(path='temp')
