from django.db import models
from backend.coreapp.models import TechAndSolution, Meta


class Course(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField()
    discount = models.FloatField()
    price = models.FloatField()
    tech_and_solution = models.ManyToManyField(TechAndSolution)
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
    description = models.TextField()


class Promotion(models.Model):
    course = models.ManyToManyField(Course)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    name = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField()
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)
