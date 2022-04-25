from django.db import models

# Create your models here.


class Destination(models.Model):
    name = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'pics' )
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
