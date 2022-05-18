from django.urls import path
from django.contrib.auth.decorators import login_required,user_passes_test
from . import views
from django.views.generic import RedirectView

urlpatterns = [
    path('', login_required(views.EmployeeView.as_view(),'','login'),name=""),
    path('admins/', login_required(views.AdminView.as_view(),'','login'),name="admins"),
    path('teams/',  login_required(views.TeamView.as_view(),'','login'),name="teams"),
    path('edit/<int:id>', login_required(views.EmployeeView.as_view(is_edit = True),'','login')),
    path('edit_admin/<int:id>', login_required(views.AdminView.as_view(is_edit = True),'','login')),
    path('edit_team/<int:id>', login_required(views.TeamView.as_view(is_edit = True),'','login')),
    path('delete/<str:str>', login_required(views.EmployeeView.as_view(),'','login')),
    path('delete_admin/<str:str>', login_required(views.AdminView.as_view(),'','login')),
    path('team_delete/<str:str>', login_required(views.TeamView.as_view(),'','login')),
    path('team/<int:id>',login_required(views.TeamEmployeeView.as_view(),'','login')),
    path('about-us/', login_required(views.AboutUsView.as_view(),'','login'),name="about-us"),
    path('profile/', login_required(views.ProfileView.as_view(),'','login'),name="profile"),
    path('redirect-view/', RedirectView.as_view(url='https://www.djangoproject.com/')),
]
