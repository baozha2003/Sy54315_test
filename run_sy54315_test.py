#!/usr/bin/env python
# -*- coding:UTF-8 -*-
import unittest
import time
import os
from HTMLTestRunner_PY3 import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import smtplib
import datetime


# 定义发送邮件
def send_mail(file_new):
    # 发送邮件服务器
    smtpserver = 'smtp.163.com'
    # 发送邮箱用户/密码
    user = 'baozha2003@163.com'
    password = 'baozha2003'
    # 发送邮箱
    sender = 'baozha2003@163.com'
    # 接收邮箱
    receiver = ['185143666@qq.com','523228680@qq.com']
    # 今天日期
    # today = str(datetime.date.today())

    sendfile = open(file_new, 'rb')
    mail_body = sendfile.read()
    sendfile.close()

    # msg = MIMEText(mail_body,'html','utf-8')
    # 创建一个带附件的实例
    msg = MIMEMultipart()
    # 定义发件人和收件人参数
    msg['from'] = 'baozha2003@163.com'
    msg['to'] = '185143666@qq.com,523228680@qq.com'

    # 发送邮件主题
    subject = 'Sy54315自动化测试报告'
    msg['Subject'] = Header(subject, 'utf-8')

    # 邮件正文内容
    msg.attach(MIMEText('测试报告请查看附件', 'plain', 'utf-8'))

    att = MIMEText(mail_body, 'base64', 'utf-8')
    att["Content-Type"] = "application/octet-stream"
    # 这里的filename可以任意写，写什么名字，邮件中显示什么名字
    att["Content-Disposition"] = 'attachment;filename="Report.html"'
    msg.attach(att)

    # 链接发送邮件
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
    print('邮件发送成功email has send out !')


# ========================找到最新的测试报告文件===========================
def new_report(testreport):
    lists = os.listdir(testreport)
    # 重新按时间对目录下的文件进行排序
    lists.sort(key=lambda fn: os.path.getatime(testreport + "\\" + fn))
    file_new = os.path.join(testreport, lists[-1])
    # print(file_new)
    return file_new


if __name__ == '__main__':
    test_dir = './sy54315/test_case/'
    test_report = './sy54315/report/'
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='*case.py')
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    filename = test_report + now + 'result.html'
    runner = unittest.TextTestRunner()

    # 定义报告存放路径
    fp = open(filename, 'wb')
    # 定义测试报告
    runner = HTMLTestRunner(stream=fp,
                            title='Sy54315测试报告',
                            description='用例执行情况：')

    runner.run(discover)  # 运行测试用例
    fp.close()  # 关闭报告文件
    new_report = new_report(test_report)#找到最新的报告文件
    send_mail(new_report)#发送报告文件
