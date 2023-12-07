from django.db import models


class Employee(models.Model):
    full_name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    career_summary = models.JSONField(default=dict, null=False)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='employee_images')

    class Meta:
        db_table = 'employee'
