"""bookshelf URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from shelf.views import load_home_page, get_books, add_book_form, add_book, delete_book, edit_book, add_comment, view_book_detail, add_comment, add_like, remove_like
from shelf.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', get_books, name='home'),
    path('add_book_form/', add_book_form, name='add_book_form'),
    path('add_book/', add_book, name="add_book"),
    path('delete_book/<book_id>', delete_book, name='delete_book'),
    path('edit_book/<book_id>', edit_book, name='edit_book'),
    path('book_detail/<book_id>', view_book_detail, name='book_detail'),
    path('add_comment/<book_id>', add_comment, name='add_comment'),
    path('like/<book_id>', add_like, name='add_like'),
    path('unlike/<book_id>', remove_like, name='remove_like'),
    path('my_books/', get_my_books, name='my_books'),
    path('favorites/', get_favorites, name='favorites'),
    path('books_by_owner/<owner_id>', books_by_owner, name='books_by_owner'),
    path('search/', perform_search, name='perform_search'),
    path('delete_comment/<comment_id>', delete_comment, name='delete_comment'),
    path('update_comment/<comment_id>', update_comment, name='update_comment'),
]
