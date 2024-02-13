from django.shortcuts import render
from django.http import JsonResponse
from .data.books_data import BOOKS
from django.templatetags.static import static
from django.http import JsonResponse, HttpResponse, Http404
from django.views.decorators.csrf import csrf_exempt
import json

def get_books(request):
    books_with_images = []
    for book in BOOKS:
        book_copy = book.copy()
        book_copy['image'] = request.build_absolute_uri(static(f'playground/static/{book["image"]}'))
        books_with_images.append(book_copy)
    return render(request, 'books.html', {'books': books_with_images})

@csrf_exempt
def delete_book(request, id):
    global BOOKS
    BOOKS = [book for book in BOOKS if book['id'] != id]
    return HttpResponse(status=204)

def get_book(request, id):
    try:
        book = next(book for book in BOOKS if book['id'] == id)
        book_copy = book.copy()
        book_copy['image'] = request.build_absolute_uri(static(f'playground/data/{book["image"]}'))
        return render(request, 'book_profile.html', {'book': book_copy})
    except StopIteration:
        raise Http404("Book not found")
    
@csrf_exempt
def add_book(request, title, author, published_year, image):
    if request.method == 'POST':
        data = {
            'id': max(book['id'] for book in BOOKS) + 1,  
            'title': title,
            'author': author,
            'published_year': int(published_year),
            'image': image
        }
        BOOKS.append(data)
        return JsonResponse(data, status=201)
    else:
        return HttpResponse(status=405)
    
def index(request):
    return render(request, 'index.html')