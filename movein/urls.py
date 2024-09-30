from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name="index"),
    
    # OWNER URLS
    path('owner/rooms', l_room, name="tenant_room"),
    path('owner/announcements', l_announcement, name="landlord_announcement"),
    path('owner/announcements/create', announcement_view, name="createAnnouncement"),
    path('owner/bills', l_bills, name="landlord_bills"),

    # TENANT URLS
    path('tenant/myRoom', t_myRoom, name="myRoom"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)