from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=150)

    def __str__(self):
        return self.author_name


class Genre(models.Model):
    genre_name = models.CharField(max_length=70, unique=True)

    def __str__(self):
        return self.genre_name


class LibraryBranch(models.Model):
    branch_address = models.CharField(max_length=250, unique=True)
    is_branch_open = models.BooleanField(default=True)

    def __str__(self):
        return self.branch_address


class Book(models.Model):
    book_name = models.CharField(max_length=200)
    no_of_pages = models.IntegerField()
    is_published = models.BooleanField(default=True)
    author = models.ForeignKey(Author, on_delete=models.RESTRICT)
    genre = models.ForeignKey(Genre, on_delete=models.RESTRICT)
    branch = models.ForeignKey(LibraryBranch, on_delete=models.RESTRICT, related_name='books', null=True)

    def __str__(self):
        return self.book_name



















