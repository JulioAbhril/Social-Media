from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin

from accounts.models import Profile
from accounts.forms import EditProfileForm
from social_media.models import Image, SocialPost, SocialComment
from social_media.forms import SocialPostForm

from core.views import HomeView


# Create your views here.
User = get_user_model()


class UserProfileView(View):        
    def get(self, request, username, *args, **kwargs):
        user = get_object_or_404(User, username=username)
        profile = Profile.objects.get(user=user)
        context = {
            'user':user,
            'profile':profile
        }
        return render(request, 'users/detail.html', context)

@login_required
def EditProfile(request):
    user = request.user.id
    profile = Profile.objects.get(user__id=user)
    user_info = User.objects.get(id=user)
    
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            user_info.first_name = form.cleaned_data.get('first_name')
            user_info.last_name = form.cleaned_data.get('last_name')
            profile.picture = form.cleaned_data.get('picture')
            profile.banner = form.cleaned_data.get('banner')
            profile.location = form.cleaned_data.get('location')
            profile.url = form.cleaned_data.get('url')
            profile.birthday = form.cleaned_data.get('birthday')
            profile.bio = form.cleaned_data.get('bio')
            
            profile.save()
            user_info.save()
            return redirect('users:profile', username=request.user.username)
    else:
        form = EditProfileForm(instance=profile)
    
    context={
        'form':form,
    }
    return render(request, 'users/edit.html', context)


