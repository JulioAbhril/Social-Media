from accounts.models import Profile
from rest_framework.views import APIView
from rest_framework.response import Response
from social_media.models import SocialPost, Image
from rest_framework.permissions import IsAuthenticated
from social_media.views import AddLike
from rest_framework import viewsets, permissions
from django.contrib.auth import authenticate
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import (
    ProfileSerializer, 
    SocialPostSerializer, 
    ImageSerializer,
)

class ProfileViewSet(viewsets.ModelViewSet):
    Profile.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = ProfileSerializer
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return Profile.objects.all()

class SocialPostViewSet(viewsets.ModelViewSet):
    SocialPost.objects.all() 
    permission_classes = [IsAuthenticated]
    serializer_class = SocialPostSerializer
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return SocialPost.objects.all()

class ImageSerializer(viewsets.ModelViewSet):
    Image.objects.all() 
    permission_classes = [IsAuthenticated]
    serializer_class = ImageSerializer
    authentication_classes = [JWTAuthentication]
    
    def get_queryset(self):
        return Image.objects.all()

class LoginView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)

        if user:
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            return Response({'access_token': access_token})
        else:
            return Response({'error': 'Invalid credentials'})

