"""Sales URLS"""

#Django
from django.urls import path, include

#django REST framework
from rest_framework.routers import DefaultRouter

#Views
from cinema.sales.views.sales import SalesViewSet, ReportersViewSet


router = DefaultRouter()
router.register(r'sales', SalesViewSet, basename='sales')
router.register(r'reporters/totalmovies', ReportersViewSet, basename='reporters')
urlpatterns = [
    path('', include(router.urls))
]
