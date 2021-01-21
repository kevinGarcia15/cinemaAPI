"""Movies views with views sets"""

#django REST Framework
from rest_framework import viewsets, mixins

#permissions

#Filters

#seralizers
from cinema.movies.serializer.movies import MoviesModelSerializer

#Models
from cinema.movies.models import Movie, Category

class MoviesViewSet(
    viewsets.GenericViewSet,
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin):
    """
    A Movies view Set
    """
    queryset = Movie.objects.all()
    serializer_class = MoviesModelSerializer
    lookup_field = 'title'
