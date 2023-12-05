from django.db import models
from backend.common.models import TechAndSolution, Meta, Image


class Worker(models.Model):
    position = models.CharField(max_length=45)
    experience = models.FloatField()
    full_name = models.CharField(max_length=200)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'worker'


class Company(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'company'


class Case(models.Model):
    order_number = models.IntegerField()
    title = models.CharField(max_length=255)

    company = models.OneToOneField(Company, on_delete=models.CASCADE, primary_key=True)

    tech_and_solutions = models.ManyToManyField(TechAndSolution)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE)

    class Meta:
        db_table = 'case'


class Service(models.Model):
    order_number = models.IntegerField()
    name = models.CharField(max_length=255)
    description = models.TextField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'service'


class Blog(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField()

    meta = models.ForeignKey(Meta, on_delete=models.CASCADE)


class BlogPost(Blog):
    class Meta:
        db_table = 'blog_post'


class BlogCategory(Blog):
    class Meta:
        db_table = 'blog_category'
