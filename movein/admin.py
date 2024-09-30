from django.contrib import admin
from .models import Tenant, Property, Room, Reports, Announcements

# Register your models here.

# Admin access
admin.site.register(Tenant)
admin.site.register(Property)
admin.site.register(Room)
admin.site.register(Reports)
admin.site.register(Announcements)

