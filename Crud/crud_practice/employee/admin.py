from django.contrib import admin
from .models import Employee,Team
from reversion.admin import VersionAdmin
from django.urls import reverse
from django.utils.http import urlencode
from django.utils.html import format_html

# Register your models here.
# admin.site.register(Employee)

# @adminregister(Employee)
class ClientModelAdmin(VersionAdmin):
      pass

@admin.register(Employee)
class Employee(admin.ModelAdmin):
      def users(self, obj):
            return format_html('<a href="/admin/auth/user/{}/change/">{}</a>',obj.user.id,obj.user)
      users.admin_order_field = 'user'

      def teams(self, obj):
            return format_html('<a href="/admin/employee/team/{}/change/">{}</a>',obj.team.id,obj.team)
      teams.admin_order_field = 'team'

      # Field to show in table
      list_display = ['id','image','name','email','phone','users','teams']
      # Searching Funcionality on fields
      search_fields = ['phone','name','email','user__username','team__name']
      # Order by Listing
      ordering = ['-id']
      # Pagination
      list_per_page = 5
      list_filter = ('user__username', 'team__name')
      #To Disable add button return False
      def has_add_permission(self, request):
        return True

      #To Disable Delete button return False
      def has_delete_permission(self, request, obj = None):
        return True

@admin.register(Team)
class Team(admin.ModelAdmin):
      # Field to show in table
      # Searching Funcionality on fields
      search_fields = ['name']
      # Order by Listing
      ordering = ['-id']
      # Pagination
      list_per_page = 5
      def Status(self, obj):
            return int(obj.status)

      Status.boolean = True
      list_display = ['id','name','Status']
      #To Disable add button return False
      def has_add_permission(self, request):
        return True

      #To Disable Delete button return False
      def has_delete_permission(self, request, obj = None):
        return True
