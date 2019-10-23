# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 20:59
# @Author  : MLee
# @File    : task.py
from .crawler import get_outage_info
from .email_notify import do_email_notify
from .models import PowerOutageInfo, SubscriberInfoModel


def email_notify(title, url):
    email_set = SubscriberInfoModel.get_all_subscriber_email()
    for email in email_set:
        do_email_notify(email, title, url)


def task_crawl_power_outage_info():
    """获取"""
    power_outage_info = get_outage_info()
    if power_outage_info:
        for info in power_outage_info:
            title, url = info
            if PowerOutageInfo.has_power_outage_info(url):
                continue
            PowerOutageInfo.add_power_outage_info(title=title, url=url)
            email_notify(title, url)
