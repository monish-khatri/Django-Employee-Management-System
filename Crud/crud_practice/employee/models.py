from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class EmployeeTeam(models.Model):
    STATUS =(
        ("1", "Active"),
        ("0", "De-active"),
    )
    name = models.CharField(max_length=50)
    status = models.CharField(
        max_length = 20,
        choices = STATUS,
        default = '1'
    )
    class Meta:
        db_table = "employee_groups"

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=50,default='No Name')
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    image = models.ImageField(upload_to='employee/',default='employee/NoImage.png',blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    team = models.ForeignKey(EmployeeTeam,on_delete=models.CASCADE,null=True)
    date_of_birth = models.DateField(null=True,blank=True)
    class Meta:
        db_table = "employee"

    def __str__(self):
        return self.name

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == "group":
            kwargs["queryset"] = EmployeeTeam.objects.order_by('name')
        return super(Employee, self).formfield_for_foreignkey(db_field, request, **kwargs)
