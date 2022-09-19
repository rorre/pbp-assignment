from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class MyWatchList(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length=255)
    rating = models.FloatField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5),
        ]
    )
    release_date = models.DateField()
    review = models.TextField()
