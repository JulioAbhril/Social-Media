from django.shortcuts import render
from .models import SocialPost, SocialComment
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls.base import reverse_lazy
from django.views.generic.base import View
from django.views.generic.edit import UpdateView, DeleteView
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.

class PostDetailView(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)
        
        context = {
            'post': post,
        }
        
        return render(request, 'pages/social/detail.html', context)
    
    def post(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)
        context = {
            'post': post,
        }
        
        return render(request, 'pages/social/edit.html', context)


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model=SocialPost
    fields=['body']
    template_name='pages/social/edit.html'
    
    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('social_media:post_detail', kwargs={'pk':pk})
                            
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=SocialPost
    template_name='pages/social/delete.html'
    success_url = reverse_lazy('home')
    
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
    
class AddLike(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        post = SocialPost.objects.get(pk=pk)
        
        is_like = False
        for like in post.likes.all():
            if like == request.user:
                is_like = True
                break
        
        if not is_like:
            post.likes.add(request.user)
        else:
            post.likes.remove(request.user)

        next = request.POST.get('next','/')
        return HttpResponseRedirect(next)