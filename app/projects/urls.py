"""
URLS mapping for the project API
"""

from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('', views.GetAndCreateProjectAPIView.as_view(), name='get-no-query'),
    path('<int:id>/', views.UpdateAndDeleteProjectAPIView.as_view(), name='get-query'),

]