from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chlogin, name='chlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('manageemployes', views.manageemployes, name='manageemployes'),
    path('chlogout', views.chlogout, name='chlogout'),

]
