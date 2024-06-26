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

            
            contact = Contact.objects.create(
                contact_name=contact_name,
                contact_sender=contact_sender,
                contact_message=contact_message
            )

            
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

#MAIN PAGE
    
from rest_framework.views import APIView
from rest_framework.response import Response
from app_publications.models import Publications
from app_papers.models import Paper
from .serializers import appPublicationSerializer, appPaperSerializer

class MainPageView(APIView):
    def get(self, request, format=None):
        latest_publications = Publications.objects.order_by('-publication_date')[:5]  
        most_viewed_papers = Paper.objects.order_by('-paper_view')[:5]  

        publications_serializer = appPublicationSerializer(latest_publications, many=True)
        papers_serializer = appPaperSerializer(most_viewed_papers, many=True)

        return Response({
            'latest_publications': publications_serializer.data,
            'most_viewed_papers': papers_serializer.data
        })
