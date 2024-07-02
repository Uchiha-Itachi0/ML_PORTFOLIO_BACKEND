"""
URLS mapping for the about API
"""

from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('get/', views.AboutView.as_view(), name='get'),
    path('get_admin/', views.AboutUpdateView.as_view(), name='get_admin'),
]