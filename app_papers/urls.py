from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PaperViewSet, ArticleViewSet, AnnotationViewSet, ReferenceViewSet

router = DefaultRouter()
router.register(r'papers', PaperViewSet)
router.register(r'articles', ArticleViewSet)
router.register(r'annotations', AnnotationViewSet)
router.register(r'references', ReferenceViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
