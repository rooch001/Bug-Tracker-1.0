from django.shortcuts import render, redirect

# Create your views here.
def chlogin(request):
    return render(request, 'company_head/chlogin.html')
