from django.contrib import admin
from .models import Employee
from reversion.admin import VersionAdmin
# Register your models here.
# admin.site.register(Employee)

@admin.register(Employee)
class ClientModelAdmin(VersionAdmin):
      pass