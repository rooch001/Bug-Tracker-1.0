from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Account

# Create your views here.
def profiles(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            profile = get_object_or_404(Account, email=request.user)
            if request.POST['first_name']:
                profile.first_name = request.post['first_name']
            if request.POST['last_name']:
                profile.last_name = request.post['last_name']
            if request.POST['age']:
                profile.age = request.post['age']
            if request.POST['mobile']:
                profile.mobile = request.post['mobile']
            if request.POST['job_title']:
                profile.job_title = request.post['job_title']
            if request.FILES['photo']:
                profile.photo = request.post['photo']
            if request.FILES['address']:
                profile.address = request.post['address']
            profile.save()
        else:
            return render(request, 'profiles/profile.html')
    else:
        return redirect('chlogin')
