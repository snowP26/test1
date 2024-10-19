from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),
    
    # OWNER URLS
    path('owner/rooms', l_room, name="landlord_room"),
    path('owner/announcements', l_announcement, name="landlord_announcement"),
    path('owner/bills', l_bills, name="landlord_bills"),
    path('owner/reports', l_reports, name="landlord_reports"),

    # TENANT URLS
    path('tenant/myRoom', t_myRoom, name="myRoom"),
    path('tenant/announcements', t_announcement, name="tenant_announcement"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)