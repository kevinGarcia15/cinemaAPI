#Django Rest Framework
from rest_framework import serializers

#model 
from cinema.movies.models import Category

class CategoryModelSerializer(serializers.ModelSerializer):
    """
    Movies Model Serializer
    """

    class Meta:
        """
        Meta class
        """
        model = Category
        
        fields = (
            'category', 'price_ticket',
            'comments'
        )
