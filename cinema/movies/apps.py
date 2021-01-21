"""users apps"""
#django
from django.apps import AppConfig

class MoviesAppConfig(AppConfig):
    """
    Movies app config
    """
    
    name = 'cinema.movies'
    verbose_name = 'Movies' 