from django.db import models


# точность
class Course(models.Model):
    name = models.CharField(max_length=255)
    discount = models.FloatField(null=True)
    price = models.FloatField()
    block_content = models.JSONField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='images')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='meta')

    tech_and_solution = models.ManyToManyField('common.TechAndSolution', related_name='tech_and_solutions')

    class Meta:
        db_table = 'course'


class Promotion(models.Model):
    name = models.CharField(max_length=255)
    dt_start = models.DateTimeField()
    dt_end = models.DateTimeField()
    block_content = models.JSONField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='images')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='meta')

    course = models.ManyToManyField('academy.Course', related_name='courses')

    class Meta:
        db_table = 'promotion'
