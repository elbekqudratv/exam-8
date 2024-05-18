from rest_framework import viewsets
from .models import PublicationType, Gender, Publications, Author
from .serializers import PublicationTypeSerializer, GenderSerializer, PublicationsListSerializer, PublicationsDetailSerializer, AuthorSerializer

class PublicationTypeViewSet(viewsets.ModelViewSet):
    queryset = PublicationType.objects.all()
    serializer_class = PublicationTypeSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer

class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class PublicationsListView(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsListSerializer

    def get_queryset(self):
        return self.queryset.values('id', 'pub_name_uz', 'pub_desc_uz')

class PublicationsDetailView(viewsets.ModelViewSet):
    queryset = Publications.objects.all()
    serializer_class = PublicationsDetailSerializer