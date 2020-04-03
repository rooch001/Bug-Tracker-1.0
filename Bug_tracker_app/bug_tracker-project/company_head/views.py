from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth
from django.contrib.auth.models import User
from accounts.models import Account
from django.http import JsonResponse
from django.views.generic import View
from django.views.generic import ListView
# Create your views here.


def chlogin(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['password'])
        if user is not None and user.is_superuser:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'company_head/chlogin.html', {"error": "Username or Password is not correct"})
    else:
        if request.user.is_authenticated:
            return redirect('dashboard')
        else:
            return render(request, 'company_head/chlogin.html')


def dashboard(request):
    if request.user.is_authenticated:
        try:
            account = get_object_or_404(Account, username=request.user)
            print(account.username)
            return render(request, 'company_head/dashhead.html', {'account': account})
        except:
            auth.logout(request)
            return render(request, 'company_head/chlogin.html', {'error': 'Your profile details are not ready'})
    else:
        return redirect('chlogin')


def addemployee(request):
    return render(request, 'company_head/addEmployee.html')


def manageemployes(request):
    return render(request, 'company_head/manageEmployee/manageEmployes.html')


def chlogout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('chlogin')


class employeeView(ListView):
    model = Account
    template_name = 'company_head/manageEmployee/manageEmployes.html'
    context_object_name = 'users'


class createEmployee(View):
    def get(self, request):
        emp_id1 = request.GET.get('emp_id', None)
        first_name1 = request.GET.get('first_name', None)
        last_name1 = request.GET.get('last_name', None)
        age1 = request.GET.get('age', None)
        mobile1 = request.GET.get('mobile', None)
        job_title1 = request.GET.get('job_title', None)
        email1 = request.GET.get('email', None)
        address1 = request.GET.get('address', None)
        city1 = request.GET.get('city', None)
        state1 = request.GET.get('state', None)
        zip1 = request.GET.get('zip', None)

        obj = Account.objects.create(
            emp_id=emp_id1,
            first_name=first_name1,
            last_name=last_name1,
            age=age1,
            mobile=mobile1,
            job_title=job_title1,
            email=email1,
            address=address1,
            city=city1,
            state=state1,
            zip=zip1
        )
        user = {'id': obj.emp_id,
                'firstname': obj.first_name,
                'lastname': obj.last_name,
                'age': obj.age,
                'mobile': obj.mobile,
                'jobtitle': obj.job_title,
                'email': obj.email,
                'address': obj.address,
                'city': obj.city,
                'state': obj.state,
                'zip': obj.zip,
                }

        data = {
            'user': user
        }
        return JsonResponse(data)


class updateEmployee(View):
    def get(self, request):
        emp_id1 = request.GET.get('emp_id', None)
        first_name1 = request.GET.get('first_name', None)
        last_name1 = request.GET.get('last_name', None)
        age1 = request.GET.get('age', None)
        mobile1 = request.GET.get('mobile', None)
        job_title1 = request.GET.get('job_title', None)
        email1 = request.GET.get('email', None)
        address1 = request.GET.get('address', None)
        city1 = request.GET.get('city', None)
        state1 = request.GET.get('state', None)
        zip1 = request.GET.get('zip', None)

        obj = Account.objects.create(
            emp_id=emp_id1,
            first_name=first_name1,
            last_name=last_name1,
            age=age1,
            mobile=mobile1,
            job_title=job_title1,
            email=email1,
            address=address1,
            city=city1,
            state=state1,
            zip=zip1
        )
        user = {'id': obj.emp_id,
                'firstname': obj.first_name,
                'lastname': obj.last_name,
                'age': obj.age,
                'mobile': obj.mobile,
                'jobtitle': obj.job_title,
                'email': obj.email,
                'address': obj.address,
                'city': obj.city,
                'state': obj.state,
                'zip': obj.zip,
                }
        data = {
            'user': user
        }
        return JsonResponse(data)


class deleteEmployee(View):
    def get(self, request):
        id1 = request.GET.get('emp_id', None)
        Account.objects.get(emp_id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)
