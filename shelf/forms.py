from . models import Book, Comment
from django import forms


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'description', 'genre')


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body', )
