from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views import View
from .form import *

def index(request):
    return render(request, 'movein/index.html')

# Owner Views
def l_room(request):
    context = {
        'active_link': 'rooms',
    }
    return render(request, 'movein/l_roompage.html', context)

def l_announcement(request):
    announcements = Announcements.objects.order_by('-Announce_date')
    
    if request.method == "POST":
        form = announcementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landlord_announcement') 
    else: 
        form = announcementForm()
    
    context = {
        'announcements': announcements,
        'active_link': 'announcements',
        'form': form,
    }
    return render(request, 'movein/l_announcement.html', context)

def announcement_view(request):
    if request.method == "POST":
        form = announcementForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('landlord_announcement') 
    else: 
        form = announcementForm()

    return render(request, 'movein/announcement_create.html', {'form': form} ) 


def l_bills(request):
    context = {
        'active_link': 'bills',
    }

    return render(request, 'movein/l_bills.html', context)

def l_reports(request):
    reports = Reports.objects.all() 
    context = {
        'active_link': 'reports',
        'reports': reports
    }
    return render(request, 'movein/l_reports.html', context)


# Tenant Views
def t_myRoom(request):
    context = {
        'active_link': 'rooms',
    }

    return render(request, 'movein/t_myRoom.html', context)

def t_announcement(request):
    announcements = Announcements.objects.order_by('-Announce_date')
    context = {
        'active_link': 'announcements',
        'announcements': announcements, 
    }

    return render(request, 'movein/t_announcement.html', context)
