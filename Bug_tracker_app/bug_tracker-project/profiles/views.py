from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from accounts.models import Account

# Create your views here.
def profiles(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            try:
                if request.POST['current_password'] is not None:
                    p = True;
            except:
                p = False;
            if p == True:
                    if auth.authenticate(username = request.user, password = request.POST['current_password']):
                        if request.POST['new_password1'] == request.POST['new_password2']:
                            u = User.objects.get(username__exact=request.user)
                            u.set_password(request.POST['new_password1'])
                            u.save()
                            if u.is_superuser:
                                auth.logout(request)
                                return redirect('chlogin')
                            else:
                                auth.logout(request)
                                return redirect('home')
                        else:
                            profile = get_object_or_404(Account, username=request.user)
                            return render(request, 'profiles/profile.html', {'error':'Confirm Password does not match.','profile':profile})
                    else:
                        profile = get_object_or_404(Account, username=request.user)
                        return render(request, 'profiles/profile.html', {'error':'Password does not match.','profile':profile})
            if p == False:
                profile = get_object_or_404(Account, username=request.user)
                if request.POST['first_name'] is not None:
                    profile.first_name = request.POST['first_name']
                if request.POST['last_name'] is not None:
                    profile.last_name = request.POST['last_name']
                if request.POST['age'] is not None:
                    profile.age = request.POST['age']
                if request.POST['mobile'] is not None:
                    profile.mobile = request.POST['mobile']
                if request.POST['job_title'] is not None:
                    profile.job_title = request.POST['job_title']
                if request.POST['email'] is not None:
                    profile.email = request.POST['email']
                try:
                    profile.photo = request.FILES['photo']
                except:
                    pass
                if request.POST['address'] is not None:
                    profile.address = request.POST['address']
                if request.POST['city'] is not None:
                    profile.city = request.POST['city']
                if request.POST['state'] is not None:
                    profile.state = request.POST['state']
                if request.POST['zip'] is not None:
                    profile.zip = request.POST['zip']
                profile.save()
                profile = get_object_or_404(Account, username=request.user)
                return render(request, 'profiles/profile.html', {'profile':profile})
        else:
            profile = get_object_or_404(Account, username=request.user)
            return render(request, 'profiles/profile.html', {'profile':profile})
    else:
        if user.is_superuser:
            return redirect('chlogin')
        else:
            return redirect('login')
