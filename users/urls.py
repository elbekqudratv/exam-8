from django.urls import path
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegisterAPIView, PasswordChangeView, PasswordResetView, login



router = DefaultRouter()
router.register(r'register', RegisterAPIView)
router.register(r'password/change/', PasswordChangeView)
router.register(r'password/reset/',PasswordResetView)
router.register(r'login/',login)

urlpatterns = [
    path('', include(router.urls)),
]