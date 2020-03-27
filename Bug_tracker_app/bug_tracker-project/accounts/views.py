from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['email'],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html',{'error':'Email or Password is not correct'})
    else:
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('login')
