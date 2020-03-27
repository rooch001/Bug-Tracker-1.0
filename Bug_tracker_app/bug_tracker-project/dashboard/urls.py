from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('addproject.html', views.addproject, name='addproject'),
]
