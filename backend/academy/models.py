from django.db import models
#on_delete action


class Course(models.Model):
    name = models.CharField(max_length=255)
    discount = models.DecimalField(decimal_places=2, max_digits=10, null=False)
    price = models.DecimalField(decimal_places=2, max_digits=10, null=False)
    block_content = models.JSONField(default=dict, null=False)
    slag = models.SlugField(max_length=255, unique=True)

    image = models.ForeignKey('common.Image', on_delete=models.RESTRICT, related_name='course_image')
    meta = models.ForeignKey('common.Meta', on_delete=models.RESTRICT, related_name='course_meta')

    tech_and_solution = models.ManyToManyField('common.Technology', related_name='course_technology')

    class Meta:
        db_table = 'academy_course'


# пожизненная акция
class Promotion(models.Model):
    name = models.CharField(max_length=255)
    dt_start = models.DateTimeField()
    dt_end = models.DateTimeField()
    block_content = models.JSONField(default=dict, null=False)
    slug = models.SlugField(max_length=255, unique=True)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='promotion_image')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='promotion_meta')

    course = models.ManyToManyField('academy.Course', related_name='promotion_courses')

    class Meta:
        db_table = 'academy_promotion'
