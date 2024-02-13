from django.contrib import admin
from django.urls import path
from playground import views

#http://127.0.0.1:8000/playground/cookie/set?title=cookie&value=favorite
#http://127.0.0.1:8000/playground/cookie/get/cookie
#http://127.0.0.1:8000/playground/header/set?title=header&value=one
#http://127.0.0.1:8000/playground/header/get/header
urlpatterns = [
    path('cookie/set', views.set_cookie, name='set_cookie'),
    path('cookie/get/<str:cookie_title>', views.get_cookie, name='get_cookie'),
    path('header/set', views.set_header, name='set_header'),
    path('header/get/<str:title>/', views.get_header, name='get_header'),
]