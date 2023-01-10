from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from django.views import generic, View
from django.template import loader
from django.contrib import messages
from django.template.defaultfilters import slugify
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
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
        if book.likes.filter(id=request.user.id).exists():
            liked_books.append(book.id)

    page = request.GET.get('page', 1)
    paginator = Paginator(books, 6)

    try:
        paginated_books = paginator.page(page)
    except PageNotAnInteger:
        paginated_books = paginator.page(1)
    except EmptyPage:
        paginated_books = paginator.page(paginator.num_pages)

    template = loader.get_template('index.html')
    context = {
        'books': paginated_books,
        'liked_books': liked_books,
        'genres': Book.GENRES,
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

        book_form = BookForm(data=request.POST)
        if book_form.is_valid():
            title = request.POST.get('title')
            author = request.POST.get('author')
            description = request.POST.get('description')
            genre = request.POST.get('genre')
            slug = slugify(title)
            image_url = Book.COVER_URLS.get(genre)
            Book.objects.create(title=title, author=author, description=description,
                            genre=genre, owner=request.user, slug=slug, image_url=image_url)
            messages.info(request, "Successfully added your book.")
            return redirect('/')
        else:
            messages.error(request, "Woops. Something went wrong. Could not save your book.")
            context = {
                'form': book_form
            }
            return render(request, 'add_book_template.html', context)


def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            updated_book = get_object_or_404(Book, id=book_id)
            updated_book.slug = slugify(book.title)
            updated_book.image_url = Book.COVER_URLS.get(updated_book.genre)
            updated_book.save()
            messages.info(request, "Successfully updated your book.")
            return redirect('/')
        else:
            messages.error(request, "Woops. Something went wrong.")
    form = BookForm(instance=book)
    context = {
        'form': form
    }

    return render(request, 'edit_book_template.html', context)


def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    book.delete()
    messages.info(request, "Book succssfully deleted.")
    return redirect('/')


def add_comment(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    comment_form = CommentForm(data=request.POST)

    if comment_form.is_valid():
        comment_form.instance.author = request.user
        comment_form.instance.book = book
        comment_form.save()
        messages.info(request, "You have added a comment.")
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
 

def get_my_books(request):

    books = Book.objects.filter(owner=request.user)
    liked_books = []
    for book in books:
        if book.likes.filter(id=request.user.id).exists():
            liked_books.append(book.id)

    template = loader.get_template('index.html')
    context = {
        'books': books,
        'liked_books': liked_books,
        'heading_label': 'My Books',
        'genres': Book.GENRES
    }

    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('accounts/login')


def get_favorites(request):
    books = Book.objects.filter(likes__id=request.user.id)

    liked_books = []
    for book in books:
        liked_books.append(book.id)

    template = loader.get_template('index.html')
    context = {
        'books': books,
        'liked_books': liked_books,
        'heading_label': 'My Favorites',
        'genres': Book.GENRES
    }

    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('accounts/login')


def books_by_owner(request, owner_id):
    books = Book.objects.filter(owner__id=owner_id)
    owner = User.objects.get(id=owner_id)

    print(owner.username)
    
    liked_books = []
    for book in books:
        if book.likes.filter(id=request.user.id).exists():
            liked_books.append(book.id)

    template = loader.get_template('index.html')
    heading = f'{owner.username}\'s Books'
    context = {
        'books': books,
        'liked_books': liked_books,
        'heading_label': heading,
        'genres': Book.GENRES
    }

    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('accounts/login')


def perform_search(request):
    list = request.POST.getlist('genres')
    genre_query = Q()
    author_query = Q()
    title_query = Q()
    description_query = Q()

    liked_books = []

    for gen in list:
        genre_query = genre_query | Q(genre__iexact=gen)
    
    title_search_terms = request.POST['title-search-input']
    author_search_terms = request.POST['author-search-input']
    description_search_terms = request.POST['description-search-input']

    if title_search_terms:
        terms = title_search_terms.split()
        for term in terms:
            title_query = title_query | Q(title__icontains=term)
        print(title_query)

    if author_search_terms:
        terms = author_search_terms.split()
        for term in terms:
            author_query = author_query | Q(author__icontains=term)

    if description_search_terms:
        terms = description_search_terms.split()
        for term in terms:
            description_query = description_query | Q(description__icontains=term)
    
    books = Book.objects.filter(author_query, title_query, genre_query, description_query)
    for book in books:
        if book.likes.filter(id=request.user.id).exists():
            liked_books.append(book.id)

    template = loader.get_template('index.html')
    context = {
        'books': books,
        'liked_books': liked_books,
        'heading_label': 'Search Result',
        'genres': Book.GENRES
    }

    if request.user.is_authenticated:
        return HttpResponse(template.render(context, request))
    else:
        return redirect('accounts/login')