"""circle serializer"""

#Django Rest Framework
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


#model 
from cinema.movies.models import Movie, Category 

#serializer

class MoviesModelSerializer(serializers.ModelSerializer):
    """
    Movies Model Serializer
    """
     
    class Meta:
        """
        Meta class
        """
        model = Movie
        
        fields = (
            'title', 'year_of_launch',
            'picture', 'language', 'duration',
            'rating', 'trama'
        )

class TotalSaleMoviesModelSerializer(serializers.ModelSerializer):
    """
    Movies Model Serializer
    """
     
    class Meta:
        """
        Meta class
        """
        model = Movie
        
        fields = (
            'title', 'year_of_launch',
            'rating', 'total_sales'
        )


class MovieCreateSerializer(serializers.Serializer):
    """
    Movie created serializer
    """
    title = serializers.CharField(
        min_length=1,
        max_length=50,
        required=True,
        validators=[UniqueValidator(queryset=Movie.objects.all())]
    )
    year_of_launch = serializers.IntegerField(min_value=1990, required=True)
    language = serializers.CharField(
        min_length=1,
        max_length=30,
        required=True
    )
    duration = serializers.IntegerField(min_value=1)
    rating = serializers.IntegerField(min_value=0, max_value=5)
    trama = serializers.CharField(required=False)
    child_price = serializers.IntegerField(min_value=0)
    adult_price = serializers.IntegerField(min_value=0)
    
    def create(self, data):
        """
       Create a movie 
        """
        child_price = data['child_price']
        adult_price = data['adult_price']
        data.pop('child_price')
        data.pop('adult_price')
        movie = Movie.objects.create(**data)
        child_category = Category.objects.create(category='child', price_ticket=child_price, movie=movie)
        adult_category = Category.objects.create(category='adult', price_ticket=adult_price, movie=movie)

        return movie