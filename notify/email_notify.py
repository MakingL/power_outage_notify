# -*- coding: utf-8 -*-
# @Time    : 2019/10/12 11:24
# @Author  : MLee
# @File    : email_notify.py

from django.core.mail import EmailMultiAlternatives

from power_outage_notify.settings import EMAIL_HOST_USER


def do_email_notify(email, page_title, page_url, from_email=EMAIL_HOST_USER):
    """
    邮件通知停电信息
    :param page_title: 停电的标题
    :param page_url: 具体的通知页面
    :return:
    """

    title = '有新的停电通告 {}'.format(page_title)
    subject, from_email, to = title, from_email, email
    text_content = ""
    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    html_content = """
                    你好: <br>
                    <p>学校有发布了新的停电通告，请确认是否对您有影响，以提前做好相应的措施，避免造成财产损失。</p>
                    <p>具体信息请查看学校的通告页：<a href="{page_url}" target=blank>{title}</a></p>
                    """.format(page_url=page_url, title=page_title)
    msg.attach_alternative(html_content, "text/html")
    msg.send()
