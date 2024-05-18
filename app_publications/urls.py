from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PublicationTypeViewSet, GenderViewSet, PublicationsViewSet, AuthorViewSet, PublicationsListView, PublicationsDetailView

router = DefaultRouter()
router.register(r'pubtypes', PublicationTypeViewSet)
router.register(r'genders', GenderViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'publications', PublicationsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('publications/list/', PublicationsListView.as_view(), name='publications-list'),
    path('publications/detail/<int:pk>/', PublicationsDetailView.as_view(), name='publications-detail'),
]
