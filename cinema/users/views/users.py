"""Users views"""

#django Rest Framework
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

#serializers
from cinema.users.serilizer import(
        UserSignUpSerializer, 
        UserModelSerializer,
        UserLoginSerializer
) 
#permissions

#models 
from cinema.users.models import User

class UserViewSet(viewsets.GenericViewSet):
    """
    Class used for Signup and login user
    """
    queryset = User.objects.filter(is_active=True, is_admin=False)
    serializer_class = UserModelSerializer
    lookup_field = 'username'

    @action(detail=False, methods=['post'])
    def signup(self, request):
        """
        User sign up
        """
        serializer = UserSignUpSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data

        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def login(self, request):
        """
        User login
        """

        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data={
            'user': UserModelSerializer(user).data,
            'access_token': token
        } 

        return Response(data, status=status.HTTP_201_CREATED)