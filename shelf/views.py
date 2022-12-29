from django.shortcuts import render, HttpResponse, redirect
from django.views import generic
from django.template import loader
from . models import Book

# Create your views here.

# Make a function based view just to make sure the wiring will work
# Especially with Heroku

# This method will simply return some HTML


def load_home_page(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('accounts/login')


def get_books(request):
    books = Book.objects.all()
    for book in books:
        book.genre = book.get_genre_display()
    template = loader.get_template('index.html')
    context = {
        'books': books,
    }
    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('accounts/login')