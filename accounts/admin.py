from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import User, OTP

class UserAdmin(BaseUserAdmin):
    ordering = ['id']
    list_display = ['id','email', 'fname','lname']
    # list_filter = ('User__is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (('Personal Info'), {'fields': ('fname','lname',)}),
        (
            ('Permissions'),
            {'fields': ('is_active','is_staff', 'is_superuser',)}
        ),
        (('Important dates'), {'fields': ('last_login',)})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

admin.site.register(User, UserAdmin)
# admin.site.register(OTP)