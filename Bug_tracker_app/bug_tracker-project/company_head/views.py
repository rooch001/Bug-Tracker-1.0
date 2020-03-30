from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import Account
# Create your views here.


def chlogin(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_superuser:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'company_head/chlogin.html', {"error":"Username or Password is not correct"})
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'company_head/chlogin.html')

def dashboard(request):
    if request.user.is_authenticated:
        current_user = request.user
        try:
            account = get_object_or_404(Account, email=current_user)
            return render(request, 'company_head/dashhead.html', {'account': account})
        except:
            auth.logout(request)
            return render(request, 'company_head/chlogin.html', {'error':'Your profile details are not ready'})
    else:
        return redirect('chlogin')

def addemployee(request):
    return render(request, 'company_head/addEmployee.html')

def manageemployes(request):
    return render(request, 'company_head/manageEmployes.html')

def chlogout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('chlogin')
