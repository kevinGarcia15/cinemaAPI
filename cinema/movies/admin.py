"""Movie admins """

#django
from django.contrib import admin

#Models
from cinema.movies.models import Movie, Category

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    """
    Movie admin
    """
    
    list_display = (
        'title',
        'year_of_launch',
        'picture',
        'language',
        'duration',
        'rating'
    )

    search_fields = ('title',)

    list_filter = (
        'year_of_launch',
        'language',
        'rating'
    )

  #  actions = ['make_verified', 'make_unverified', 'download_todays_rides']
