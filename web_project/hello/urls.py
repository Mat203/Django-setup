from django.contrib import admin
from django.urls import path
from hello import views

urlpatterns = [
    path('hello/', views.sayHello),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
]