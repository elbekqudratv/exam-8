from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FAQViewSet, ContactView, RequirementsViewSet


router = DefaultRouter()
router.register(r'faqs', FAQViewSet, basename='faq')

router.register(r'requirements',RequirementsViewSet, basename='requirements')



urlpatterns = [
    path('contact/', ContactView.as_view(), name='contact'),
    path('', include(router.urls)),
]