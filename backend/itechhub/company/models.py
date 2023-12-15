from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=255)
    block_content = models.JSONField(default=dict, null=False)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='company_image')

    class Meta:
        db_table = 'company'


class CompanyCase(models.Model):
    title = models.CharField(max_length=255)
    block_content = models.JSONField(default=dict, null=False)
    slag = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")

    order_number = models.PositiveIntegerField(default=1, null=False)

    company = models.OneToOneField('company.Company', on_delete=models.CASCADE)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='company_case_image')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='company_case_image')

    tech_and_solutions = models.ManyToManyField('common.Technology', related_name='company_case_technology')

    class Meta:
        db_table = 'company_case'


class CompanyService(models.Model):
    name = models.CharField(max_length=255)
    order_number = models.PositiveIntegerField(default=1, null=False)
    block_content = models.JSONField(default=dict, null=False)
    slug = models.SlugField(max_length=255, unique=True)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='company_service_image')

    class Meta:
        db_table = 'company_service'
