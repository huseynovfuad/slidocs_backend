from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from accounts.models import User


class UserAdmin(BaseUserAdmin):
    list_display = ("email", "name", "surname", "code", "is_active", "is_staff", "is_superuser")
    fieldsets = (
        (
            None,
            {
                "fields": (
                    "email",
                    "name",
                    "surname",
                    "code",
                    "password",
                )
            },
        ),
        (
            "Permissions",
            {"fields": ("is_active", "is_staff", "is_superuser", "user_permissions")},
        ),
        ("Groups", {"fields": ("groups",)}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "name",
                    "surname",
                    "password1",
                    "password2",
                ),
            },
        ),
    )
    exclude = ("date_joined",)
    search_fields = ("email", "name", "surname")
    ordering = ("email", "name", "surname")
    filter_horizontal = ()


admin.site.register(User, UserAdmin)