from django.shortcuts import render, HttpResponse, redirect
from django.views import generic

# Create your views here.

# Make a function based view just to make sure the wiring will work
# Especially with Heroku

# This method will simply return some HTML


def load_home_page(request):
    if request.user.is_authenticated:
        return render(request, 'index.html')
    else:
        return redirect('accounts/login')