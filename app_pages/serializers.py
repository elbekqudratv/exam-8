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