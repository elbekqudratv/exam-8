from datetime import datetime
from random import randint

from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings

from rest_framework.generics import CreateAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from config import settings as config_settings
from users.models import PasswordResets
from users.serializers import UserSerializer, PasswordChangeSerializer
from .serializers import PasswordCodeCheck, PasswordEmailCodeSend

from django.contrib.auth import authenticate, login as django_login


@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        django_login(request, user)
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid username or password'}, status=status.HTTP_401_UNAUTHORIZED)



class RegisterAPIView(CreateAPIView):
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        serializer.save()


@api_view(['POST'])
def PasswordChangeView(request):
    if request.method == 'POST':
        serializer = PasswordChangeSerializer(data=request.data)
        if serializer.is_valid():
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            user = request.user
            if user.check_password(old_password):
                user.set_password(new_password)
                user.save()
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            else:
                return Response({'status': 'fail', 'description': 'Old password is incorrect'},
                                status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(
            data={'status': 'fail', 'description': 'Only POST methods allowed'},
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'POST'])
def PasswordResetView(request):
    if request.method == 'POST':
        serializer = PasswordCodeCheck(data=request.data)
        if serializer.is_valid():
            reset_code = serializer.validated_data.get('code')
            new_password = serializer.validated_data.get('new_password')
            try:
                reset_user = PasswordResets.objects.get(reset_code=reset_code, status=True)
                if datetime.now().timestamp() - reset_user.created_at.timestamp() > 600:
                    return Response({'status': 'fail', 'description': 'Code time out'},
                                    status=status.HTTP_400_BAD_REQUEST)
            except PasswordResets.DoesNotExist:
                return Response({'status': 'fail', 'description': 'Code invalid!'}, status=status.HTTP_400_BAD_REQUEST)
            try:
                user = get_user_model().objects.get(pk=int(reset_user.user_id))
                PasswordResets.objects.filter(reset_code=reset_code).update(status=False)
                user.set_password(new_password)
                user.save()
                return Response({'status': 'success'}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({'status': 'fail', 'description': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        serializer = PasswordEmailCodeSend(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            user = get_user_model().objects.filter(email=email).first()
            if user:
                reset_code = f"{randint(100, 999)}-{randint(100, 999)}"
                try:
                    reset_request = PasswordResets.objects.create(user=user, reset_code=reset_code)
                    reset_request.save()
                    send_mail(
                        subject='Password Reset Request',
                        from_email=config_settings.EMAIL_HOST_USER,
                        recipient_list=[email],
                        message=f'Please, insert this code to reset your password: {reset_code}!\n\n'
                                f'Code will expire in 10 minutes.',
                    )
                    return Response(
                        data={'status': 'Code for reset your password sent to your email, check your email, please!'},
                        status=status.HTTP_200_OK
                    )
                except Exception as e:
                    print(e)
                    return Response({'status': 'fail'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            else:
                return Response(
                    data={'status': 'fail', 'description': 'email not found'},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
