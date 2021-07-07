from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from core.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2',
                'is_superuser',
                'is_staff',
                'is_active',
            )
        }),)

    fieldsets = (
        (None, {'fields': ('email',
                           'password',)}),

        ('Permissions', {'fields': ('is_staff',
                                    'is_superuser',)}),

        ('Important', {'fields': ('is_active',
                                  'created_at',
                                  'modified_at',)}),
    )

    list_display = [
        'id',
        'email',
        'is_active',
        'is_staff',
        'is_superuser',
    ]

    list_display_links = ['id', 'email']

    readonly_fields = ['created_at', 'modified_at']

    list_filter = ['email']
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()
