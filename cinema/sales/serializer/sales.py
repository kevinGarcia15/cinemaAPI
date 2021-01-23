"""Sales serializer"""

#Django Rest Framework
from rest_framework import serializers

#model 
from cinema.sales.models import Sales
from cinema.movies.models import Movie, Category
from cinema.users.models import User

#serializer
from cinema.movies.serializer import MoviesModelSerializer, CategoryModelSerializer
from cinema.users.serilizer import UserModelSerializer


class SalesModelSerializer(serializers.ModelSerializer):
    """
    Sales model serializer
    """
    category = CategoryModelSerializer(read_only=True)
    client = UserModelSerializer(read_only=True)
    lookup_field = 'id'  

    class Meta:
        """
        Meta class
        """
        model = Sales
        fields = (
            'category',
            'client',
            'schedule',
            'room', 'quantity', 
            'created'
        )

class SalesCreateSerializer(serializers.Serializer):
    """Create a sale custom"""
    movie_title = serializers.CharField(
        min_length=1,
        max_length=50,
        required=True
    )
    category_tipe = serializers.CharField(
        min_length=1,
        max_length=50,
        required=True
    )
    quantity = serializers.IntegerField(min_value=1)
    room = serializers.CharField(
        min_length=1,
        max_length=30,
        required=True
    )
    schedule = serializers.TimeField(format="%H:%M:%S")   

    def validate(self, data):
        """Verifi if exist the movie and category"""
        try:
            movie = Movie.objects.get(title=data['movie_title'])
            category = Category.objects.get(movie=movie, category=data['category_tipe'])
        except:
            raise serializers.ValidationError('The movie or categorie does\'t exist')
        return data

