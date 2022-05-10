from django.urls import path

from . import views

urlpatterns = [
    path('', views.employee),
    path('admins/', views.user_register),
    path('teams/', views.teams),
    path('edit/<int:id>', views.edit),
    path('edit_admin/<int:id>', views.edit_admin),
    path('edit_team/<int:id>', views.team_edit),
    path('delete/<str:str>', views.delete),
    path('user_delete/<str:str>', views.user_delete),
    path('team_delete/<str:str>', views.team_delete),
    path('team/<int:id>', views.team_employee),
]