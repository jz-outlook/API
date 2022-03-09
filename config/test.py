# coding=utf-8

import smtplib
from email.mime.text import MIMEText
from email.header import Header

from_addr = '1512238569@qq.com'  # 邮件发送账号
to_addrs = '1512238569@qq.com'  # 接收邮件账号
qqCode = 'mwhmrtnvfozsiefa'  # 授权码（这个要填自己获取到的）
smtp_server = 'smtp.qq.com'  # 固定写死
smtp_port = 465  # 固定端口

# 配置服务器
stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
stmp.login(from_addr, qqCode)

# 组装发送内容
message = MIMEText('我是发送的内容11111111111111111', 'plain', 'utf-8')  # 发送的内容
message['From'] = Header("Python邮件预警系统", 'utf-8')  # 发件人
message['To'] = Header("管理员", 'utf-8')  # 收件人
subject = 'Python SMTP 邮件测试'
message['Subject'] = Header(subject, 'utf-8')  # 邮件标题

try:
    stmp.sendmail(from_addr, to_addrs, message.as_string())
except Exception as e:
    print('邮件发送失败--' + str(e))
print('邮件发送成功')


# coding=utf-8
# 1.先设置编码，utf-8可支持中英文，如上，一般放在第一行
# 2.注释：包括记录创建时间，创建人，项目名称。
# ----------------------------------------------------------------------------------------------------------------------
# 3.导入模块
# import smtplib
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
# from email.header import Header
# from email import encoders
# from email.mime.base import MIMEBase

#
# def send_mail(file_new):
#     # -----------1.跟发件相关的参数------
#     smtpserver = 'smtp.qq.com'  # 发件服务器
#     port = 465  # 端口
#     username = '1512238569@qq.com'  # 发件箱用户名
#     password = 'mwhmrtnvfozsiefa'  # 发件箱密码
#     sender = '1512238569@qq.com'  # 发件人邮箱
#     receiver = ['1512238569@qq.com']  # 收件人邮箱
#     name = '张笑笑'
#     # ----------2.编辑邮件的内容------
#     # 读文件内容
#     f = open(file_new, 'rb')
#     mail_body = f.read()
#     f.close()
#     # 邮件正文是MIMEText
#     body = MIMEText(mail_body, 'html', 'utf-8')
#     # 邮件对象
#     msg = MIMEMultipart()
#     msg['Subject'] = Header("自动化测试报告", 'utf-8').encode()  # 主题
#     msg['From'] = Header(u'测试机 <%s>' % sender)  # 发件人
#     msg['To'] = Header(u'测试负责人 <%s>' % name)  # 收件人
#     msg['To'] = ';'.join(receiver)
#     msg.attach(body)
#     # # MIMEBase表示附件的对象
#     att = MIMEText(mail_body, "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     # filename是显示附件名字
#     att["Content-Disposition"] = 'attachment; filename="test_report.html"'
#     msg.attach(att)
#     # ----------3.发送邮件------
#     try:
#         smtp = smtplib.SMTP()
#         smtp.connect(smtpserver)  # 连服务器
#         smtp.login(sender, password)
#     except:
#         smtp = smtplib.SMTP_SSL(smtpserver, port)
#         smtp.login(sender, password)  # 登录
#     smtp.sendmail(sender, receiver, msg.as_string())  # 发送
#     smtp.quit()
#
#
# if __name__ == "__main__":
#     # 本地文件的路径
#     att_path = r'D:\Desktop\111.html'
#     send_mail(att_path)
