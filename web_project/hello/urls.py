from django.contrib import admin
from django.urls import path
from hello import viewsNode
from hello import views

urlpatterns = [
    path('hello/', views.sayHello),
    path('set_cookie/', views.set_cookie),
    path('get_cookie/', views.get_cookie),
    path("node/post", viewsNode.get_node_view_with_post),
    path("node/rceive", viewsNode.parse_node_req_view)
]