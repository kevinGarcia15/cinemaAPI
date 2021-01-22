"""circle serializer"""

#Django Rest Framework
from rest_framework import serializers

#model 
from cinema.movies.models import Movie, Category 

#serializer
from cinema.movies.serializer.category import CategoryModelSerializer

class MoviesModelSerializer(serializers.ModelSerializer):
    """
    Movies Model Serializer
    """

    category = CategoryModelSerializer(read_only=True)
    class Meta:
        """
        Meta class
        """
        model = Movie
        
        fields = (
            'title', 'year_of_launch',
            'picture', 'language', 'duration',
            'rating', 'trama','category'
        )

class MovieCreateSerializer(serializers.Serializer):
    """
    Movie created serializer
    """
    title = serializers.CharField(
        min_length=1,
        max_length=50,
        required=True
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
    category = serializers.CharField(
        min_length=1,
        max_length=20
    )

    def validate(self, data):
        """
        Validate if category not exist in the category table
        """
        try:
            category = Category.objects.get(category=data['category'])        
        except:
            raise serializers.ValidationError('That category don\'t exist')
        return data


    def create(self, data):
        """
       Create a movie 
        """
        category = Category.objects.get(category=data['category'])
        data.pop('category')
        movie = Movie.objects.create(**data,category=category)
        return movie