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

    def __str__(self):
        """Return summary."""
        return '{} Price  Q{}'.format(
            self.category,
            self.price_ticket
        )