from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.views import View
from .form import *
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt 


class LogoutView(BaseLogoutView):
    @method_decorator(csrf_exempt)  
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

def index(request):
    return render(request, 'movein/index.html')

# Owner Views
def l_register(request):
    if request.method == "POST":
        form = ownerRegForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            if User.objects.filter(username=email).exists():  
                messages.error(request, "Email already exists.")
                return render(request, 'movein/l_registerpage.html', {'form': form})

            
            user = form.save(commit=False)
            user.username = email  
            user.set_password(password)  
            user.save()
            login(request, user)  
            return redirect('landlord_room')  

    else:
        form = ownerRegForm()

    return render(request, 'movein/l_registerpage.html', {'form': form})


def l_login(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("email") 
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == 'landlord':
                login(request, user)    
                return redirect('landlord_room')
            else:
                messages.error(request, "You do not have permission to access the landlord page.")
                return redirect('landlord_login')
        else:
            messages.error(request, "Username or password is invalid.")

    return render(request, 'movein/l_loginpage.html', {'error': error_message})

@login_required(login_url='owner/login')
def l_room(request):
    context = {
        'active_link': 'rooms',
    }

    return render(request, 'movein/l_roompage.html', context)


@login_required(login_url='owner/login')
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


@login_required(login_url='owner/login')
def l_bills(request):
    context = {
        'active_link': 'bills',
    }

    return render(request, 'movein/l_bills.html', context)

@login_required(login_url='owner/login')
def l_reports(request):
    reports = Reports.objects.all() 
    context = {
        'active_link': 'reports',
        'reports': reports
    }
    return render(request, 'movein/l_reports.html', context)


# Tenant Views

@login_required(login_url='tenant/login')
def t_myRoom(request):
    context = {
        'active_link': 'rooms',
    }

    return render(request, 'movein/t_myRoom.html', context)

@login_required(login_url='tenant/login')
def t_announcement(request):
    announcements = Announcements.objects.order_by('-Announce_date')
    context = {
        'active_link': 'announcements',
        'announcements': announcements, 
    }

    return render(request, 'movein/t_announcement.html', context)

@login_required(login_url='tenant/login')
def t_report(request):
    reports = Reports.objects.order_by('Reports_date')
    context = {
        'active_link': 'reports',
        'reports': reports,
    }

    return render(request, 'movein/t_reports.html', context)

def t_login(request):
    error_message = None
    if request.method == "POST":
        username = request.POST.get("email") 
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.role == 'tenant':
                login(request, user)
                return redirect('myRoom')
            else:
                messages.errror(request, "Trying to log in as a tenant? Continue here.")
                return redirect('tenant_login')
        else:
            messages.error(request, "Username or password is invalid.")

    return render(request, 'movein/t_loginpage.html')

def t_register(request):
    if request.method == "POST":
        form = userRegForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            
            if User.objects.filter(username=email).exists():
                messages.error(request, "Email already exists.")
                return render(request, 'movein/t_registerpage.html', {'form': form})

            user = form.save(commit=False)
            user.username = email
            user.set_password(password)
            user.save()
            login(request, user)
            return redirect('myRoom')
        
    else:
        form = userRegForm()


    return render(request, 'movein/t_registerpage.html', {'form': form})



def tenant_logout(request):
    logout(request)
    return redirect('tenant_login')