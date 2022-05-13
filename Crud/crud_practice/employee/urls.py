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
    path('delete_admin/<str:str>', views.delete_admin),
    path('team_delete/<str:str>', views.team_delete),
    path('team/<int:id>', views.team_employee),
    path('about-us/', views.about_us),
    path('profile/', views.profile),
]