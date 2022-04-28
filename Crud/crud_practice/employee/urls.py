from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee),
    path('edit/<int:id>', views.edit),
    path('delete/<str:str>', views.delete),
]