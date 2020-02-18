from django.db import models


class PowerOutageInfo(models.Model):
    """
    停电公告信息
    """
    title = models.CharField(verbose_name="通知标题", max_length=15)
    page_url = models.CharField(verbose_name="页面 URL", max_length=255)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

    def __str__(self):
        return str(self.page_url)

    class Meta:
        verbose_name = verbose_name_plural = "停电公告信息"
        # 声明此元选项所属的 APP
        app_label = "notify"

    @classmethod
    def add_power_outage_info(cls, title, url):
        obj = cls.objects.create(title=title, page_url=url)
        obj.save()

    @classmethod
    def has_power_outage_info(cls, url):
        filter_res = cls.objects.filter(page_url=url)
        return True if filter_res else False


class SubscriberInfoModel(models.Model):
    """
    订阅者 的详细信息
    """
    email = models.EmailField(verbose_name="订阅者邮箱", unique=True, primary_key=True)
    create_time = models.DateTimeField(verbose_name="创建时间", auto_now=True)

    def __str__(self):
        return str(self.email)

    class Meta:
        verbose_name = verbose_name_plural = "订阅者信息"
        # 声明此元选项所属的 APP
        app_label = "notify"

    @classmethod
    def get_all_subscriber_email(cls):
        email_set = set()
        for sub in cls.objects.all():
            email_set.add(sub.email)
        return email_set

    @classmethod
    def add_subscriber(cls, email):
        filter_res = cls.objects.filter(email=email)
        if filter_res:
            return True

        cls.objects.create(email=email).save()
