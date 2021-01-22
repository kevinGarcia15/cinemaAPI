"""Movies URLS"""

#Django
from django.urls import path, include

#django REST framework
from rest_framework.routers import DefaultRouter

#Views
from cinema.movies.views.movies import MoviesViewSet
from cinema.movies.views.movies import CategoryViewSet

router = DefaultRouter()
router.register(r'movies', MoviesViewSet, basename='movies')
router.register(r'categories', CategoryViewSet, basename='categories')
urlpatterns = [
    path('', include(router.urls))
]