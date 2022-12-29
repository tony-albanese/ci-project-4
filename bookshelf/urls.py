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
from shelf.views import load_home_page, get_books, add_book_form, add_book, delete_book, edit_book

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('', get_books, name='home'),
    path('add_book_form/', add_book_form, name='add_book_form'),
    path('add_book/', add_book, name="add_book"),
    path('delete_book/<book_id>', delete_book, name='delete_book'),
    path('edit_book/<book_id>', edit_book, name='edit_book')


]
