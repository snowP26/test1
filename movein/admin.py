from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Property, Room, Reports, Announcements

# Define a custom UserAdmin
class CustomUserAdmin(BaseUserAdmin):
    model = User
    list_display = ('email', 'username', 'role', 'is_staff', 'is_active')  # Use 'role' instead of 'user_type'
    list_filter = ('role', 'is_staff', 'is_active')  # Use 'role' instead of 'user_type'
    fieldsets = BaseUserAdmin.fieldsets + (
        (None, {'fields': ('role',)}),  # Ensure this matches your model field
    )
    add_fieldsets = BaseUserAdmin.add_fieldsets + (
        (None, {'fields': ('role',)}),
    )

# Register your models here.
admin.site.register(Property)
admin.site.register(Room)
admin.site.register(Reports)
admin.site.register(Announcements)
admin.site.register(User, CustomUserAdmin)  # Register your custom UserAdmin    