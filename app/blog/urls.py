"""
URLS mapping for the about API
"""

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.GetAndCreateAPIView.as_view(), name='blog-no-query'),
    path('<int:id>/', views.UpdateAndDestroyAPIView.as_view(), name='blog-query'),

]