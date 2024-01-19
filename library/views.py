from .models import Book, Genre, Author, LibraryBranch
from .serializer import BookSerializer, AuthorSerializer, GenreSerializer, LibraryBranchSerializer
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


class BookViewset(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['book_name', 'author__author_name', 'genre__genre_name', 'branch__branch_address']


class AuthorViewset(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class GenreViewset(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


class LibraryBranchViewset(viewsets.ModelViewSet):
    serializer_class = LibraryBranchSerializer
    queryset = LibraryBranch.objects.all()


