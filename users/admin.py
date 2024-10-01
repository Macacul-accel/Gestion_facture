from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Info perso'), {'fields': ('first_name', 'phone_number')}),
        (_('Permissions'), {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_filter = ('email', 'first_name', 'phone_number','is_staff', 'is_active',)
    list_display = ('email', 'first_name', 'phone_number', 'is_staff', 'is_active',)
    search_fields = ('email',)
    ordering = ('email',)
