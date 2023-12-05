from django.db import models
from backend.common.models import TechAndSolution, Meta


class Course(models.Model):
    name = models.CharField(max_length=255)
    discount = models.FloatField()
    price = models.FloatField()
    description = models.TextField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE)

    tech_and_solution = models.ManyToManyField(TechAndSolution)

    class Meta:
        db_table = 'course'


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    time_start = models.DateTimeField()
    time_end = models.DateTimeField()
    description = models.TextField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE)

    course = models.ManyToManyField(Course)

    class Meta:
        db_table = 'promotion'
