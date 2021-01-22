#django 
from django.db import models

#utils
from cinema.utils.models import CinemaModel

class Sales(CinemaModel):
    """
    Sales model 

    Here is created the model sales ticket for join to watch a movie
    """

    client = models.ForeignKey("users.User", on_delete=models.CASCADE)
    category = models.ForeignKey("movies.Category", on_delete=models.CASCADE, null=True)

    quantity = models.PositiveIntegerField(default=1)
    room = models.CharField("movie room", max_length=50)
    schedule = models.TimeField()

    def __str__(self):
        """Return summary."""
        return 'Movie_id: {} | Schedule: {} | Room: {} | Quantity: {} ticket(s) | category: {}'.format(
            self.category.movie,
            self.schedule,
            self.room,
            self.quantity,
            self.category.category
        )