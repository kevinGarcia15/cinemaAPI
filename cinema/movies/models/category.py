#django 
from django.db import models
#utils
from cinema.utils.models import CinemaModel

class Category(CinemaModel):
    """
    Category model

    Category movie like childs, or adults. Also they have a price of the ticket
    for each category
    """
    category = models.CharField('movie category', max_length=100)
    price_ticket = models.FloatField(default=0)
    comments = models.TextField(blank=True)

    movie = models.ForeignKey("movies.Movie", on_delete=models.CASCADE)

    def __str__(self):
        """Return summary."""
        return 'movie: {} | category: {}  | Price:  Q{}'.format(
            self.movie.title,
            self.category,
            self.price_ticket
        )