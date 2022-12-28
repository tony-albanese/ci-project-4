from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    GENRES = [
        ('fan', 'Fantasy'),
        ('adv', 'Adventure'),
        ('rom', 'Romance'),
        ('dys', 'Dystopian'),
        ('mys', 'Mystery'),
        ('hor', 'Horror'),
        ('thrill', 'Thriller'),
        ('hisfic', 'Historical Fiction'),
        ('scifi', 'Science Fiction'),
        ('bio', 'Biography'),
        ('cook', 'Cookbook'),
        ('mot', 'Motivational'),
        ('health', 'Health'),
        ('his', 'history'),
        ('travel', 'Travel'),
        ('diy', 'How-to'),
    ]
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    genre = models.CharField(max_length=6, choices=GENRES)
    likes = models.ManyToManyField(User, blank=True)
    comments = models.ForeignKey(Comment, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def number_of_like(self):
        return self.likes.count()


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    written_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['written_on']


class Shelf(models.Model):
    title = models.CharField(max_length=100, default="My Shelf")
    books = models.ForeignKey(Book, on_delete=models.CASCADE)
