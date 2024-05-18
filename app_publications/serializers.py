from rest_framework import serializers
from .models import PublicationType, Gender, Publications, Author

class PublicationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PublicationType
        fields = '__all__'

class GenderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gender
        fields = '__all__'

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class PublicationsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = ['id', 'pub_name_uz', 'pub_desc_uz']

class PublicationsDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'
