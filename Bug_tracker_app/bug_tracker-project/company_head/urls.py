from django.urls import path, include
from . import views

urlpatterns = [
    path('chlogin', views.chlogin, name='chlogin'),
]
