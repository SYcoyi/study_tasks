# -*- coding:utf-8 -*-
"""
Created on 2017年11月14日

@author: sheldon
"""
import os
import sys
import logging


def launch_request(FileName, ParamName, InterfaceName, SourcePath='database', StaticPath='static_data'):
    sys.path.append(SourcePath)
    sys.path.append(StaticPath)
    mod = my_import(FileName)
    for params in mod.__all__:
        if params == ParamName:
            param = getattr(mod, params)
            for p in param:
                try:
                    if p['File']:
                        p['File'] = os.getcwd() + '/files/' + p['File']
                except:
                    p['File'] = None
                if p['InterfaceName'] == InterfaceName:
                    try:
                        mod_data = my_import(FileName + "_params")
                        data_param = getattr(mod_data, mod_data.__all__[0])
                        for data in data_param:
                            if data['name'] == FileName + "__" + ParamName + "__" + InterfaceName:
                                p['params'] = data['data']
                    except:
                        print('没有匹配到响应的请求参数json')
                    return p


def my_import(name):
    import importlib
    model_ins = __import__(name)
    mod = importlib.reload(model_ins)
    components = name.split('.')
    for comp in components[1:]:
        mod = getattr(mod, comp)
    return mod


def get_all_ParamObject(FileName, SourcePath='../database'):
    sys.path.append(SourcePath)
    mod = my_import(FileName)
    return mod
