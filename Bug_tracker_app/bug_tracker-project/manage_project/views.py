from django.shortcuts import render

# Create your views here.
def projectDetails(request):
    return render(request, 'projects.html')
