from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=50,default='No Name')
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    class Meta:
        db_table = "employee"