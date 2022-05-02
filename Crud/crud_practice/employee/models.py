from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(max_length=50,default='No Name')
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='employee/',default='employee/NoImage.png',blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name

    # def save(self, *args, **kwargs):
    #     super().save(*args, **kwargs)  # Call the "real" save() method.
