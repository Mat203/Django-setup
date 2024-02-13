from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, FileResponse

def set_cookie(request):
    cookie_title = request.GET.get('title')
    cookie_value = request.GET.get('value')
    http_only = request.GET.get('http_only', False)
    response = JsonResponse({"status": "Cookie set!", "title": cookie_title, "value": cookie_value})
    response.set_cookie(cookie_title, cookie_value, httponly=http_only)
    return response

def get_cookie(request, cookie_title):
    cookie_value = request.COOKIES.get(cookie_title, 'Cookie not found')
    return JsonResponse({"title": cookie_title, "value": cookie_value})

def set_header(request):
   response = HttpResponse("Headers", content_type="text/plain")
   response['X-Custom-Header'] = 'Custom Value'
   return response


def get_header(request, title):
    allheaders = request.META
    my_header_value = allheaders.get('HTTP_' + title.upper(), 'Header not set')
    return HttpResponse(my_header_value)