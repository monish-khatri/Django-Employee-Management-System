from employee.models import Employee,Team
from rest_api.models import Snippet
from rest_framework import viewsets
from rest_framework import permissions
from django.contrib.auth.models import User,Group,Permission

from rest_api.serializers import TeamSerializer,EmployeeSerializer,UserSerializer,GroupSerializer,SnippetSerializer,PermissionSerializer


class TeamViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teams to be viewed or edited.
    """
    queryset = Team.objects.all().order_by('-id')
    serializer_class = TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teams to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-id')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
class PermissionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Permission.objects.all()
    serializer_class = PermissionSerializer
    permission_classes = [permissions.IsAuthenticated]

class EmployeeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teams to be viewed or edited.
    """
    queryset = Employee.objects.all().order_by('-id')
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows Teams to be viewed or edited.
    """
    queryset = Snippet.objects.all().order_by('-id')
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticated]
