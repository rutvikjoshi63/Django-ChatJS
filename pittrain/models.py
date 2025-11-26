from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class PITAirportTrainFact(models.Model):
    dateAdded = models.DateField(auto_now_add=True)
    funFact = models.TextField(blank=True)
    rank = models.IntegerField(
        default=5,
        validators=[MinValueValidator(1), MaxValueValidator(10)],
        help_text="Rank from 1 (bad) to 10 (awesome)"
    )

    def __str__(self):
       return f"{self.dateAdded}: {self.funFact[40:]}..."