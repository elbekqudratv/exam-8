from django.urls import path
from .views import RegisterAPIView, PasswordChangeView, PasswordResetView

urlpatterns = [
    path('register/', RegisterAPIView.as_view(), name='register'),
    path('password/change/', PasswordChangeView, name='password_change'),
    path('password/reset/', PasswordResetView, name='password_reset'),
]
