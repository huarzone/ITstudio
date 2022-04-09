from . import models as us
from api.models import *
from django.shortcuts import redirect
from untils.configs import get_code



from django.contrib import admin

class StatusFilter(admin.SimpleListFilter):
    title = "录取阶段"
    parameter_name = "status"

    def lookups(self, request, model_admin):
        return (
            ('0', "初审未开始"),
            ('1', "初审通过"),
            ('2', "初审未通过"),
            ('3', "面试通过"),
            ('4', "面试未通过"),
            ('5', "笔试通过"),
            ('6', "笔试未通过"),
            ('7', "录取通过"),
            ('8', "录取未通过"),
        )

    def queryset(self, request, queryset):
        if self.value() in ['0', '1', '2', '3', '4', '5', '6', '7', '8']:
            return queryset.filter(status=self.value())


class DepartmentFilter(admin.SimpleListFilter):
    title = "部门选择"
    parameter_name = "departer"

    def lookups(self, request, model_admin):
        return (
            ('0', "程序开发"),
            ('1', "游戏开发"),
            ('2', "Web开发"),
            ('3', "APP开发"),
            ('4', "UI设计"),
        )

    def queryset(self, request, queryset):
        if self.value() == "0":
            return queryset.filter(departer="程序开发")
        elif self.value() == "1":
            return queryset.filter(departer="游戏开发")
        elif self.value() == "2":
            return queryset.filter(departer="Web开发")
        elif self.value() == "3":
            return queryset.filter(departer="APP开发")
        elif self.value() == "4":
            return queryset.filter(departer="UI设计")


@admin.register(us.Register)
class Registers(admin.ModelAdmin):
    # 要显示的字段
    list_display = ['name', 'phone', 'major', 'departer', 'state', 'enable', 'create_time']
    # 搜索框，按照元组内指定字段搜索
    search_fields = ('name', 'departer')
    # 选中条目个数显示
    actions_selection_counter = True
    # action功能摆放位置
    # actions_on_bottom = True
    # actions_on_top = True
    # 不允许点击id跳转
    # list_display_links = None
    # 按时间过滤
    date_hierarchy = 'create_time'
    # 每页显示多少条
    list_per_page = 20
    # 过滤器
    list_filter = (StatusFilter, DepartmentFilter)
    # 允许只读字段
    readonly_fields = ['name']


    # 定义动作列表
    actions = ["status_0", "status_1", "status_2", "status_3", "status_4", "status_5", "status_6",
               "status_7", "status_8", "is_active", "not_is_active", "export", "ip"]

    def status_0(self, request, queryset):
        row_updated = queryset.update(status=0)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_0.short_description = '初审未开始'

    def status_1(self, request, queryset):
        row_updated = queryset.update(status=1)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_1.short_description = '初审通过'

    def status_2(self, request, queryset):
        row_updated = queryset.update(status=2)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_2.short_description = '初审未通过'

    def status_3(self, request, queryset):
        row_updated = queryset.update(status=3)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_3.short_description = '面试通过'

    def status_4(self, request, queryset):
        row_updated = queryset.update(status=4)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_4.short_description = '面试未通过'

    def status_5(self, request, queryset):
        row_updated = queryset.update(status=5)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_5.short_description = '笔试通过'

    def status_6(self, request, queryset):
        row_updated = queryset.update(status=6)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_6.short_description = '笔试未通过'

    def status_7(self, request, queryset):
        row_updated = queryset.update(status=7)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_7.short_description = '录取通过'

    def status_8(self, request, queryset):
        row_updated = queryset.update(status=8)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    status_8.short_description = '录取未通过'

    def is_active(self, request, queryset):
        row_updated = queryset.update(enable=1)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    is_active.short_description = '一键激活'

    def not_is_active(self, request, queryset):
        row_updated = queryset.update(enable=0)
        self.message_user(request, "修改了{}条字段".format(row_updated))

    not_is_active.short_description = '一键冻结'

    def export(self, request, queryset):
        sid = get_code(type='sid')
        queryset.update(sid=sid)
        return redirect(f"/api/export?sid={sid}")

    export.short_description = '数据导出'

    def ip(self, request, queryset):
        return redirect("/api/get/ip?type=code")

    ip.short_description = '用户IP池'


class Works(admin.ModelAdmin):
    list_display = ['title', 'year', 'url', 'create_time']
    search_fields = ('title',)
    date_hierarchy = 'create_time'
    list_filter = ['title']


class Departments(admin.ModelAdmin):
    list_display = ['name', 'introduce', 'create_time']
    search_fields = ('name', 'introduce',)
    date_hierarchy = 'create_time'
    list_filter = ['name']


class Members(admin.ModelAdmin):
    list_display = ['name', 'grade', 'department', 'create_time']
    search_fields = ('name', 'grade', 'department',)
    date_hierarchy = 'create_time'
    list_filter = ['grade', 'department']


class Historys(admin.ModelAdmin):
    list_display = ['title', 'year', 'detail', 'create_time']
    search_fields = ('title',)
    date_hierarchy = 'create_time'
    list_filter = ['year']


class Comment(admin.ModelAdmin):
    list_display = ['content', 'create_time']
    search_fields = ('content',)
    date_hierarchy = 'create_time'
    actions = ["ip", "ban_ip"]

    def ip(self, request, queryset):
        return redirect("/api/get/ip?type=comment")

    ip.short_description = '用户IP池'

    def ban_ip(self, request, queryset):
        return redirect("/api/get/ip?type=ban")

    ban_ip.short_description = '被封IP池'


# 注册   第一个参数为数据库模型， 第二为自己写的类
admin.site.register(us.Work, Works)
admin.site.register(us.Department, Departments)
admin.site.register(us.Member, Members)
admin.site.register(us.History, Historys)
admin.site.register(us.Comment, Comment)
