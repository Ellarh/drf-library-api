from .models import Book, Genre, Author
from .serializer import BookSerializer, AuthorSerializer, GenreSerializer
from rest_framework import viewsets
from rest_framework import filters


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['book_name', 'author__author_name', 'genre__genre_name']


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
