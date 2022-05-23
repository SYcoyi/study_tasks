# 安徽社区


## 简介
* 项目地址 git@gitlab.f-road.com.cn:testplatform/Anhui_eBank_BDD.git
* 安徽社区项目api自动化，基于python + requests + behave(BDD) + allure(报告)实现


## 基本框架

* requests
* behave - python BDD实现， behave执行时，会读取当前目录下的behave.ini配置文件


## 项目运行依赖包
* pip install behave
* pip install requests
* pip install PyHamcrest
* pip install pymysql
* pip install xlrd
* pip install allure-behave
* 或pip install -r requirements.txt

## 基本结构
* allure_report  生成最终报告文件
* report/ allure_result/  临时报告目录
* features feature文件目录
* steps 步骤定义文件目录
* utils 常用工具目录
* environment.py 世界文件
* behave.ini behave基础配置文件


## 执行测试

* powershell 执行 behave -f allure_behave.formatter:AllureFormatter -o report ./features
* powershell 执行 allure generate report -o allure_report --clean
* powershell 执行 allure open allure_report
* 访问终端的链接，查看报告
* 查看日志 g2p_test.log


## behave常用命令

* 指定执行tag 
```bash
behave -f allure_behave.formatter:AllureFormatter -o report '.\features\LM Accounts Management\lm_account_opening.feature' -t DEBUG
```

* allure集成命令
```bash
allure serve report
```


## Git 提交步骤（同一个branch）

* 查看本地更新的代码
* commit需要提交的内容，到本地仓库
* git pull
* 查看其他人提交的内容
* 处理merge，如果存在的话
* 查看提交的内容
* git push


## TAG 标记

* NEED_LOGIN 暂无tag

## 环境测试数据
待补充

## 模块简介
* 目前分为银行端、商户pc端、商户个人端、客户个人端

## 当前进度
* 暂无