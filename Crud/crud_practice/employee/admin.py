from django.contrib import admin
from .models import Employee
from reversion.admin import VersionAdmin

# Register your models here.
# admin.site.register(Employee)

# @adminregister(Employee)
class ClientModelAdmin(VersionAdmin):
      pass

@admin.register(Employee)
class Employee(admin.ModelAdmin):
      # Field to show in table
      list_display = ['id','image','name','email','phone','user','team']
      # Searching Funcionality on fields
      search_fields = ['phone','name','email','user__username','team__name']
      # Order by Listing
      ordering = ['-id']
      # Pagination
      list_per_page = 5

      #To Disable add button return False
      def has_add_permission(self, request):
        return True

      #To Disable Delete button return False
      def has_delete_permission(self, request, obj = None):
        return True
