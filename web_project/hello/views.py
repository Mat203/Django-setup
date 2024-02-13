from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse, FileResponse

def sayHello(request):
        return HttpResponse("Hello, Djnago!")

def sayBig(request):
        return render(request, "Hello.html")

def set_cookie(request):
        response = HttpResponse("Cookie set!")
        response.set_cookie('my_cookie','Hello from server!')
        return response

def get_cookie(request):
        print(request.META)
        my_cookie_value = request.COOKIES.get('my_cookie','Cookie not set')
        return HttpResponse(f"Value of my cookie:{my_cookie_value}")

def my_websocket(request):
        return HttpResponse("Hello, Djnago!")