from django.db import models
from backend.coreapp.models import TechAndSolution, Meta


class Worker(models.Model):
    position = models.CharField(max_length=45)
    experience = models.FloatField()
    image = models.ImageField()
    full_name = models.CharField(max_length=200)


class Company(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField()


class Case(models.Model):
    order_number = models.IntegerField()
    company = models.OneToOneField(Company, on_delete=models.CASCADE, primary_key=True)
    tech_and_solutions = models.ManyToManyField(TechAndSolution)
    title = models.CharField(max_length=45)
    image = models.ImageField()
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)


class Service(models.Model):
    order_number = models.IntegerField()
    name = models.CharField(max_length=45)
    image = models.ImageField()
    description = models.TextField()


class BlogPost(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField()
    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)


class BlogCategory(BlogPost):
    pass
