"""
URLS mapping for the project API
"""

from django.urls import path
from . import views

app_name = 'project'

urlpatterns = [
    path('get/', views.PublicProjectView.as_view(), name='get'),
    path('create/', views.ProjectCreateAPI.as_view(), name='create'),
    path('update/<int:pk>/', views.ProjectUpdateAPI.as_view(), name='update'),
    path('delete/<int:pk>/', views.ProjectDeleteAPI.as_view(), name='delete'),

]