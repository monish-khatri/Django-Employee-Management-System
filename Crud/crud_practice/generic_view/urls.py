from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
        path('create/', views.GeeksCreate.as_view() ),
        path('', views.GeeksList.as_view(),name='list'),
        path('<pk>', views.GeeksDetailView.as_view(),name='detail'),
        path('<pk>/update', views.GeeksUpdateView.as_view()),
        path('<pk>/delete/', views.GeeksDeleteView.as_view()),

]
