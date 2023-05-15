from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image
import os
from django.db.models.signals import post_save




# Create your models here.

VERIFICATION_OPTIONS = (
    ('unverified', 'unverified'),
    ('verified', 'verified'),
)


def user_directory_path_profile(instance, filename):
    profile_picture_name = 'users/{0}/profile.jpg'.format(instance.user.username)
    full_path = os.path.join(settings.MEDIA_ROOT, profile_picture_name)
    
    if os.path.exists(full_path):
        os.remove(full_path)
    
    return profile_picture_name
    
def user_directory_path_banner(instance, filename):
    banner_picture_name = 'users/{0}/banner.jpg'.format(instance.user.username)
    full_path = os.join(settings.MEDIA_ROOT, banner_picture_name)
    
    if os.path.exist(full_path):
        os.remove(full_path)
    
    return banner_picture_name


class User(AbstractUser):
    strip_customer_id = models.CharField(max_length=50)
    
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    picture = models.ImageField(default='users/user_profile_default.jpeg', upload_to=user_directory_path_profile)
    banner = models.ImageField(default='users/user_banner_default.jpeg', upload_to=user_directory_path_banner)
    verified = models.CharField(max_length=10, choices=VERIFICATION_OPTIONS, default='unverified')
    date_created = models.DateTimeField(auto_now_add=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    url = models.CharField(max_length=2000, null=True, blank=True)
    birthday = models.DateField(null=True, blank=True)
    bio = models.TextField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.user.username
    

def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()



post_save.connect(create_user_profile, sender=User) #to crate profile
post_save.connect(save_user_profile, sender=User) #to save profile
    
    