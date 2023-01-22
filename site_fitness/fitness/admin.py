from django.contrib import admin

from .models import *


class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'mail')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'id')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class ServicePhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_path',)
    list_display_links = ('photo_path',)


class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'mail')
    list_display_links = ('id', 'name')


class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'main_phrase')
    list_display_links = ('id', 'main_phrase')


class PermissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class RoleAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')

class ServiceTimetableAdmin(admin.ModelAdmin):
    list_display = ('id',)
    list_display_links = ('id',)


admin.site.register(Client, ClientAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(ServicePhoto, ServicePhotoAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Discount, DiscountAdmin)
admin.site.register(Subscription, SubscriptionAdmin)
admin.site.register(Feedback, FeedbackAdmin)
admin.site.register(Permission, PermissionAdmin)
admin.site.register(Role, RoleAdmin)
admin.site.register(ServiceTimetable, ServiceTimetableAdmin)
