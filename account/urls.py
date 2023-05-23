from django.urls import path
from account.views import LoginView, RegisterView, UsersView, UserDetailView
from rest_framework_simplejwt.views import (
  TokenRefreshView,
)

urlpatterns = [
  path('register/', RegisterView.as_view()),
  path('login/', LoginView.as_view()),
  path('users/', UsersView.as_view()),
  path('user_detail/<int:pk>/', UserDetailView.as_view()),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]