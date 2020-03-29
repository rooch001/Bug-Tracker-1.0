from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Account
from dashboard.models import Project

def home(request):
    if request.user.is_authenticated:
        try:
            current_user = request.user
            account = get_object_or_404(Account, email=current_user)
            return render(request, 'dashboard/home.html', {'account': account})
        except:
            auth.logout(request)
            return render(request, 'accounts/login.html', {'error':'Your profile details are not ready'})
    else:
        return redirect('login')

def addproject(request):
    current_user = request.user
    account = get_object_or_404(Account, email=current_user)
    if request.method == "POST":
        project = Project()
        project.project_name = request.POST["project_name"]
        project.description = request.POST["editor1"]
        project.project_file = request.FILES["projectFile"]
        try:
            project.additional_file = request.FILES["additionalFile"]
        except:
            project.additional_file = None
        project.date_of_initiation = request.POST['start_date']
        project.deadline = request.POST['dead_line']
        project.save()
        return render(request, 'dashboard/addproject.html', {'account': account,'project':project})
    else:
        current_user = request.user
        account = get_object_or_404(Account, email=current_user)
        return render(request, 'dashboard/addproject.html', {'account': account})
