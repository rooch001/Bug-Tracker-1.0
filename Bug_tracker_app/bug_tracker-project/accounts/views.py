from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Account

# Create your views here.


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            current_user = request.user
            try:
                account = get_object_or_404(Account, username=current_user)
                return redirect('home')
            except:
                auth.logout(request)
                return render(request, 'accounts/login.html', {'error': 'Your profile details are not ready'})
        else:
            return render(request, 'accounts/login.html', {'error': 'Email or Password is not correct'})
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
