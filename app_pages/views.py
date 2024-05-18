from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework import viewsets
from django.core.mail import send_mail
from rest_framework import status
from rest_framework.response import Response
from .serializers import ContactSerializer, FAQSerializer, RequirementsSerializer
from .models import Contact, FAQ, Requirements
from .permissions import IsOwnerOrSuperUser
from rest_framework.permissions import IsAdminUser


class ContactView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = ContactSerializer(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            contact_name = data.get('contact_name')
            contact_sender = data.get('contact_sender')
            contact_message = data.get('contact_message')

            # Save the contact instance
            contact = Contact.objects.create(
                contact_name=contact_name,
                contact_sender=contact_sender,
                contact_message=contact_message
            )

            # Send the email
            send_mail(
                subject=f'Contact Form mail from {contact_name}',
                message=contact_message,
                from_email=contact_sender,
                recipient_list=['test@gmail.com'],
                fail_silently=False,
            )

            return Response({"success": "Sent"}, status=status.HTTP_200_OK)
        else:
            return Response({'success': "Failed", 'errors': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)



class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer
    permission_classes = [IsAdminUser]


class RequirementsViewSet(viewsets.ModelViewSet):
    queryset = Requirements.objects.all()
    serializer_class = RequirementsSerializer
    permission_classes = [IsOwnerOrSuperUser]