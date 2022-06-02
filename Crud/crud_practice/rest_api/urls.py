from rest_api import views
from rest_framework import routers
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'teams', views.TeamViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('', include('rest_framework.urls', namespace='rest_framework'))
]