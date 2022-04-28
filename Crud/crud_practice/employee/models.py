from distutils.command.upload import upload
from email.policy import default
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50,default='No Name')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12,unique=True)
    image = models.ImageField(upload_to='employee/',default='employee/NoImage.png',blank=True)
    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name