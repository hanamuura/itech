from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    block_content = models.JSONField(default={}, null=False)

    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='images')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='meta')


class BlogPost(Blog):
    class Meta:
        db_table = 'blog_post'


class BlogCategory(Blog):
    class Meta:
        db_table = 'blog_category'
