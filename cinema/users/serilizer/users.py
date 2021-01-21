"""User serializer"""
#django
from django.conf import settings
from django.contrib.auth import password_validation, authenticate
from django.core.mail import EmailMultiAlternatives
from django.utils import timezone


#django REST framaework
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from rest_framework.validators import UniqueValidator

#Models
from cinema.users.models.users import User

#Utilities
import jwt
from datetime import timedelta

class UserModelSerializer(serializers.ModelSerializer):
    """
    User model serializer
    """
    class Meta:
        """
        Meta class
        """
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email'
        )

class UserSignUpSerializer(serializers.Serializer):
    """
    User SignUp serializer

    Handle sign up data validation and creation
    """
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    username = serializers.CharField(
        min_length=4,
        max_length=20,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    #password
    password = serializers.CharField(min_length=8, max_length=64)
    password_confirmation =  serializers.CharField(min_length=8, max_length=64)

    #name
    first_name = serializers.CharField(min_length=2, max_length=30)
    last_name = serializers.CharField(min_length=2, max_length=30)


    def validate(self, data):
        """
        Verify password match
        """
        passwrd = data['password']
        passwrd_confirm = data['password_confirmation']

        if passwrd != passwrd_confirm:
            raise serializers.ValidationError('Password does\'t match')

        password_validation.validate_password(passwrd)
        return data

    def create(self, data):
        """
        Handle user creation
        """
        #eliminamos password confirm
        data.pop('password_confirmation')

        #create_user es un metodo propio de django
        user = User.objects.create_user(**data, is_admin=False)

        return user

class UserLoginSerializer(serializers.Serializer):
    """
    User login serializer

    Handle the login and generate Token 
    """
    username = serializers.CharField(max_length=64)
    password =  serializers.CharField(min_length=8, max_length=64)

    def validate(self, data):
        """
        check credentials
        """
        user = authenticate(username=data['username'], password=data['password'])
        if not user:
            raise serializers.ValidationError('invalid credentials')
            
        self.context['user'] = user

#        import ipdb; ipdb.set_trace()
        return data

    def create(self, data):
        """
        Generate or retrive new token
        """
        token, created = Token.objects.get_or_create(user=self.context['user'])
        return self.context['user'], token.key
    