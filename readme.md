# 停电检测的服务

## 此项目的功能

此项目用来检测学校的停断电公告信息，并及时将新的停断电公告信息推送给订阅者的邮箱，从而让订阅者提前做好服务器断电的准备工作，避免服务器等设备因意外断电而造成数据丢失。

## 为何会有这个项目

1. 教研室曾因为没有及时获知学校的停电通告，没有提前关闭服务器，造成服务器上的数据丢失。事后的数据恢复工作十分繁杂，且未备份的数据没能找回。简而言之，就是因为服务器意外断电造成过数据丢失。
2. 在断电前几天，学校就会在后勤保障部门的网站上提前通知停电事件
3. 本人会忘记关注学校的停电通知，因此有新的停电事件公布时想让程序自动推送本人邮箱


## 所用到的技术

- Django （Python Web 框架）
- django-crontab （Django 定时任务）
- selenium (数据爬取)

## 环境依赖

- Linux
- Python 3
- chromium-chromedriver (安装: sudo apt-get install chromium-chromedriver)
- nginx （部署用，也可直接采用 runserver 运行服务）
- python 包: requirement.txt 文件

## 部署

1. 部署前先在 power_outage_notify/settings.py 中编辑自己用于通知的邮箱 

        # TODO: 请设置自己用于发邮件的邮箱, 设置自己的邮箱及授权码
        # 自己的邮箱
        EMAIL_HOST_USER = 'xxx@126.com'
        # 自己的邮箱授权码，非密码
        EMAIL_HOST_PASSWORD = 'xxxx'
       
2. 添加爬虫检测的定时服务: python manage.py crontab add
2. 查看定时服务: python manage.py crontab show
3. python manage.py makemigrations
4. python manage.py migrate (数据库迁移)
5. python manage.py createsuperuser （创建后台管理员账号）
6. python manage.py collectstatic （生成静态文件）
7. python manage.py runserver
   （运行服务，此方式仅在单机测试环境使用，生产环境部署请使用 Nginx + wsgi
   方式运行）
9. 进入 admin 后台，添加订阅者的邮箱
   
## 运行效果

- 学校发布通知信息的网站

![学校后勤网站的公告](image/image0.png)

- 后端爬取到的停电信息

![停电公告数据](image/image1.png)

- 订阅者信息

![订阅者信息](image/image2.png)

- 邮箱通知效果

![邮箱通知效果](image/image3.png)