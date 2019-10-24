# -*- coding: utf-8 -*-
# @Time    : 2019/10/22 20:56
# @Author  : MLee
# @File    : crawler.py
import re
from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_outage_info(show_browser=False):
    """
    获取 UESTC 后勤保障部最新的停电公告
    :param show_browser: 是否在爬虫是显示浏览器信息
    :return: 停电公告信息的集合
    """
    chrome_options = Options()
    if not show_browser:
        # Chrome 无头模式
        chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(options=chrome_options)

    # 获取后勤保障部通告通知的网页
    driver.get("https://hq.uestc.edu.cn/web/list.jsp?type_id=4")
    sleep(2)

    # 点击首页按钮
    element = driver.find_element_by_xpath('//*[@id="yw0"]/li[1]')
    element.click()
    sleep(5)

    # 获取所有通知的 div
    content_divs = driver.find_elements_by_xpath('/html/body/div[2]/div[2]/div[2]/div')

    # 定位所有通知中的标题栏
    contents = list()
    for content_div in content_divs:
        content_title2 = content_div.find_elements_by_tag_name("h4")
        contents.extend(content_title2)

    pattern = re.compile(r'[停断]电')
    notify_set = set()
    for announcement in contents:
        # 匹配标题中的信息
        announcement = announcement.find_element_by_tag_name('a')
        announcement_title = announcement.get_attribute("text")
        announcement_url = announcement.get_attribute('href')
        # 搜索标题中是否存在“停电”关键字
        result = pattern.search(announcement_title)
        if result:
            notify_set.add((announcement_title, announcement_url))

    # 关闭浏览器
    driver.quit()

    return notify_set

if __name__ == '__main__':
    print(get_outage_info())
