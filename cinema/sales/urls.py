"""Sales URLS"""

#Django
from django.urls import path, include

#django REST framework
from rest_framework.routers import DefaultRouter

#Views
from cinema.sales.views.sales import SalesViewSet


router = DefaultRouter()
router.register(r'sales', SalesViewSet, basename='sales')
urlpatterns = [
    path('', include(router.urls))
]
