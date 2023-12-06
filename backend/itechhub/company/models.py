from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    block_content = models.JSONField()

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'company'


class CompanyCase(models.Model):
    title = models.CharField(max_length=255)
    block_content = models.JSONField()

    order_number = models.PositiveIntegerField(default=1, null=False)

    company = models.OneToOneField('itechhub.Company', on_delete=models.CASCADE)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE)

    tech_and_solutions = models.ManyToManyField('common.TechAndSolution', related_name='tech_and_solutions')

    class Meta:
        db_table = 'company_case'


class CompanyService(models.Model):
    name = models.CharField(max_length=255)
    order_number = models.PositiveIntegerField(default=1, null=False)
    block_content = models.JSONField(default={}, null=False)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE)

    class Meta:
        db_table = 'company_service'
