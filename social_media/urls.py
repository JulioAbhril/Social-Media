from django.urls import path
from .views import PostDeleteView, PostEditView, PostDetailView, AddLike



app_name="social_media"

urlpatterns = [
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/edit/<int:pk>', PostEditView.as_view(), name='post_edit'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('post/<int:pk>/like', AddLike.as_view(), name='like'),
]
