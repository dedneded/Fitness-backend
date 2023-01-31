from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import *
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


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone',)
    ordering = ('phone',)

    add_fieldsets = (
        (None, {
            'fields': (
                'phone', 'first_name', 'last_name', 'password1', 'password2', 'groups', 'is_superuser', 'is_staff'
            )
        }),
    )

    fieldsets = (
        (None, {
            "fields": (
                'phone', 'first_name', 'last_name', 'password', 'groups', 'is_superuser', 'is_staff'
            )
        }),
    )

class ClientSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('client',)
    list_display_links = ('client',)


admin.site.register(ClientSubscription, ClientSubscriptionAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
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
