from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
# Create your views here.


def chlogin(request):
    return render(request, 'company_head/chlogin.html')


def dashboard(request):
    return render(request, 'company_head/dashhead.html')


def addemployee(request):
    return render(request, 'company_head/addEmployee.html')


def manageemployes(request):
    return render(request, 'company_head/manageEmployes.html')


def chlogout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('chlogin')
