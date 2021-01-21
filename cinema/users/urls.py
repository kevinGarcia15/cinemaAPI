"""users URLS"""

#Django
from django.urls import path, include

#django REST framework
from rest_framework.routers import DefaultRouter

#Views
from cinema.users.views.users import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls))
]
