from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = (
        'email',
        'first_name',
        'last_name',
    )
    list_filter = (
        'email',
    )
    search_fields = (
        'email',
    )