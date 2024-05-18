from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, ContactView, RequirementsViewSet


router = DefaultRouter()
router.register(r'faqs', FAQViewSet)
router.register(r'contact', ContactView)
router.register(r'requirements',RequirementsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]