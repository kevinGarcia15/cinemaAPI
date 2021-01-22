"""Sales views."""

# Django REST Framework
from rest_framework import mixins, viewsets, status
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

# Permissions
from rest_framework.permissions import IsAuthenticated

# Serializers
from cinema.sales.serializer import SalesModelSerializer
# Filters
from rest_framework.filters import SearchFilter, OrderingFilter

# Models
from cinema.sales.models import Sales
# Utilities

class SalesViewSet(mixins.ListModelMixin,
                mixins.UpdateModelMixin,
                mixins.RetrieveModelMixin,                                                                                                                                                                                                                                                                                                                      
                mixins.CreateModelMixin,
                viewsets.GenericViewSet):
    """Sales view set."""

    serializer_class = SalesModelSerializer
    queryset = Sales.objects.all()
