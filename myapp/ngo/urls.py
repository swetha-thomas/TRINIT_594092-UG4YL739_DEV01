from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.ngoHome, name="ngoHome"),
   path('search/', views.ngoSearch, name="ngoSearch"),
   path('events/', views.ngoEvent, name="ngoEvent"),

]