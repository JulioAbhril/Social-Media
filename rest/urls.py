from django.urls import path
from rest_framework import routers
from .api import (
                    ProfileViewSet,     
                    SocialPostViewSet,
                    ImageSerializer,
                    LoginView 
)
 
    

router = routers.DefaultRouter()

router.register('api/rest/profile', ProfileViewSet, 'profile')
router.register('api/rest/post', SocialPostViewSet, 'post')
router.register('api/rest/image', ImageSerializer, 'image')


urlpatterns = [
    path('api/auth/login/', LoginView.as_view(), name='login'),
] + router.urls  
