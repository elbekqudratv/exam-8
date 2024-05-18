from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicationTypeViewSet, GenderViewSet, PublicationsListView, PublicationsDetailView, AuthorViewSet

router = DefaultRouter()
router.register(r'publicationtypes', PublicationTypeViewSet)
router.register(r'genders', GenderViewSet)
router.register(r'authors', AuthorViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('publications/list/', PublicationsListView.as_view({'get': 'list'}), name='publications-list'),
    path('publications/detail/<int:pk>/', PublicationsDetailView.as_view({'get': 'retrieve'}), name='publications-detail'),
]
