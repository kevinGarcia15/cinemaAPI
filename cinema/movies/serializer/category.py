#Django Rest Framework
from rest_framework import serializers

#model 
from cinema.movies.models import Category

#serializer
from cinema.movies.serializer import MoviesModelSerializer


class CategoryModelSerializer(serializers.ModelSerializer):
    """
    Movies Model Serializer
    """
    movie = MoviesModelSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Category
        
        fields = (
            'category', 'price_ticket','movie'
        )
