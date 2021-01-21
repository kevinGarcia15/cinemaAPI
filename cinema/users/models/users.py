"""User Admins model"""

#django 
from django.db import models
from django.contrib.auth.models import AbstractUser

#utils
from cinema.utils.models import CinemaModel

class User(CinemaModel, AbstractUser):
    """
    User model extend from CinemaModel
    """
    email = models.EmailField(
        "Email Address", 
        max_length=254
        )
    
    username = models.CharField(
        "username", 
        max_length=50,
        unique  = True,
        error_messages={
            'Unique': 'User already exist'
        })

    is_admin = models.BooleanField(
        "Admin",
        default=False,
        help_text=(
            "Distingish if is admin or client for access to system"
        )
    )

    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']#Campos requeridos u obligatorios


    def __str__(self):
        """
        Retrun Username
        """
        return self.username

    