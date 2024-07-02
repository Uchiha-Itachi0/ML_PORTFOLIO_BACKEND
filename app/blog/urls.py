"""
URLS mapping for the about API
"""

from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('get/', views.PublicBlogView.as_view(), name='get'),
    path('create/', views.AdminBlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.AdminBlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AdminBlogDeleteView.as_view(), name='delete'),

]