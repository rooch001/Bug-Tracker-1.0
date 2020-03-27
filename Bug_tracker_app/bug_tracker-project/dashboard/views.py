from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.models import User


def home(request):
    if request.user.is_authenticated:
        return render(request, 'dashboard/home.html')
    else:
        return redirect('login')


def addproject(request):
    return render(request, 'dashboard/addproject.html')
