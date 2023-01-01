from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Shelf(models.Model):
    title = models.CharField(max_length=100, default="My Shelf")


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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    genre = models.CharField(max_length=6, choices=GENRES)
    likes = models.ManyToManyField(User, blank=True, related_name="book_likes")
    #shelf = models.ForeignKey(Shelf, on_delete=models.CASCADE, default="My Shelf")

    def __str__(self):
        return self.title

    def number_of_like(self):
        return self.likes.count()
    
    def get_absolute_url(self):
        return reverse("book_detail",  kwargs={"slug": self.slug})


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="comments")
    body = models.TextField()
    written_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['written_on']

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"

