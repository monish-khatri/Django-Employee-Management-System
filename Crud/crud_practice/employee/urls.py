from django.urls import path
from django.contrib.auth.decorators import login_required,user_passes_test
from . import views

urlpatterns = [
    path('', login_required(views.EmployeeView.as_view(),'','login')),
    path('admins/', login_required(views.AdminView.as_view(),'','login')),
    path('teams/',  login_required(views.TeamView.as_view(),'','login')),
    path('edit/<int:id>', login_required(views.EmployeeView.as_view(is_edit = True),'','login')),
    path('edit_admin/<int:id>', login_required(views.AdminView.as_view(is_edit = True),'','login')),
    path('edit_team/<int:id>', login_required(views.TeamView.as_view(is_edit = True),'','login')),
    path('delete/<str:str>', login_required(views.EmployeeView.as_view(),'','login')),
    path('delete_admin/<str:str>', login_required(views.AdminView.as_view(),'','login')),
    path('team_delete/<str:str>', login_required(views.TeamView.as_view(),'','login')),
    path('team/<int:id>', views.team_employee),
    path('about-us/', views.about_us),
    path('profile/', views.profile),
]