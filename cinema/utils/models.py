"""Django models utilities"""

#django
from django.db import models

class CinemaModel(models.Model):
    """
    All our models inherit it of this class
    The CinemaModel use a abstract method, that mean that is a base 
    model and not a table in data base. 
    the following class have functions of Created at and updated at.

    """
    created = models.DateTimeField(
        'created at',
        auto_now_add=True,
        help_text='Date time on which the objetc was created'
    )

    modified = models.DateTimeField(
        'modified at',
        auto_now=True,
        help_text='Date time on which the objetc was last modified'
    )

    class Meta:
        """
        Meta options
        """
        abstract = True

        get_latest_by = 'created'
        ordering = ['-created', '-modified']