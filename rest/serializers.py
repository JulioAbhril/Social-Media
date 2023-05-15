from rest_framework import serializers
from accounts.models import Profile
from social_media.models import SocialPost, Image



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('user', 'picture', 'banner', 'verified', 'date_created', 'location', 'url', 'birthday', 'bio')

class SocialPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialPost
        fields = ('body', 'image', 'created_on', 'author', 'likes')

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('image', )
        
