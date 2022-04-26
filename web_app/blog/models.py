from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.BigAutoField(primary_key=True, default="1")
    user_id = models.IntegerField(default='1')
    blog_category = models.IntegerField(default='1')
    blog_title = models.CharField(max_length=250)
    blog_desc = models.TextField()
    blog_img = models.ImageField(upload_to="blog/images", default='untitled.png')
    created_at = models.DateTimeField()

    def __str__(self):
        return self.blog_title
"""
    Reference : https://docs.djangoproject.com/en/4.0/ref/models/fields/
    
    Field.primary_key
    Field.unique
    AutoField
    BigAutoField
    IntegerField
    BigIntegerField
    CharField
    DateField
    DateTimeField
    DecimalField
    EmailField
    JSONField
    PositiveIntegerField
    TextField
"""
