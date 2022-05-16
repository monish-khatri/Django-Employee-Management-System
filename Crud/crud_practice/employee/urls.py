from django.urls import path
from django.contrib.auth.decorators import login_required,user_passes_test
from . import views

urlpatterns = [
    path('', login_required(views.EmployeeView.as_view(),'','login')),
    path('admins/', login_required(views.AdminView.as_view(),'','login')),
    path('teams/',  login_required(views.TeamView.as_view(),'','login')),
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