#coding = utf-8
##作业，pytest生成建议报告并发送至邮箱


# import smtplib
# from smtplib import SMTP
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
#
# ##发件相关的参数
# smtpserver ="smtp.163.com"#发件服务器
# port = 25
# sender = "XXXX"
# psw = "XXXXX"
# receiver = "XXX"
#
# ##编辑邮件内容
# msg = MIMEMultipart()
#
# body = '\r\n'.join((      #组合sendmail方法的邮件主体内容，各段以"\r\n"进行分离
#     "From: %s" %"pytest",
#     "TO: %s" %"姓名",
#     "subject: %s" %"pytest_autoSend",
#     "",
# ))
# att1 = open('report/report2.html','r',encoding='utf-8').read()
# print(att1)
# # msg.attach(att1)
# # print(att1)
# subject = "pytest_auto"
# HOST = smtpserver
# FROM = sender
# TO = receiver
# SUBJECT =subject
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(sender,psw)
# smtp.sendmail(sender,receiver,att1)
# smtp.quit()


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import logging

def send_mail():
    # 发送邮箱服务器
    smtp_server = 'smtp.163.com'

    # 发送邮箱用户名密码
    user = 'XXXX'##'你的163邮箱名称'
    password = 'XXXX'#'开启设置的时候复制的登录密码'

    # 接收邮箱
    receives ="XXXX" ##['你需要发给的邮箱1', '你需要发给的邮箱2', '你需要发给的邮箱3'...]

    # 发送邮件和主题内容
    subject = 'Auto_test'
    content = '<html><h1 style="color:red">自动化邮件发送_附件</h1></html>'

    # 构建发送与接收信息
    msg_root = MIMEMultipart()
    msg_root.attach(MIMEText(content, 'html', 'utf-8'))
    msg_root['subject'] = subject
    msg_root['From'] = user
    msg_root['To'] = ','.join(receives)

    # 构造附件3（附件为HTML格式的网页）
    att3 = MIMEText(open('report/report1.html', 'rb').read(), 'base64', 'utf-8')
    att3["Content-Type"] = 'application/octet-stream'
    att3["Content-Disposition"] = 'attachment; filename="report_test.html"'
    msg_root.attach(att3)

    # SSL协议端口号要使用465
    smtp = smtplib.SMTP_SSL(smtp_server, 465)

    # H E L O 向服务器标识用户身份
    smtp.helo(smtp_server)
    # 服务器返回结果确认
    smtp.ehlo(smtp_server)
    # 登录邮箱服务器用户名和密码
    smtp.login(user, password)

    logging.info("Start send email...")

    smtp.sendmail(user, receives, msg_root.as_string())

    smtp.quit()
    logging.info("Send End！")
    logging.info('============================================================================================')

send_mail()