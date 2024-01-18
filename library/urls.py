from django.urls import include, path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('books', views.BookViewset, basename='books')
router.register('author', views.AuthorViewset, basename='author')
router.register('genre', views.GenreViewset, basename='genre')
router.register('library_branch', views.LibraryBranchViewset, basename='library_branch')


urlpatterns = [
    path('api/', include(router.urls))
]