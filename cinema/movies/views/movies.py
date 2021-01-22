"""Movies views with views sets"""

#django REST Framework
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

#permissions
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser

#Filters

#seralizers
from cinema.movies.serializer.movies import MoviesModelSerializer,MovieCreateSerializer
from cinema.movies.serializer.category import CategoryModelSerializer

#Models
from cinema.movies.models import Movie, Category

class MoviesViewSet(
    viewsets.GenericViewSet,
    mixins.UpdateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.DestroyModelMixin):
    """
    A Movies view Set
    """
    queryset = Movie.objects.all()
    serializer_class = MoviesModelSerializer
    lookup_field = 'title'


    def get_permissions(self):
        """
        Asign permisions based on actions
        """
        permissions = [AllowAny]
        if self.action in ['update', 'partial_update','delete', 'create']:
            permissions = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permissions]

    def create(self, request):
        """
        Create a movie
        """
        serializer = MovieCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        movie = serializer.save()
        data = MoviesModelSerializer(movie).data

        return Response(data, status=status.HTTP_201_CREATED)

class CategoryViewSet(viewsets.GenericViewSet,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin
                ):
    """
    A class views of category, we can make CRUD with categories.
    """
    queryset = Category.objects.all()
    serializer_class = CategoryModelSerializer
    lookup_field = 'category'  

    def get_permissions(self):
        """
        Asign permisions based on actions
        """
        permissions = [IsAdminUser, IsAuthenticated]
        return [permission() for permission in permissions]