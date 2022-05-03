from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee),
    path('users/', views.user_register),
    path('edit/<int:id>', views.edit),
    path('delete/<str:str>', views.delete),
    path('user_delete/<str:str>', views.user_delete),
]