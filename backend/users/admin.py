from django.contrib import admin
from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Follow


class CustomUserAdmin(UserAdmin):
    list_display = ['email', 'username', ]
    list_filter = ['email', 'username', ]


@register(Follow)
class FollowAdmin(admin.ModelAdmin):
    autocomplete_fields = ('author', 'user')


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
