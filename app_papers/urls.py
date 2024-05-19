from rest_framework.routers import DefaultRouter
from .views import PaperViewSet, ArticleViewSet, AnnotationViewSet, ReferenceViewSet, PaperCountViewSet

router = DefaultRouter()
router.register(r'papers', PaperViewSet, basename='paper')
router.register(r'articles', ArticleViewSet, basename='article')
router.register(r'annotations', AnnotationViewSet, basename='annotation')
router.register(r'references', ReferenceViewSet, basename='reference')
router.register(r'paper-view-count', PaperCountViewSet, basename='paper-count')  # Unique basename

urlpatterns = router.urls