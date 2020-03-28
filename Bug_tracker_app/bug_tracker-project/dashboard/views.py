from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Account
from dashboard.models import Project

def home(request):
    if request.user.is_authenticated:
        current_user = request.user
<<<<<<< HEAD
        try:
            account = get_object_or_404(Account, email=current_user)
            return render(request, 'dashboard/home.html', {'account': account})
        except:
            auth.logout(request)
            return render(request, 'accounts/login.html', {'error': 'Your profile details are not ready'})
=======
        account = get_object_or_404(Account, email=current_user)
        return render(request, 'dashboard/home.html', {'account':account})
>>>>>>> 86075ae4e5687e75beaa7dec9776be6dbf374cef
    else:
        return redirect('login')

def addproject(request):
    if request.method == "POST":
        project = Project()
        if request.POST["project_name"] and request.POST["editor1"] or request.POST["inputGroupFile01"] and request.POST["inputGroupFile02"] and request.POST["start_date"] and request.POST["dead_line"]:

            project.project_name = request.POST["project_name"]
            project.description = request.POST["editor1"]
            project.project_file = request.POST["inputGroupFile01"]
            project.additional_file = request.POST["inputGroupFile02"]

            startdate = request.POST['start_date']
            formatedStartDate = startdate.strftime("%Y-%m-%d")
            project.date_of_initiation = formatedStartDate

            deadLine = request.POST['start_date']
            formatedDeadLine = deadLine.strftime("%Y-%m-%d")

            project.deadline = formatedDeadLine
            project.save()
        return render(request, 'dashboard/addproject.html')
    else:
        current_user = request.user
        account = get_object_or_404(Account, email=current_user)
        return render(request, 'dashboard/addproject.html', {'account': account})
