"""
URLS mapping for the about API
"""

from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.AboutRetrieveUpdateView.as_view(), name='about'),
]