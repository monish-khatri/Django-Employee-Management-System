from django.contrib import admin


# Register your models here.
from .models import Blog, Contact, Category, Tags

admin.site.register(Blog)
admin.site.register(Contact)
admin.site.register(Category)
admin.site.register(Tags)
