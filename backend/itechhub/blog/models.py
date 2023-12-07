from django.db import models


class Blog(models.Model):
    name = models.CharField(max_length=255)
    block_content = models.JSONField(default=dict, null=False)

    class Meta:
        abstract = True


class BlogPost(Blog):
    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='blog_post_image')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='blog_post_meta')

    class Meta:
        db_table = 'blog_post'


class BlogCategory(Blog):
    image = models.ForeignKey('common.Image', on_delete=models.CASCADE, related_name='blog_category_image')
    meta = models.ForeignKey('common.Meta', on_delete=models.CASCADE, related_name='blog_category_meta')

    class Meta:
        db_table = 'blog_category'
