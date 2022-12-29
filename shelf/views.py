from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic
from django.template import loader

from django.template.defaultfilters import slugify
from .models import Book

from .forms import BookForm

# Create your views here.


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


def add_book_form(request):
    if request.user.is_authenticated:
        book_form = BookForm()
        context = {
            'form': book_form
        }
        template = loader.get_template('add_book_template.html')
        return HttpResponse(template.render(context, request))
    else:
        return redirect('accounts/login')


def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        slug = slugify(title)
        Book.objects.create(title=title, author=author, description=description,
                            genre=genre, owner=request.user, slug=slug)
    return redirect('/')


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        form.save()
        return redirect('/')

    form = BookForm(instance=book)
    context = {
        'form': form
    }

    return render(request, 'edit_book_template.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    return redirect('/')
