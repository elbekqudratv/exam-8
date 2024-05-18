# from rest_framework import viewsets, permissions, status
# from rest_framework.response import Response
# from .models import Paper, Article, Annotation, Reference
# from .serializers import PaperSerializer, ArticleSerializer, AdminArticleSerializer
# from rest_framework.decorators import action

# class IsAuthorOrAdmin(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         return obj.author == request.user or request.user.is_staff

# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer

#     def get_permissions(self):
#         if self.action in ['update', 'partial_update', 'destroy']:
#             self.permission_classes = [IsAuthorOrAdmin]
#         elif self.action == 'create':
#             self.permission_classes = [permissions.IsAuthenticated]
#         else:
#             self.permission_classes = [permissions.AllowAny]
#         return super().get_permissions()

#     def perform_create(self, serializer):
#         serializer.save(author=self.request.user)

#     def perform_update(self, serializer):
#         article = self.get_object()
#         if article.status == 'approved':
#             return Response({'error': 'Cannot update an approved article'}, status=status.HTTP_400_BAD_REQUEST)
#         serializer.save()

#     def perform_destroy(self, instance):
#         if instance.status == 'approved':
#             return Response({'error': 'Cannot delete an approved article'}, status=status.HTTP_400_BAD_REQUEST)
#         instance.delete()

#     @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
#     def approve(self, request, pk=None):
#         article = self.get_object()
#         article.status = 'approved'
#         article.save()
#         return Response({'status': 'article approved'})

#     @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
#     def reject(self, request, pk=None):
#         article = self.get_object()
#         article.status = 'rejected'
#         article.save()
#         return Response({'status': 'article rejected'})

#     @action(detail=True, methods=['post'], permission_classes=[permissions.IsAdminUser])
#     def set_publication(self, request, pk=None):
#         article = self.get_object()
#         publication = request.data.get('publication')
#         if not publication:
#             return Response({'error': 'Publication is required'}, status=status.HTTP_400_BAD_REQUEST)
#         article.publication = publication
#         article.save()
#         return Response({'status': 'publication set'})

from rest_framework import viewsets
from .models import Paper, Article, Annotation, Reference
from .serializers import PaperSerializer, ArticleSerializer, AnnotationSerializer, ReferenceSerializer
from .permissions import IsOwnerOrSuperUser

class PaperViewSet(viewsets.ModelViewSet):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    permission_classes = [IsOwnerOrSuperUser]

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsOwnerOrSuperUser]

class AnnotationViewSet(viewsets.ModelViewSet):
    queryset = Annotation.objects.all()
    serializer_class = AnnotationSerializer
    permission_classes = [IsOwnerOrSuperUser]

class ReferenceViewSet(viewsets.ModelViewSet):
    queryset = Reference.objects.all()
    serializer_class = ReferenceSerializer
    permission_classes = [IsOwnerOrSuperUser]


