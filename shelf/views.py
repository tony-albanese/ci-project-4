from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.template import loader
from django.contrib import messages
from django.template.defaultfilters import slugify
from .models import Book

from .forms import BookForm, CommentForm

# Create your views here.


def load_home_page(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('accounts/login')


def get_books(request):
    books = Book.objects.all()
    liked_books = []
    for book in books:
        book.genre = book.get_genre_display()
        if book.likes.filter(id=request.user.id).exists():
            liked_books.append(book.id)

    template = loader.get_template('index.html')
    context = {
        'books': books,
        'liked_books': liked_books
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
    # TODO Add validity check
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        description = request.POST.get('description')
        genre = request.POST.get('genre')
        slug = slugify(title)
        Book.objects.create(title=title, author=author, description=description,
                            genre=genre, owner=request.user, slug=slug)
        messages.success(request, "Successfully added your book.")
    return redirect('/')


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    # TODO add validity check
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        form.save()
        updated_book = get_object_or_404(Book, id=book_id)
        updated_book.slug = slugify(book.title)
        updated_book.save()
        messages.success(request, "Successfully updated your book.")
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


def add_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
        comment_form.instance.author = request.user
        comment_form.instance.book = book
        comment_form.save()
        messages.success(request, "Successfully added comment.")
    else:
        messages.error(request, "Something went wrong.")
        comment_form = CommentForm()
    
    comments = book.comments.order_by("-written_on")
    context = {
        'comment_form': CommentForm(),
        'book': book,
        'comments': comments
    }
    return render(request, 'book_detail_template.html', context)


def view_book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comments = book.comments.order_by("-written_on")
    template = loader.get_template('book_detail_template.html')
    form = CommentForm()
    context = {
        'comment_form': form,
        'book': book,
        'comments': comments
    }

    return HttpResponse(template.render(context, request))


def add_like(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.likes.add(request.user)
    return redirect('/')


def remove_like(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.likes.remove(request.user)
    return redirect('/')
 