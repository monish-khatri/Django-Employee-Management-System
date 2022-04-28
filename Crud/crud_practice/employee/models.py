from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50,default='No Name')
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=12,unique=True)
    class Meta:
        db_table = "employee"