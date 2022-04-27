from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('view/<int:id>', views.viewblog, name='BlogView'),
    path('add/', views.addblog, name='BlogAdd'),
    path('edit/<int:id>', views.editblog, name='BlogEdit'),
    path('remove/<int:id>', views.removeblog, name='BlogRemove'),
    path('contact', views.contact, name='BlogContact'),
]
