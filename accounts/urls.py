from django.urls import path, include
from .views import UserProfileView, EditProfile

app_name='account'

urlpatterns = [
    path('<username>/', UserProfileView.as_view(), name="profile"),
    path('profile/edit', EditProfile, name="edit-profile"),
    path('social_media/', include('social_media.urls', namespace='social_media')),
]
