from django.db import models

# Create your models here.
class Blog(models.Model):
    blog_id = models.AutoField
    user_id = models.IntegerField
    blog_title = models.CharField(max_length=250)
    blog_desc = models.TextField()
    blog_img = models.ImageField(upload_to="blog/images")
    created_at = models.DateTimeField()

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
