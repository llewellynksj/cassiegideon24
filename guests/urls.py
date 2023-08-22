from django.urls import path
from . import views

urlpatterns = [
    path('', views.DisplayHome, name='home'),
    path('', views.DisplayContact, name='contact'),
]
