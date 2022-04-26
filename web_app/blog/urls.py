from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='BlogHome'),
    path('view/<int:id>', views.viewblog, name='BlogView'),
]
