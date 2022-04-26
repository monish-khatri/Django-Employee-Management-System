from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("add_destination", views.add_destination, name="add_destination"),
    path("details/<int:id>", views.details, name="details")
]
