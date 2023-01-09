from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

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

    COVER_URLS = {
        'fan': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_fantasy_jzdbyb.jpg',
        'adv': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_adventure_nslq2f.jpg',
        'rom': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_romance_ed8yc8.jpg',
        'dys': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_dystopia_vzvsx7.jpg',
        'mys': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673272296/assets/book_covers/cover_mystery_bxumol.jpg',
        'hor': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673272205/assets/book_covers/cover_horror_pjafgt.jpg',
        'thrill': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_thriller_neqvi9.jpg',
        'hisfic': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673270932/assets/book_covers/cover_hisfic_dkiorh.jpg',
        'scifi': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_scifi_zavbdy.jpg',
        'bio': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269245/assets/book_covers/cover_bio_szb7x2.jpg',
        'cook': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269760/assets/book_covers/cover_cookbook_k8fuqz.jpg',
        'mot': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673269760/assets/book_covers/cover_motivation_tmlbib.jpg',
        'health': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673270018/assets/book_covers/cover_health_lfdgjr.jpg',
        'his': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673270319/assets/book_covers/cover_history_oajjvt.jpg',
        'travel': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673270505/assets/book_covers/cover_travel_ortf8u.jpg',
        'diy': 'https://res.cloudinary.com/dzg7yacrw/image/upload/v1673270719/assets/book_covers/cover_howto_v00rx2.jpg'
    }

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.CharField(max_length=200)
    description = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='+')
    genre = models.CharField(max_length=6, choices=GENRES)
    likes = models.ManyToManyField(User, blank=True, related_name="book_likes")
    # cover_image = 
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

