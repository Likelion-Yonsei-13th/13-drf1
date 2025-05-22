from django.urls import path
from .views import signup_view, login_view, permission_view

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('permission/', permission_view, name='permission'),  # 인증 확인용
]