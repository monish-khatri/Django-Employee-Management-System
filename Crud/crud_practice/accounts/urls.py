from django.urls import path

from . import views

urlpatterns = [
    path("register", views.register, name="register"),
    path("", views.login, name="login"),
    path("login", views.login, name="login"),
    path("logout", views.logout, name="logout"),
    path("magic-link/<str:token>", views.login_with_magic_link, name="login_with_magic_link")
]
