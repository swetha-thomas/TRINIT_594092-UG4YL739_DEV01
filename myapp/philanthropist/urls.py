from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   # path('', views.ngoHome, name="ngoHome"),
   path('search/', views.philanthropistSearch, name="philanthropistSearch"),
   path('', views.philanthropistHome, name="philanthropistHome"),
   path('calculate/<str:event_name>/<str:org_name>/<str:user_name>', views.philanthropistCalculate, name="philanthropistCalculate"),
   path('like/<str:org_name>', views.philanthropistLike, name="philanthropistLike"),

   # path('search/', views.philanthropistSearch, name="philanthropistSearch"),
]