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

class PublicationsSerializer(serializers.ModelSerializer):
    pub_type = PublicationTypeSerializer()
    pub_author = AuthorSerializer()

    class Meta:
        model = Publications
        fields = '__all__'
