from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Step(models.Model):
	steps = models.IntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(50000)])
	days = models.DateField(blank=True, null=True, unique_for_date='days')