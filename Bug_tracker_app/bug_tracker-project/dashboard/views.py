from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import Account


def home(request):
    if request.user.is_authenticated:
        current_user = request.user
        try:
            account = get_object_or_404(Account, email=current_user)
            return render(request, 'dashboard/home.html', {'account':account})
        except:
            auth.logout(request)
            return render(request, 'accounts/login.html', {'error':'Your Profile Details are not ready'})
    else:
        return redirect('login')


def addproject(request):
    return render(request, 'dashboard/addproject.html')
