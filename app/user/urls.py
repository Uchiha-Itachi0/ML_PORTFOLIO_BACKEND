"""
URLS mapping for the user API
"""

from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('validate-token/', views.TokenValidationView.as_view(), name='validate-token')
]