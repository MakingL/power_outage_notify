from django.contrib import admin

from .models import PowerOutageInfo, SubscriberInfoModel


@admin.register(PowerOutageInfo)
class PowerOutageInfoAdmin(admin.ModelAdmin):
    # 按指定的顺序，显示指定的字段
    list_display = ("title", "page_url", "create_time")
    # 指定修改的字段的显示，下面禁止了修改的链接，所以此处定义无用
    fields = ("title", "page_url")

    # action 按钮所在的位置
    actions_on_top = True
    actions_on_bottom = True
    # save 按钮所在的位置
    save_on_top = True
    # 空值所填充的内容
    empty_value_display = '-empty-'
    # 顶部的时间导航栏，日期过滤器
    date_hierarchy = 'create_time'
    # 右侧的过滤器
    list_filter = ("create_time",)
    # 链接修改页面的字段
    list_display_links = ("title",)
    list_max_show_all = 200
    # 每个页面显示的记录数
    list_per_page = 100
    # 设置排序方式
    ordering = ["-create_time"]
    # 控制是否在 admin 页面显示 "View site" 的链接
    view_on_site = False


@admin.register(SubscriberInfoModel)
class SubscriberInfoModelAdmin(admin.ModelAdmin):
    # 按指定的顺序，显示指定的字段
    list_display = ("email", "create_time")
    # 指定修改的字段的显示，下面禁止了修改的链接，所以此处定义无用
    fields = ("email",)

    # action 按钮所在的位置
    actions_on_top = True
    actions_on_bottom = True
    # save 按钮所在的位置
    save_on_top = True
    # 空值所填充的内容
    empty_value_display = '-empty-'
    # 顶部的时间导航栏，日期过滤器
    date_hierarchy = 'create_time'
    # 右侧的过滤器
    list_filter = ("create_time",)
    # 链接修改页面的字段
    list_display_links = ("email",)
    list_max_show_all = 200
    # 每个页面显示的记录数
    list_per_page = 100
    # 设置排序方式
    ordering = ["-create_time"]
    # 控制是否在 admin 页面显示 "View site" 的链接
    view_on_site = False
