"""Sales views."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from cinema.sales.serializer import SalesModelSerializer,SalesCreateSerializer
from cinema.movies.serializer import MoviesModelSerializer,TotalSaleMoviesModelSerializer
# Filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from cinema.sales.models import Sales
from cinema.movies.models import Movie,Category
# Utilities

class SalesViewSet(mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,                                                                                                                                                                                                                                                                                                                      
                mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    """Sales view set."""

    serializer_class = SalesModelSerializer
    queryset = Sales.objects.all() 
    
    def get_permissions(self):
        """
        Asign permisions based on actions
        """
        permissions = [IsAuthenticated]
        return [permission() for permission in permissions]

    def create(self, request):
        """
        Create a Sale ticket

        the user can buy a ticket for watch a movie
        """
        serializer = SalesCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        movie = Movie.objects.get(title=request.data['movie_title'])
        category = Category.objects.get(movie=movie, category=request.data['category_tipe'])
        sales = Sales.objects.create(
            client=request.user, 
            category=category, 
            quantity=request.data['quantity'],
            room=request.data['room'],
            schedule=request.data['schedule'] 
        )

        #adds what has total_sales to quantity and saves it in partial_sales, 
        #then assigns it back to total_sales
        partial_sales = movie.total_sales+request.data['quantity']
        movie.total_sales = partial_sales
        movie.save()
        data = SalesModelSerializer(sales).data

        return Response(data, status=status.HTTP_201_CREATED)  

class ReportersViewSet(viewsets.GenericViewSet,mixins.ListModelMixin):
    """reporters like total movies, avg child and adults"""

    serializer_class = TotalSaleMoviesModelSerializer
    queryset = Movie.objects.all()
