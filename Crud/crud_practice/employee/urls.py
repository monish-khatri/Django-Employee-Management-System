from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee),
    path('user_register/', views.user_register),
    path('edit/<int:id>', views.edit),
    path('delete/<str:str>', views.delete),
]