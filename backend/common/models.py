from django.db import models


class Image(models.Model):
    path = models.CharField(max_length=255, null=False)
    # hash =

    class Meta:
        db_table = 'image'


class Meta(models.Model):
    title = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    h1_title = models.CharField(max_length=225, null=True)

    seo_image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'meta'


class TechAndSolution(models.Model):
    name = models.CharField(max_length=255)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'tech_and_solution'
