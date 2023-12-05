from django.db import models


class Meta(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    h1 = models.CharField(max_length=35)


class TechAndSolution(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField()