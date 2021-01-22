"""Sales serializer"""

#Django Rest Framework
from rest_framework import serializers

#model 
from cinema.sales.models import Sales

#serializer
from cinema.movies.serializer import MoviesModelSerializer, CategoryModelSerializer
from cinema.users.serilizer import UserModelSerializer


class SalesModelSerializer(serializers.ModelSerializer):
    """
    Sales model serializer
    """
    movie = MoviesModelSerializer(read_only=True)
    category = CategoryModelSerializer(read_only=True)
    client = UserModelSerializer(read_only=True)

    class Meta:
        """
        Meta class
        """
        model = Sales
        fields = (
            'movie', 'schedule',
            'room', 'quantity', 'category',
            'client','created'
        )

