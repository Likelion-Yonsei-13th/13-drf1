# post/urls.py

from django.urls import path
from .views import create_post, delete_post

urlpatterns = [
    path('', create_post, name='create_post'),  # POST /api/post/
    path('<int:post_id>/delete/', delete_post, name='delete_post'),
]