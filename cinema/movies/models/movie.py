#django 
from django.db import models
from django.core.validators import MinValueValidator

#utils
from cinema.utils.models import CinemaModel

class Movie(CinemaModel):
    """
    Movies model 

    The movies model is a object that contains all 
    character of a muvie like a title, year launch etc.
    """

    title = models.CharField("title", max_length=100)
    year_of_launch =  models.PositiveIntegerField(
        validators=[
            MinValueValidator(1990)
        ]
    )
    picture = models.ImageField(
        "Move cover", 
        upload_to='movies/cover/', 
        blank=True,
        null=True
    )
    language = models.CharField(max_length=50)
    duration = models.PositiveIntegerField()
    rating = models.IntegerField(default=1)
    trama = models.TextField(blank=True)

    category = models.ForeignKey('movies.Category', on_delete=models.CASCADE)

    def __str__(self):
        """Return summary."""
        return '{} | year {} | raiting imdb{}'.format(
            self.title,
            self.year_of_launch,
            self.rating,
        )