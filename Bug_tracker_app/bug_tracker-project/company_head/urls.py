from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.chlogin, name='chlogin'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('addemployee', views.addemployee, name='addemployee'),
    path('chlogout', views.chlogout, name='chlogout'),
    # path('manageEmployes/create',
    #      views.createEmployee.as_view(), name='createEmployee'),
    # path('manageEmployes/update',
    #      views.updateEmployee.as_view(), name='updateEmployee'),
    # path('manageEmployes/delete',
    #      views.deleteEmployee.as_view(), name='deleteEmployee'),
]
