"""circle serializer"""

#Django Rest Framework
from rest_framework import serializers

#model 
from cinema.movies.models import Movie 

#serializer
from cinema.movies.serializer.category import CategoryModelSerializer

class MoviesModelSerializer(serializers.ModelSerializer):
    """
    Movies Model Serializer
    """
    category = CategoryModelSerializer()
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
