from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Account
from dashboard.models import Project
# Create your views here.


def project(request):
    if request.user.is_authenticated:
        try:
            current_user = request.user
            account = get_object_or_404(Account, email=current_user)
            return render(request, 'projects.html', {'account': account, 'project': Project})
        except:
            auth.logout(request)
            return render(request, 'accounts/login.html', {'error': 'Your profile details are not ready'})
    else:
        return redirect('login')
