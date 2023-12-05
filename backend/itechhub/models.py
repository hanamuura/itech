from django.db import models


class Meta(models.Model):
    title = models.CharField(max_length=45)
    description = models.CharField(max_length=100)
    h1 = models.CharField(max_length=35)


# Create your models here.
class Worker(models.Model):
    position = models.CharField(max_length=45)
    experience = models.FloatField()
    image = models.ImageField()
    full_name = models.CharField(max_length=200)


class TechAndSolution(models.Model):
    name = models.CharField(max_length=45)
    image = models.ImageField()


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


class BlogPost(models.Model):
    name = models.CharField(max_length=45)
    description = models.TextField()
    image = models.ImageField()
    meta = models.ForeignKey(Meta)


class BlogCategory(BlogPost):
    pass
