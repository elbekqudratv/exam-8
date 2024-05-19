from rest_framework import serializers
from .models import Contact, FAQ, Requirements



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = ['contact_name', 'contact_sender', 'contact_message']



class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = '__all__'


class RequirementsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Requirements
        fields = '__all__'


#main uchun
        

from rest_framework import serializers
from app_publications.models import Publications
from app_papers.models import Paper

class appPublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publications
        fields = '__all__'

class appPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'