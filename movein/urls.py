from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', index, name="index"),
    path('logout/', LogoutView.as_view(next_page='landlord_login'), name='landlord_logout'),
    
    # OWNER URLS
    path('owner/rooms', l_room, name="landlord_room"),
    path('owner/announcements', l_announcement, name="landlord_announcement"),
    path('owner/bills', l_bills, name="landlord_bills"),
    path('owner/reports', l_reports, name="landlord_reports"),
    path('owner/login', l_login, name="landlord_login"),
    path('owner/register', l_register, name="landlord_register"),

    # TENANT URLS
    path('tenant/myRoom', t_myRoom, name="myRoom"),
    path('tenant/announcements', t_announcement, name="tenant_announcement"),
    path('tenant/login', t_login, name="tenant_login"),
    path('tenant/register', t_register, name="tenant_register"),
    path('tenant/logout/', views.tenant_logout, name='tenant_logout'),
    # path('tenant/reports', t_report, name="tenant_report"),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)