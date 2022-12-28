from django.shortcuts import render, HttpResponse
from django.views import generic

# Create your views here.

# Make a function based view just to make sure the wiring will work
# Especially with Heroku

# This method will simply return some HTML


def hello_bookshelf(request):
    return HttpResponse("<h1>Hello</h1><p>This is from HttpResponse pure.</p>")


def hello_bookshelf_template(request):
    return render(request, "hello_template.html")